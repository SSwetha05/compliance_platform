from config import Upload_Folder
import streamlit as st
from database import run_query, execute_query

st.title("Client Responses")

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

uploaded_file = st.file_uploader(
    "Upload Client Response"
)

status = st.selectbox(
    "Status",
    [
        "Select",
        "Awaiting Response",
        "Partially Completed",
        "Completed"
    ]
)

if st.button("Save Response"):

    file_path = ""

    if uploaded_file:

        file_path = f"{Upload_Folder}/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    execute_query(
        """
        INSERT INTO client_responses
        (
            questionnaire_id,
            response_file_path,
            status
        )
        VALUES (%s,%s,%s)
        """,
        (
            questionnaire_map[selected_questionnaire],
            file_path,
            status
        )
    )

    st.success("Response saved.")

responses = run_query("""
SELECT *
FROM client_responses
ORDER BY uploaded_at DESC
""")