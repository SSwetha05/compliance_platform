import streamlit as st
from database import run_query, execute_query
from config import Upload_Folder

st.title("Questionnaires")

law_areas = run_query(
    """
    SELECT
        law_id,
        law_name
    FROM law_areas
    """
)

law_areas_map = {
    row["law_name"]:
    row["law_id"]
    for _, row in law_areas.iterrows()
}

uploaded_file = st.file_uploader(
    "Upload Questionnaire"
)

selected_law = st.selectbox(
    "Compliance Type",
    options=["Select Compliance Type"] + list(law_areas_map.keys()),
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
            law_id,
            version,
            status,
            file_path,
            uploaded_by
        )
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            law_areas_map[selected_law],
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