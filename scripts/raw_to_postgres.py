import os
import json
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import glob

# Load environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT', '5432')

def load_raw_data():
    """Reads JSON files from data lake and loads them into PostgreSQL raw schema."""
    conn = None
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Create raw schema
        cursor.execute("CREATE SCHEMA IF NOT EXISTS raw;")
        
        # Create raw.telegram_messages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS raw.telegram_messages (
                id SERIAL PRIMARY KEY,
                message_id BIGINT,
                channel_name TEXT,
                message_date TIMESTAMP,
                message_text TEXT,
                has_media BOOLEAN,
                image_path TEXT,
                views INT,
                forwards INT,
                inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Get all JSON files from the data lake
        json_files = glob.glob('data/raw/telegram_messages/**/*.json', recursive=True)
        
        count = 0
        for file_path in json_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                for entry in data:
                    cursor.execute("""
                        INSERT INTO raw.telegram_messages 
                        (message_id, channel_name, message_date, message_text, has_media, image_path, views, forwards)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        entry['message_id'],
                        entry['channel_name'],
                        entry['message_date'],
                        entry['message_text'],
                        entry['has_media'],
                        entry['image_path'],
                        entry['views'],
                        entry['forwards']
                    ))
                    count += 1
        
        conn.commit()
        print(f"Successfully loaded {count} records into raw.telegram_messages.")

    except Exception as e:
        print(f"Error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    load_raw_data()
