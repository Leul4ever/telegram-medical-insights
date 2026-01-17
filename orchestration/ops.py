import subprocess
import os
from dagster import op, get_dagster_logger

logger = get_dagster_logger()

def run_script(script_path, args=None):
    cmd = ["python", script_path]
    if args:
        cmd.extend(args)
    
    logger.info(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        logger.error(f"Error running {script_path}: {result.stderr}")
        raise Exception(f"Script {script_path} failed with exit code {result.returncode}")
    
    logger.info(f"Output: {result.stdout}")
    return result.stdout

@op
def scrape_telegram_data():
    """Step 1: Scrape data from Telegram channels."""
    return run_script("src/scraper.py")

@op
def load_raw_to_postgres(scrape_result):
    """Step 2: Load raw JSON data into PostgreSQL."""
    return run_script("scripts/raw_to_postgres.py")

@op
def run_yolo_enrichment(load_result):
    """Step 3: Detect objects in images using YOLOv8."""
    return run_script("src/yolo_detect.py")

@op
def load_yolo_to_postgres(yolo_result):
    """Step 4: Load detection results into PostgreSQL."""
    return run_script("scripts/load_detections.py")

@op
def run_dbt_transformations(yolo_load_result):
    """Step 5: Run dbt transformations (marts and tests)."""
    # Using our custom run_dbt.py helper to ensure env vars are loaded
    run_script("scripts/run_dbt.py", ["run"])
    return run_script("scripts/run_dbt.py", ["test"])
