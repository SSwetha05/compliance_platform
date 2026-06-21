INSERT INTO clients (
    client_name,
    industry,
	state,
    contact_name,
    contact_email,
	contact_number
)
VALUES (
    'ASV Manufacturing',
    'Manufacturing',
	'Maharashtra',
    'Swetha Sowrirajan',
    'swetha@sse.com',
	'9600005123'
);

INSERT INTO law_areas (
    client_id,
    law_name,
    status
)
VALUES (
    4,
    'HR',
    'Draft'
);

INSERT INTO questionnaires (
    law_id,
    version,
    status,
    file_path,
    uploaded_by
)
VALUES (
    5,
    1,
    'Under Review',
    'uploads/questionnaire_v1.pdf',
    'Associate'
);

INSERT INTO questionnaires (
    law_id,
    version,
    status,
    file_path,
    uploaded_by
)
VALUES (
    5,
    2,
    'Approved',
    'uploads/questionnaire_v2.pdf',
    'Associate'
);

INSERT INTO questionnaire_reviews (
    questionnaire_id,
    reviewer_name,
    review_comment,
    decision
)
VALUES (
    4,
    'Senior Reviewer',
    'Please add PF applicability questions.',
    'Changes Requested'
);

INSERT INTO client_responses (
    questionnaire_id,
    response_file_path,
    status
)
VALUES (
    5,
    'uploads/client_response.xlsx',
    'Completed'
);

INSERT INTO checklists (
    law_id,
    version,
    status,
    file_path,
    uploaded_by
)
VALUES (
    5,
    1,
    'Under Review',
    'uploads/checklist_v1.xlsx',
    'Associate'
);

INSERT INTO checklist_reviews (
    checklist_id,
    reviewer_name,
    review_comment,
    decision
)
VALUES (
    2,
    'Senior Reviewer',
    'Observation #12 requires additional evidence reference.',
    'Changes Requested'
);

INSERT INTO checklists (
    law_id,
    version,
    status,
    file_path,
    uploaded_by
)
VALUES (
    5,
    2,
    'Under Review',
    'uploads/checklist_v2.xlsx',
    'Associate'
);