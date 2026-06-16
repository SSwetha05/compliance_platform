import streamlit as st
from database import run_query, execute_query

st.title("Checklist Reviews")

checklists = run_query("""
SELECT
    checklist_id,
    checklist_id || ' - V' || version AS display_name
FROM checklists
ORDER BY checklist_id DESC
""")

checklist_map = {
    row["display_name"]: row["checklist_id"]
    for _, row in checklists.iterrows()
}

selected_checklist = st.selectbox(
    "Checklist",
    options=["Select Version"] + list(checklist_map.keys()),
    index=0
)

reviewer_name = st.text_input(
    "Reviewer Name"
)

review_comment = st.text_area(
    "Review Comment"
)

decision = st.selectbox(
    "Decision",
    [
        "Select",
        "Approved",
        "Changes Requested"
    ]
)

if st.button("Submit Review"):

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
            checklist_map[selected_checklist],
            reviewer_name,
            review_comment,
            decision
        )
    )

    st.success("Review submitted.")

reviews = run_query("""
SELECT *
FROM checklist_reviews
ORDER BY reviewed_at DESC
""")