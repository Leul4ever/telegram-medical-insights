import os
import csv
import psycopg2
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT', '5432')

def load_detections():
    csv_file = 'data/raw/yolo_detections.csv'
    if not os.path.exists(csv_file):
        logging.error(f"CSV file {csv_file} not found. Run yolo_detect.py first.")
        return

    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Create table
        cursor.execute("CREATE SCHEMA IF NOT EXISTS raw;")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS raw.image_detections (
                id SERIAL PRIMARY KEY,
                message_id BIGINT,
                channel_name TEXT,
                detected_objects TEXT,
                confidence_score FLOAT,
                image_category TEXT,
                inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Clear existing data to avoid duplicates if re-running
        cursor.execute("TRUNCATE TABLE raw.image_detections;")

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute("""
                    INSERT INTO raw.image_detections 
                    (message_id, channel_name, detected_objects, confidence_score, image_category)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    row['message_id'],
                    row['channel_name'],
                    row['detected_objects'],
                    row['confidence_score'],
                    row['image_category']
                ))
        
        conn.commit()
        logging.info("Successfully loaded YOLO detections into raw.image_detections.")

    except Exception as e:
        logging.error(f"Error loading to DB: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    load_detections()
