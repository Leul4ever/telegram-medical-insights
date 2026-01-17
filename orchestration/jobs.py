from dagster import job
from orchestration.ops import (
    scrape_telegram_data, 
    load_raw_to_postgres, 
    run_yolo_enrichment, 
    load_yolo_to_postgres, 
    run_dbt_transformations
)

@job
def medical_insights_pipeline():
    """Main pipeline that orchestrates the entire Telegram Medical Insights workflow."""
    scrape = scrape_telegram_data()
    load_raw = load_raw_to_postgres(scrape)
    yolo = run_yolo_enrichment(load_raw)
    load_yolo = load_yolo_to_postgres(yolo)
    run_dbt_transformations(load_yolo)
