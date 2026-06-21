import streamlit as st
from database import execute_query, run_query

st.title("Client Creation")

with st.form("client_form"):

    client_name = st.text_input("Client Name")
    industry = st.text_input("Industry")
    state = st.selectbox(
        "State",
        ["Select","Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    )
    contact_name = st.text_input("Contact Name")
    contact_email = st.text_input("Contact Email")
    contact_number = st.text_input("Contact Number")

    submitted = st.form_submit_button("Add Client")

    if submitted:

        execute_query(
            """
            INSERT INTO clients
            (
                client_name,
                industry,
                state,
                contact_name,
                contact_email,
                contact_number
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                client_name,
                industry,
                state,
                contact_name,
                contact_email,
                contact_number
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