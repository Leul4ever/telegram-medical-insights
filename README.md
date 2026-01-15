# Telegram Medical Insights

An end-to-end data pipeline for Telegram, leveraging dbt for transformation, Dagster for orchestration, and YOLOv8 for data enrichment.

## Project Structure
- `src/`: Data scraping and object detection scripts.
- `medical_warehouse/`: dbt project for data transformation.
- `api/`: FastAPI application for analytical endpoints.
- `data/`: Data lake storage (JSON and images).
- `notebooks/`: Exploratory Data Analysis and prototyping.
- `scripts/`: Utility scripts for data loading.

## Requirements
See `requirements.txt` for dependencies.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`.
