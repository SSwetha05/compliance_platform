SELECT
    c.client_name,
    l.law_name,

    q.questionnaire_id,
    q.version AS questionnaire_version,
    q.status AS questionnaire_status,

    qr.reviewer_name AS questionnaire_reviewer,
    qr.decision AS questionnaire_decision,

    cl.checklist_id,
    cl.version AS checklist_version,
    cl.status AS checklist_status,

    cr.reviewer_name AS checklist_reviewer,
    cr.decision AS checklist_decision

FROM clients c
JOIN law_areas l
    ON c.client_id = l.client_id

LEFT JOIN questionnaires q
    ON l.law_id = q.law_id

LEFT JOIN questionnaire_reviews qr
    ON q.questionnaire_id = qr.questionnaire_id

LEFT JOIN checklists cl
    ON l.law_id = cl.law_id

LEFT JOIN checklist_reviews cr
    ON cl.checklist_id = cr.checklist_id;

SELECT *
FROM questionnaires
WHERE law_id = 5
ORDER BY version;

SELECT *
FROM client_responses;

SELECT *
FROM questionnaires
WHERE law_id = 5
ORDER BY version DESC
LIMIT 1;

SELECT *
FROM checklists
WHERE law_id = 5
ORDER BY version DESC
LIMIT 1;

SELECT
    l.law_id,
    c.client_name,

    (
        SELECT q.status
        FROM questionnaires q
        WHERE q.law_id = l.law_id
        ORDER BY q.version DESC
        LIMIT 1
    ) AS questionnaire_status,

    (
        SELECT cr.status
        FROM client_responses cr
        JOIN questionnaires q
            ON cr.questionnaire_id = q.questionnaire_id
        WHERE q.law_id = l.law_id
        ORDER BY cr.uploaded_at DESC
        LIMIT 1
    ) AS client_response_status,

    (
        SELECT cl.status
        FROM checklists cl
        WHERE cl.law_id = l.law_id
        ORDER BY cl.version DESC
        LIMIT 1
    ) AS checklist_status

FROM law_areas l
JOIN clients c
    ON l.client_id = c.client_id;

SELECT
    checklist_id,
    law_id,
    version,
    file_path
FROM checklists;