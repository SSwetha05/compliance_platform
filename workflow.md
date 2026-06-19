# Compliance Lifecycle Management Platform

## 1. Client Creation

### Purpose

Create and maintain client master records.

### Database Table

clients

### Responsible Person

Admin / Analyst

### Status Values

N/A

### Key Fields

* client_id
* client_name
* industry
* contact_name
* contact_email

---

## 2. Assessment Creation

### Purpose

Create a compliance engagement for a specific client.

### Database Table

assessments

### Responsible Person

Analyst

### Status Values

* Draft
* Active
* Completed

### Key Fields

* assessment_id
* client_id
* assessment_name
* state
* status

---

## 3. Questionnaire Upload

### Purpose

Upload questionnaire versions for review.

### Database Table

questionnaires

### Responsible Person

Assosiate/ Consultant

### Status Values

* Draft
* Under Review
* Changes Requested
* Approved
* Sent To Client
* Client Responded

### Key Fields

* questionnaire_id
* assessment_id
* version
* file_path
* status
* uploaded_by
* uploaded_at

---

## 4. Questionnaire Review

### Purpose

Review questionnaire and request modifications before client submission.

### Database Table

questionnaire_reviews

### Responsible Person

Senior Consultant/Consultant

### Decision Values

* Approved
* Changes Requested

### Key Fields

* review_id
* questionnaire_id
* reviewer_name
* review_comment
* decision
* reviewed_at

---

## 5. Client Response Submission

### Purpose

Record completed questionnaire received from client.

### Database Table

client_responses

### Responsible Person

Client 

### Status Values

* Awaiting Response
* Partially Completed
* Completed

### Key Fields

* response_id
* questionnaire_id
* response_file_path
* status
* uploaded_at

---

## 6. Checklist Creation

### Purpose

Create compliance checklist based on client responses.

### Database Table

checklists

### Responsible Person

Assosiate/ Consultant

### Status Values

* Draft
* Under Review
* Changes Requested
* Approved

### Key Fields

* checklist_id
* assessment_id
* version
* file_path
* status
* uploaded_by
* uploaded_at

---

## 7. Checklist Review

### Purpose

Review checklist and request corrections before final approval.

### Database Table

checklist_reviews

### Responsible Person

Senior Consultant/ Consultant

### Decision Values

* Approved
* Changes Requested

### Key Fields

* review_id
* checklist_id
* reviewer_name
* review_comment
* decision
* reviewed_at

---

# End-to-End Workflow

Client
↓
Assessment Created
↓
Questionnaire Uploaded
↓
Questionnaire Review
↓
Changes Requested (if any)
↓
Questionnaire Approved
↓
Questionnaire Sent To Client
↓
Client Response Received
↓
Checklist Created
↓
Checklist Review
↓
Changes Requested (if any)
↓
Checklist Approved

# Dashboard Status View

For each Assessment:

* Client Name
* Assessment Name
* Questionnaire Status
* Client Response Status
* Checklist Status

Test Data:

ABC Manufacturing

* Questionnaire: Approved
* Client Response: Completed
* Checklist: Under Review

Future Enhancements
-------------------
- Automatic questionnaire emailing
- Checklist auto-generation from client responses
- User authentication and role management
- Review comment threads
- Evidence/document repository
- Compliance law library integration
- Workshop tracking and closure management