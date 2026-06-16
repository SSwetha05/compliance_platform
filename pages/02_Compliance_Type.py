import streamlit as st
from database import run_query, execute_query

st.title("Compliance Type")

clients = run_query(
    """
    SELECT client_id, client_name
    FROM clients
    ORDER BY client_name
    """
)

client_map = {
    row["client_name"]: row["client_id"]
    for _, row in clients.iterrows()
}

with st.form("assessment_form"):

    selected_client = st.selectbox(
    "Client",
    options=["Select Client"] + list(client_map.keys()),
    index=0
    )

    assessment_name = st.selectbox(
        "Compliance Type",
        ["Select","HR", "Taxation", "Financial", "EHS", "Corporate", "Data Privacy", "Sector-Specific"]
    )

    state = st.selectbox(
        "State",
        ["Select","All", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    )

    status = st.selectbox(
        "Status",
        ["Select","Draft", "Active", "Completed"]
    )

    submitted = st.form_submit_button(
        "Create Compliance Type"
    )

    if submitted:

        execute_query(
            """
            INSERT INTO assessments
            (
                client_id,
                assessment_name,
                state,
                status
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                client_map[selected_client],
                assessment_name,
                state,
                status
            )
        )

        st.success("Compliance Type created.")

assessments = run_query(
    """
    SELECT
        a.assessment_id,
        c.client_name,
        a.assessment_name,
        a.state,
        a.status
    FROM assessments a
    JOIN clients c
        ON a.client_id = c.client_id
    """
)