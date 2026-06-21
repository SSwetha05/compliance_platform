CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
	state VARCHAR(50) NOT NULL,
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
	contact_number VARCHAR(20)
);

CREATE TABLE law_areas (
    law_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL,
    law_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL
		CHECK (
		    status IN (
		        'Draft',
		        'Under Review',
		        'Changes Requested',
		        'Approved',
		        'Sent To Client',
		        'Client Responded')
		),

    CONSTRAINT fk_law_areas_client
        FOREIGN KEY (client_id)
        REFERENCES clients(client_id)
        ON DELETE CASCADE
);

CREATE TABLE questionnaires (
    questionnaire_id SERIAL PRIMARY KEY,
    law_id INTEGER NOT NULL,
    version INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL
		CHECK (
		    status IN (
		        'Draft',
		        'Under Review',
		        'Changes Requested',
		        'Approved',
		        'Sent To Client',
		        'Client Responded')
		),
    file_path TEXT NOT NULL,
    uploaded_by VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_questionnaire_assessment
        FOREIGN KEY (law_id)
        REFERENCES law_areas(law_id)
        ON DELETE CASCADE
);

CREATE TABLE questionnaire_reviews (
    review_id SERIAL PRIMARY KEY,
    questionnaire_id INTEGER NOT NULL,

    reviewer_name VARCHAR(255) NOT NULL,

    review_comment TEXT NOT NULL,

    decision VARCHAR(50) NOT NULL
        CHECK (
            decision IN (
                'Approved',
                'Changes Requested'
            )
        ),

    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_review_questionnaire
        FOREIGN KEY (questionnaire_id)
        REFERENCES questionnaires(questionnaire_id)
        ON DELETE CASCADE
);

CREATE TABLE client_responses (
    response_id SERIAL PRIMARY KEY,

    questionnaire_id INTEGER NOT NULL,

    response_file_path TEXT NOT NULL,

    status VARCHAR(50) NOT NULL
        CHECK (
            status IN (
                'Awaiting Response',
                'Partially Completed',
                'Completed'
            )
        ),

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_response_questionnaire
        FOREIGN KEY (questionnaire_id)
        REFERENCES questionnaires(questionnaire_id)
        ON DELETE CASCADE
);

CREATE TABLE checklists (
    checklist_id SERIAL PRIMARY KEY,

    law_id INTEGER NOT NULL,

    version INTEGER NOT NULL,

    status VARCHAR(50) NOT NULL,

    file_path TEXT NOT NULL,

    uploaded_by VARCHAR(255),

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_checklist_law
        FOREIGN KEY (law_id)
        REFERENCES law_areas(law_id)
        ON DELETE CASCADE
);

CREATE TABLE checklist_reviews (
    review_id SERIAL PRIMARY KEY,

    checklist_id INTEGER NOT NULL,

    reviewer_name VARCHAR(255) NOT NULL,

    review_comment TEXT NOT NULL,

    decision VARCHAR(50) NOT NULL
        CHECK (
            decision IN (
                'Approved',
                'Changes Requested'
            )
        ),

    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_review_checklist
        FOREIGN KEY (checklist_id)
        REFERENCES checklists(checklist_id)
        ON DELETE CASCADE
);