import streamlit as st
import pandas as pd 
from database import (
    run_query,
    execute_query,
    get_checklist_details,
    get_previous_version
)

from utils.checklist_diff import (
    compare_checklists
)


st.title("Checklist Review")

checklists = run_query(
    """
    SELECT
        checklist_id,
        checklist_id || ' - V' || version
            AS display_name
    FROM checklists
    ORDER BY checklist_id DESC
    """
)

checklist_map = {
    row["display_name"]: row["checklist_id"]
    for _, row in checklists.iterrows()
}

selected = st.selectbox(
    "Checklist Version",
    ["Select Version"] +
    list(checklist_map.keys())
)

if selected != "Select Version":

    checklist_id = checklist_map[selected]

    current = get_checklist_details(
        checklist_id
    )

    previous = get_previous_version(
        checklist_id
    )

    st.subheader("Checklist Information")

    st.write(
        f"Version: V{current['version']}"
    )

    st.write(
        f"Status: {current['status']}"
    )

    if previous is None:

        st.warning(
            "No previous version found. "
            "Full review required."
        )

    else:

        diff = compare_checklists(
            previous["file_path"],
            current["file_path"]
        )

        st.subheader("Change Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total",
            diff["summary"]["total_new"]
        )

        col2.metric(
            "Added",
            diff["summary"]["added"]
        )

        col3.metric(
            "Modified",
            diff["summary"]["modified"]
        )

        col4.metric(
            "Deleted",
            diff["summary"]["deleted"]
        )

        st.subheader("Added Compliances")

        if not diff["added"].empty:
            st.dataframe(
                diff["added"],
                use_container_width=True
            )

        st.subheader("Modified Compliances")

        if diff["modified"]:

            for row in diff["modified"]:

                with st.expander(
                    row["key"]
                ):

                    old_df = (
                        pd.DataFrame(
                            [row["old"]]
                        )
                    )

                    new_df = (
                        pd.DataFrame(
                            [row["new"]]
                        )
                    )

                    st.write("Old")

                    st.dataframe(
                        old_df,
                        use_container_width=True
                    )

                    st.write("New")

                    st.dataframe(
                        new_df,
                        use_container_width=True
                    )

        st.subheader("Deleted Compliances")

        if not diff["deleted"].empty:

            st.dataframe(
                diff["deleted"],
                use_container_width=True
            )

    st.divider()

    reviewer_name = st.text_input(
        "Reviewer Name"
    )

    review_comment = st.text_area(
        "Review Comment"
    )

    decision = st.radio(
        "Review Action",
        [
            "Approved",
            "Changes Requested"
        ]
    )

    if st.button(
        "Submit Review"
    ):

        execute_query(
            """
            INSERT INTO checklist_reviews
            (
                checklist_id,
                reviewer_name,
                review_comment,
                decision
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                checklist_id,
                reviewer_name,
                review_comment,
                decision
            )
        )

        if decision == "Approved":

            execute_query(
                """
                UPDATE checklists
                SET status = 'Approved'
                WHERE checklist_id = %s
                """,
                (checklist_id,)
            )

        else:

            execute_query(
                """
                UPDATE checklists
                SET status =
                    'Changes Requested'
                WHERE checklist_id = %s
                """,
                (checklist_id,)
            )

        st.success(
            "Review submitted."
        )