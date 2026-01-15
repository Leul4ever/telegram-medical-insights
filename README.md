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
├── scripts/               # Database utilities
├── .env                   # Environment secrets - [Git Ignored]
├── .gitignore             # Standard ignore patterns
├── docker-compose.yml     # Infrastructure orchestration
├── Dockerfile             # Python environment
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## Progress

### Phase 1: Planning & Initialization ✅
- Defined project architecture and Star Schema design.
- Initialized directory structure and configuration files.
- Set up CI/CD workflow for automated testing.

### Task 1: Data Scraping and Collection ✅
- **Tool**: Telethon (Telegram API).
- **Functionality**:
    - Multi-channel scraping (CheMed123, lobelia4cosmetics, yetenaweg, tikvahpharma).
    - Metadata extraction (Message ID, Date, Text, Views, Forwards).
    - Image downloading to channel-specific folders.
    - Partitioned Data Lake storage (JSON by date).
- **Security**: 
    - Session files and credentials protected by `.gitignore`.
    - Rate limit handling (FloodWait) implemented.

---

## Setup & Usage

### 1. Prerequisites
- Python 3.10+
- Telegram API credentials (`api_id` and `api_hash`) from [my.telegram.org](https://my.telegram.org).

### 2. Installation
```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
TELEGRAM_API_ID=your_id
TELEGRAM_API_HASH=your_hash
DATABASE_URL=postgresql://user:password@localhost:5432/medical_db
```

### 4. Running the Scraper
```powershell
python src/scraper.py
```

---

## Next Steps
- **Task 2**: Implement Data Modeling and Transformation using dbt.
- **Task 3**: Integrate YOLOv8 for image enrichment.
