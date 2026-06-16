import streamlit as st
from database import run_query, execute_query

st.title("Questionnaire Reviews")

questionnaires = run_query("""
SELECT
    questionnaire_id,
    questionnaire_id || ' - V' || version AS display_name
FROM questionnaires
ORDER BY questionnaire_id DESC
""")

questionnaire_map = {
    row["display_name"]: row["questionnaire_id"]
    for _, row in questionnaires.iterrows()
}

selected_questionnaire = st.selectbox(
    "Questionnaire",
    options=["Select Version"] + list(questionnaire_map.keys()),
    index=0
)

reviewer_name = st.text_input("Reviewer Name")

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
        INSERT INTO questionnaire_reviews
        (
            questionnaire_id,
            reviewer_name,
            review_comment,
            decision
        )
        VALUES (%s,%s,%s,%s)
        """,
        (
            questionnaire_map[selected_questionnaire],
            reviewer_name,
            review_comment,
            decision
        )
    )

    st.success("Review submitted.")

reviews = run_query("""
SELECT *
FROM questionnaire_reviews
ORDER BY reviewed_at DESC
""")