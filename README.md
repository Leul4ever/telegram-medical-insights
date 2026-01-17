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

### Task 3: Data Enrichment (YOLOv8) ✅
- **Logic**: Automated object detection using **YOLOv8** (nano).
- **Categorization**: Classified 270+ images into `promotional`, `lifestyle`, and `product_display`.
- **Integration**: Results joined with `fct_messages` for engagement analysis.

### Task 4: Analytical API ✅
- **Framework**: **FastAPI** with Pydantic validation.
- **Features**: 
    - Top products reporting.
    - Channel activity tracking.
    - Message search.
    - Visual content statistics.
- **Documentation**: Interactive UI available at `/docs`.

### Task 5: Pipeline Orchestration ✅
- **Tool**: **Dagster**.
- **Automation**: Fully automated Job graph combining scraping, loading, detection, and transformation.
- **Scheduling**: Configured for daily midnight execution.

---

## Setup & Usage

### 1. Prerequisites
- Python 3.10+
- Docker Desktop (for PostgreSQL)
- Telegram API credentials in `.env`.

### 2. Installation
```powershell
pip install -r requirements.txt
```

### 3. Database & dbt
```powershell
docker-compose up -d
python scripts/run_dbt.py run
```

### 4. Running the API
```powershell
python -m uvicorn api.main:app --port 8001 --reload
# Visit http://localhost:8001/docs
```

### 5. Running Orchestration (Dagster)
```powershell
dagster dev -f orchestration/definitions.py
# Visit http://localhost:3000
```

---

## Final Reports
- [Task 1 Report](reports/task1.md)
- [Task 2 Report](reports/task2.md)
- [Task 3 Report](reports/task3.md)
- [Task 4 Report](reports/task4.md)
- [Task 5 Report](reports/task5.md)
- [Interim Project Report](reports/interim_report.md)
