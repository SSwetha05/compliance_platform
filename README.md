# RegiX – Compliance Lifecycle Management Platform

## Overview

RegiX is a Streamlit-based application designed to centralize the compliance assessment lifecycle. It replaces fragmented processes involving emails, Excel trackers, questionnaires, checklists, and manual reviews with a structured workflow.

The platform enables teams to manage compliance engagements, track assessment progress, maintain document versions, and record review decisions in one place.

## Key Features

- **Client Management:** Maintain client information and associated compliance engagements.
- **Compliance Type Management:** Organize assessments across areas such as HR and Labour, Taxation, EHS, Data Privacy, and Corporate Laws.
- **Questionnaire Management:** Upload and maintain questionnaire versions.
- **Questionnaire Reviews:** Record reviewer comments, approvals, and change requests.
- **Client Response Tracking:** Upload client responses and monitor completion status.
- **Checklist Management:** Upload and maintain version-controlled compliance checklists.
- **Checklist Version Comparison:** Compare checklist versions using `Comp_ID` to identify added, modified, and deleted compliances.
- **Dashboard:** Track compliance engagements, review statuses, and workflow progress.

## Checklist Version Comparison

Checklist reviews are designed to reduce the effort required to review revised checklists.

Each compliance is identified by a `Comp_ID` such as `CMP_01` or `CMP_02`. The comparison utility uses this identifier to match compliances across versions and identify:

- **Added:** Present in the new version but not the previous version.
- **Modified:** The same `Comp_ID` exists in both versions, but one or more fields have changed.
- **Deleted:** Present in the previous version but absent from the new version.
- **Unchanged:** No tracked fields have changed.

Stable IDs must be retained for existing compliances across versions. New compliances should receive new IDs, and IDs should not be reused for unrelated compliances. The accuracy of the comparison depends on consistent ID management.

## Security and Deployment

The current application is an MVP intended for local development and demonstration.

- PostgreSQL is currently configured for local use.
- Uploaded files are stored in the local `uploads/` directory.
- Authentication and role-based access control are not yet implemented.
- The application should not be used to process sensitive production data in its current configuration.

