import streamlit as st
from database import execute_query, run_query

st.title("Client Creation")

with st.form("client_form"):

    client_name = st.text_input("Client Name")
    industry = st.text_input("Industry")
    contact_name = st.text_input("Contact Name")
    contact_email = st.text_input("Contact Email")

    submitted = st.form_submit_button("Add Client")

    if submitted:

        execute_query(
            """
            INSERT INTO clients
            (
                client_name,
                industry,
                contact_name,
                contact_email
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                client_name,
                industry,
                contact_name,
                contact_email
            )
        )

        st.success("Client added successfully.")

clients = run_query(
    """
    SELECT *
    FROM clients
    ORDER BY client_id
    """
)