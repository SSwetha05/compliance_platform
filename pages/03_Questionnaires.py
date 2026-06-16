import streamlit as st
from database import run_query, execute_query
from config import Upload_Folder

st.title("Questionnaires")

assessments = run_query(
    """
    SELECT
        assessment_id,
        assessment_name
    FROM assessments
    """
)

assessment_map = {
    row["assessment_name"]:
    row["assessment_id"]
    for _, row in assessments.iterrows()
}

uploaded_file = st.file_uploader(
    "Upload Questionnaire"
)

selected_assessment = st.selectbox(
    "Compliance Type",
    options=["Select Compliance Type"] + list(assessment_map.keys()),
    index=0
)

status = st.selectbox(
    "Status",
    [
        "Select",
        "Draft",
        "Under Review",
        "Changes Requested",
        "Approved",
        "Sent To Client",
        "Client Responded"
    ]
)

version = st.number_input(
    "Version",
    min_value=1,
    value=1
)

if st.button("Save Questionnaire"):

    file_path = ""

    if uploaded_file:

        file_path = f"{Upload_Folder}/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    execute_query(
        """
        INSERT INTO questionnaires
        (
            assessment_id,
            version,
            status,
            file_path,
            uploaded_by
        )
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            assessment_map[selected_assessment],
            version,
            status,
            file_path,
            "current_user"
        )
    )

    st.success("Questionnaire uploaded.")

questionnaires = run_query(
    """
    SELECT *
    FROM questionnaires
    ORDER BY questionnaire_id DESC
    """
)