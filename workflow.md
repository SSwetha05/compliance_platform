# Compliance Workflow Platform - Workflow Documentation

## Overview

The Compliance Workflow Platform is a Streamlit-based application designed to manage the end-to-end compliance assessment lifecycle.

The platform replaces fragmented workflows currently managed through email, Excel trackers, questionnaires, checklists, and manual reviews.

Primary objectives:

* Centralize compliance workflow management
* Maintain version history for questionnaires and checklists
* Capture review comments and approvals
* Track workflow status across engagements
* Improve reviewer efficiency through version-based change tracking

---

# Workflow Stages

## 1. Client Creation

### Purpose

Create and maintain client master data.

### Database Table

clients

### Output

Client record available for compliance assessments.

---

## 2. Compliance Type Creation

### Purpose

Create compliance engagements for a client.

### Examples

* HR & Labour
* Tax
* EHS
* Data Privacy

### Database Table

assessments

### Notes

Database table name remains:

assessments

UI label displayed as:

Compliance Type

### Output

Assessment record linked to a client.

---

## 3. Questionnaire Upload

### Purpose

Associate uploads compliance questionnaire.

### Workflow

Associate
→ Upload Questionnaire
→ Save File
→ Create Version Record

### Database Table

questionnaires

### Status

Draft

or

Under Review

### Output

Questionnaire version created.

---

## 4. Questionnaire Review

### Purpose

Senior reviewer validates questionnaire content.

### Workflow

Associate Upload
↓
Senior Review
↓
Approve / Request Changes

### Review Actions

Approved

Changes Requested

### Database Table

questionnaire_reviews

### Status Updates

Approved
→ Questionnaire Status = Approved

Changes Requested
→ Questionnaire Status = Changes Requested

---

## 5. Client Response Upload

### Purpose

Store completed questionnaire responses received from clients.

### Workflow

Questionnaire Sent
↓
Client Responds
↓
Response Uploaded

### Database Table

client_responses

### Status Values

Awaiting Response

Partially Completed

Completed

---

## 6. Checklist Creation

### Purpose

Associate prepares compliance checklist based on:

* Compliance assessment scope
* Questionnaire responses
* Regulatory requirements

### Checklist Structure

Current template:

* Comp_ID
* Centre/ State
* Name of Mother Act
* Name of Rules
* Compliance/ Provision Stat
* Applicability
* Compliance Description

### Workflow

Associate
↓
Prepare Checklist
↓
Upload Checklist Version

### Database Table

checklists

### Versioning

Supported through:

checklists.version

Example:

V1
V2
V3

### Status

Draft

Under Review

Approved

Changes Requested

---

## 7. Checklist Review

### Current Problem

Checklist creation requires approximately:

3–4 hours

Checklist review also requires:

3–4 hours

Reviewers currently re-review the entire checklist even when only a small number of rows have changed.

---

## Proposed Solution

Implement version-based checklist comparison similar to GitHub Pull Requests.

### Review Workflow

Associate Uploads V1
↓
Senior Reviewer Reviews
↓
Changes Requested
↓
Associate Uploads V2
↓
System Compares V2 vs V1
↓
Reviewer Reviews Only Changes
↓
Approve / Request Changes

---

## Checklist Diff Process

### Inputs

Current Version File (checklist_v2)

Previous Version File (checklist_v1)

### Comparison Engine

Python Pandas

### Comparison Types

Added Rows

Removed Rows

Modified Rows

### Review Summary

Example:

Total Compliances: 742

Added: 3

Modified: 4

Deleted: 12

---
## Additions
Introduced

Comp_ID

Example:

CMP01

CMP02

CMP03

Benefits:

* Accurate version comparison
* Reliable modification tracking
* Faster reviews
* Better audit trail
---

## Review Actions

Reviewer can:

### Approve

Status:

Approved

### Request Changes

Status:

Changes Requested

---

## Dashboard Workflow

### Purpose

Provide management visibility.

### Metrics

Total Clients

Total Compliance Types

Pending Questionnaire Reviews

Pending Checklist Reviews

Approved Checklists

Completed Client Responses

---

# User Roles (Future)

## Associate

Responsibilities:

* Create questionnaires
* Upload questionnaires
* Upload client responses
* Create checklists
* Upload revised versions

---

## Senior Reviewer

Responsibilities:

* Review questionnaires
* Review checklists
* Approve or request changes
* Monitor quality

---

## Admin

Responsibilities:

* Manage users
* Manage clients
* Configure workflows
* Dashboard oversight

---

# File Storage Workflow

Current:

Local uploads folder

uploads/

### Example

uploads/questionnaire_v1.xlsx

uploads/checklist_v2.xlsx

### Future

* Azure Storage

---

# Status Lifecycle

## Questionnaire

Draft
↓
Under Review
↓
Approved

or

Changes Requested
↓
Reupload
↓
Under Review

---

## Checklist

Draft
↓
Under Review
↓
Approved

or

Changes Requested
↓
Reupload New Version
↓
Under Review

---

# MVP Scope

Included

* Client Management
* Compliance Type Management
* Questionnaire Upload
* Questionnaire Review
* Client Responses
* Checklist Upload
* Checklist Review
* Version Tracking
* Dashboard
* File Upload Storage

Not Included

* Authentication
* Role-Based Access Control
* Email Integration
* AI Checklist Generation
* Row-Level Review Threads

---

# Long-Term Vision

Create a centralized compliance operating platform where:

Client
↓
Assessment
↓
Questionnaire
↓
Review
↓
Client Response
↓
Checklist
↓
Version Comparison
↓
Review
↓
Dashboard Tracking

is managed within a single system with full auditability, version history, and reduced reviewer effort.