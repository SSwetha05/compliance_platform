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

with st.form("compliance_type_form"):

    selected_client = st.selectbox(
    "Client",
    options=["Select Client"] + list(client_map.keys()),
    index=0
    )

    law_name = st.selectbox(
        "Compliance Type",
        ["Select","HR", "Taxation", "Financial", "EHS", "Corporate", "Data Privacy", "Sector-Specific"]
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
            INSERT INTO law_areas
            (
                client_id,
                law_name,
                status
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                client_map[selected_client],
                law_name,
                status
            )
        )

        st.success("Compliance Type created.")

law_areas = run_query(
    """
    SELECT
        l.law_id,
        c.client_name,
        l.law_name,
        l.status
    FROM law_areas l
    JOIN clients c
        ON l.client_id = c.client_id
    """
)