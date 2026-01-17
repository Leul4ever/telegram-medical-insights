import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def analyze():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT', '5432')
    )
    
    # Query 1: Engagement by Category
    query1 = """
    SELECT 
        image_category, 
        count(*) as post_count, 
        round(avg(view_count)) as avg_views 
    FROM raw.fct_image_detections
    GROUP BY 1
    ORDER BY 3 DESC;
    """
    
    # Query 2: Visual Content by Channel
    query2 = """
    SELECT 
        c.channel_name, 
        count(d.detection_key) as image_count 
    FROM raw.dim_channels c 
    LEFT JOIN raw.fct_image_detections d ON c.channel_key = d.channel_key 
    GROUP BY 1 
    ORDER BY 2 DESC;
    """
    
    cursor = conn.cursor()
    
    print("--- Engagement by Category ---")
    cursor.execute(query1)
    rows = cursor.fetchall()
    print("Category | Count | Avg Views")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    
    print("\n--- Visual Content by Channel ---")
    cursor.execute(query2)
    rows = cursor.fetchall()
    print("Channel | Image Count")
    for row in rows:
        print(f"{row[0]} | {row[1]}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    analyze()
