from config import Upload_Folder
import streamlit as st
from database import run_query, execute_query

st.title("Checklists")

assessments = run_query("""
SELECT
    assessment_id,
    assessment_name
FROM assessments
""")

assessment_map = {
    row["assessment_name"]: row["assessment_id"]
    for _, row in assessments.iterrows()
}

selected_assessment = st.selectbox(
    "Compliance Type",
    options=["Select Compliance Type"] + list(assessment_map.keys()),
    index=0
)

uploaded_file = st.file_uploader(
    "Upload Checklist"
)

version = st.number_input(
    "Version",
    min_value=1,
    value=1
)

status = st.selectbox(
    "Status",
    [
        "Select",
        "Draft",
        "Under Review",
        "Changes Requested",
        "Approved"
    ]
)

if st.button("Save Checklist"):

    file_path = ""

    if uploaded_file:

        file_path = f"{Upload_Folder}/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    execute_query(
        """
        INSERT INTO checklists
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
            "junior_user"
        )
    )

    st.success("Checklist uploaded.")

checklists = run_query("""
SELECT *
FROM checklists
ORDER BY uploaded_at DESC
""")