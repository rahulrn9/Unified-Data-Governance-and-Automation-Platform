# Centralized Data Governance Framework

This repository contains scripts and templates to:
- Discover and register S3 buckets and RDS tables in Apache Atlas
- Automate data lineage ingestion from logs
- Enforce data access policies based on Excel templates
- Run data quality checks
- Perform automated classification of assets
- Generate data profiling reports
- Track usage analytics
- Send Slack notifications for access requests
- Provide a basic search UI via FastAPI
- Automate data retention and deletion

## Structure

- `scripts/`: Python scripts for each component
- `templates/`: Excel templates for policies and rules
- `profiles/`: Output directory for profiling reports (generated)
- `profiles.zip`: Zipped profiles (generated)

## Getting Started

1. Clone the repo
2. Fill in configuration (Atlas endpoints, AWS/RDS credentials, Slack token)
3. Install dependencies: `pip install boto3 pandas psycopg2 sqlalchemy pandas-profiling slack-sdk fastapi`
4. Run individual scripts or orchestrate with Airflow/cron

