# GEMINI.md: Project Context and AI Guide

This file provides critical information, context, and structural details for the Gemini AI model to effectively assist with development, testing, and documentation tasks within this project.

## 1. Project Overview

* **Project Name:** market-analysis-app
* **Purpose/Goal:** A real-time analytics dashboard for crypto and stocks data.
* **Current Status:** Feature development phase.
* **Target Audience:** End-users via web application

## 2. Technology Stack & Languages

| Category | Technology/Library | Version (if critical) | Notes |
| :--- | :--- | :--- | :--- |
| **Backend** | Python | 3.14.0 | |
| **Frontend** | Streamlit | 1.52.2 | |
| **Database** | [e.g., PostgreSQL] | [e.g., 14] | [e.g., Managed via AWS RDS] |

## 3. Key Directories & File Structure

This is crucial for the AI to locate relevant files when asked to modify or review code.

| Path | Contents/Purpose | Key Files to Note |
| :--- | :--- | :--- |
| `/src/` | Primary application source code. | `main.py`, `settings.ts` |
| `/src/api/` | All API endpoints and routing logic. | `routes.py`, `schemas.py` |
| `/tests/` | Unit and integration tests. | `conftest.py` |
| `/docs/` | User and developer documentation (Sphinx, MkDocs, etc.). | `index.rst` |
| `/dbt/` | All dbt models, macros, and configuration. | `dbt_project.yml`, `models/staging/` |

## 4. Coding & Style Guidelines

* **Language Style:** [e.g., PEP 8 for Python, Airbnb style for JavaScript]
* **Commenting:** [e.g., Use Google docstrings for all public functions.]
* **Variable Naming:** [e.g., `snake_case` for variables, `PascalCase` for classes.]

## 5. Important Conventions & Macros (for Data/DB Projects)

* **Naming Convention (dbt):** [e.g., `stg_` for staging, `mart_` for marts.]
* **Common Macro/Function:** [Define a custom function or macro that is heavily used.]
    * **Name:** `{{ custom_hashing(column) }}`
    * **Purpose:** [Encrypts PII before staging.]

## 6. Current Focus & Known Issues

* **Priority 1:** [E.g., Complete the authorization flow for the `/v2/` API endpoint.]
* **Priority 2:** [E.g., Refactor the `CustomerModel` class to use async methods.]
* **Known Bugs:** [E.g., Frontend filter selection sometimes defaults back to the oldest date.]