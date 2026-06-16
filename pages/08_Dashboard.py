import streamlit as st
from database import run_query

st.title("Dashboard")

query = """
SELECT
    a.assessment_id,
    a.assessment_name AS compliance_type,
    c.client_name,

    (
        SELECT q.status
        FROM questionnaires q
        WHERE q.assessment_id = a.assessment_id
        ORDER BY q.version DESC
        LIMIT 1
    ) AS questionnaire_status,

    (
        SELECT cr.status
        FROM client_responses cr
        JOIN questionnaires q
            ON cr.questionnaire_id = q.questionnaire_id
        WHERE q.assessment_id = a.assessment_id
        ORDER BY cr.uploaded_at DESC
        LIMIT 1
    ) AS client_response_status,

    (
        SELECT cl.status
        FROM checklists cl
        WHERE cl.assessment_id = a.assessment_id
        ORDER BY cl.version DESC
        LIMIT 1
    ) AS checklist_status

FROM assessments a
JOIN clients c
    ON a.client_id = c.client_id

ORDER BY c.client_name;
"""

df = run_query(query)

total_clients = len(df)

approved_questionnaires = (
    df["questionnaire_status"] == "Approved"
).sum()

completed_responses = (
    df["client_response_status"] == "Completed"
).sum()

approved_checklists = (
    df["checklist_status"] == "Approved"
).sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Clients",
        total_clients
    )

with col2:
    st.metric(
        "Approved Questionnaires",
        approved_questionnaires
    )

with col3:
    st.metric(
        "Completed Responses",
        completed_responses
    )

with col4:
    st.metric(
        "Approved Checklists",
        approved_checklists
    )

st.divider()

for _, row in df.iterrows():

    st.subheader(row["client_name"])

    st.caption(
        f"Compliance Type: {row['compliance_type']}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Questionnaire",
            row["questionnaire_status"]
            if row["questionnaire_status"]
            else "Not Started"
        )

    with col2:
        st.metric(
            "Client Response",
            row["client_response_status"]
            if row["client_response_status"]
            else "Awaiting Response"
        )

    with col3:
        st.metric(
            "Checklist",
            row["checklist_status"]
            if row["checklist_status"]
            else "Not Started"
        )

    st.divider()