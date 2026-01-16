# Telegram Medical Insights: End-to-End Data Pipeline

## Project Overview
This project, developed for **Kara Solutions**, focuses on building a robust data platform to generate actionable insights from Ethiopian medical businesses. We extract data from public Telegram channels, process it through a modern ELT (Extract, Load, Transform) pipeline, enrich it with AI-powered object detection, and expose it via an analytical API.

### Key Objectives
- **Scrape** data from medical-related Telegram channels.
- **Model** data using a Star Schema in a PostgreSQL warehouse.
- **Transform** raw data using **dbt**.
- **Enrich** data through object detection using **YOLOv8**.
- **Expose** insights via a **FastAPI** analytical service.
- **Orchestrate** the entire flow with **Dagster**.

---

## Project Structure
```text
telegram-medical-insights/
├── .vscode/               # Editor settings
├── .github/workflows/     # CI/CD (Unit Tests)
├── src/                   # Source code (Scrapers, AI logic)
├── api/                   # FastAPI application
├── data/raw/              # Data Lake (JSON & Images) - [Git Ignored]
├── medical_warehouse/     # dbt project
├── notebooks/             # EDA & prototyping
├── tests/                 # Unit tests
├── scripts/               # Database utilities (Ingestion scripts)
├── .env                   # Environment secrets - [Git Ignored]
├── .gitignore             # Standard ignore patterns
├── docker-compose.yml     # Infrastructure (PostgreSQL)
├── Dockerfile             # Python environment
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## Progress

### Phase 1: Repository Setup ✅
- Defined project architecture and Star Schema design.
- Initialized directory structure and configuration files.

### Task 1: Data Scraping and Collection ✅
- **Tool**: Telethon (Telegram API).
- **Functionality**: Multi-channel scraping, image downloading, and partitioned JSON storage.
- **Status**: Completed and verified.

### Task 2: Data Modeling and Transformation ✅
- **Database**: PostgreSQL (Dockerized on port 5433).
- **Ingestion**: Custom Python script (`raw_to_postgres.py`) to load JSON data.
- **Transformation**: **dbt** (Data Build Tool) implementation.
    - **Staging layer**: Data cleaning and standardization.
    - **Marts layer**: Star schema with `dim_channels`, `dim_dates`, and `fct_messages`.
- **Quality**: Built-in and custom dbt tests (13 tests total) passing 100%.

---

## Setup & Usage

### 1. Prerequisites
- Python 3.10+
- Docker Desktop (for PostgreSQL)
- Telegram API credentials.

### 2. Installation
```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup
```powershell
docker-compose up -d
python scripts/raw_to_postgres.py
```

### 4. Running dbt
```powershell
cd medical_warehouse
dbt run
dbt test
```

---

## Next Steps
- **Task 3**: Integrate YOLOv8 for image enrichment.
- **Task 4**: Develop FastAPI analytical endpoints.
