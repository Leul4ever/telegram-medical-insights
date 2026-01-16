# Task 2: Data Modeling and Transformation (Transform)

## Objective
The goal of this task was to transform raw, messy Telegram data into a cleaned, structured data warehouse using **dbt** and dimensional modeling (**Star Schema**).

## Accomplishments

### 1. Database Setup
- **PostgreSQL in Docker**: Configured a containerized PostgreSQL 15 database in `docker-compose.yml`.
- **Port Mapping**: Used port **5433** to avoid conflicts with existing local PostgreSQL installations.
- **Environment Management**: Updated `.env` to manage database credentials and connection strings.

### 2. Raw Data Ingestion (`scripts/raw_to_postgres.py`)
- Developed a robust Python script to:
    - Connect to the PostgreSQL database.
    - Create a `raw` schema.
    - Read partitioned JSON files from the Task 1 data lake.
    - Insert data into the `raw.telegram_messages` table.
- **Results**: Successfully loaded **376 records**.

### 3. dbt Project Initialization and Configuration
- Initialized the `medical_warehouse` dbt project.
- Configured `profiles.yml` to connect securely using environment variables.
- Set up target schemas for development and production.

### 4. Dimensional Modeling (Star Schema)
- **Staging Layer**: Cleaned and standardized raw data (handling dates, casting types, and creating flags).
- **Marts Layer**:
    - **`dim_channels`**: Dimension table for channel metadata and aggregate metrics.
    - **`dim_dates`**: Comprehensive date dimension for time-series analysis.
    - **`fct_messages`**: Central fact table containing keys to dimensions and message metrics.

### 5. Data Quality & Testing
- Implemented **13 dbt tests** (unique, not_null, and relationships).
- Added a **custom SQL test** (`assert_positive_views.sql`) to enforce business rules.
- **Outcome**: All tests passed successfully.

### 6. Documentation
- Generated dbt documentation and catalog, providing a searchable interface for the data models.

## Deliverables
- [x] Data Ingestion Script (`scripts/raw_to_postgres.py`)
- [x] dbt project structure and models
- [x] Passing test suite (13/13 tests)
- [x] Generated documentation
