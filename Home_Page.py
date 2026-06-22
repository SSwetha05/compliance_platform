import streamlit as st

st.set_page_config(
page_title="RegiX",
layout="wide",
initial_sidebar_state="expanded"
)

st.title("RegiX")
st.caption("Compliance Lifecycle Management Platform")

st.markdown(
"""
Welcome to RegiX, a centralized platform for managing the compliance
lifecycle from questionnaire creation through checklist review
and final approval.

Use the navigation menu on the left to access different stages of the
workflow.
"""
)

st.subheader("Quick Navigation")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/01_Client_creation.py", label="Client Creation")
    st.page_link("pages/02_Compliance_Type.py", label="Compliance Types")
    st.page_link("pages/03_Questionnaires.py", label="Questionnaires")
    st.page_link("pages/04_Questionnaire_review.py", label="Questionnaire Review")

with col2:
    st.page_link("pages/05_Client_responses.py", label="Client Responses")
    st.page_link("pages/06_Checklists.py", label="Checklists")
    st.page_link("pages/07_Checklist_review.py", label="Checklist Review")
    st.page_link("pages/08_Client_Status.py", label="Client Status")

st.divider()

st.subheader("Compliance Workflow")

st.markdown(
"""
**1. Client Creation**
Register and maintain client information.

**2. Compliance Type Setup**  
Create compliance engagements such as HR, Tax, EHS, Data Privacy, etc.

**3. Questionnaire Management**  
Upload, review, approve, and issue questionnaires.

**4. Client Responses**  
Track and manage responses received from clients.

**5. Checklist Management**  
Create and maintain compliance checklists with version control.

**6. Checklist Review**  
Review checklist revisions and approve only the changes made between versions.

**7. Dashboard & Reporting**  
Monitor workflow progress and review status across engagements.
"""
)

st.divider()

st.subheader("Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    Centralized compliance workflow

        -Questionnaire version control

        -Checklist version control

        -Review and approval tracking
        """
    )

with col2:
    st.markdown(
    """
    Compliance status monitoring

        -Audit trail of reviews

        -File upload management

        -Change-based checklist reviews
        """
    )

st.divider()

st.info(
"Select a module from the sidebar to begin."
)