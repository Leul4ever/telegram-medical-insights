from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from .database import get_db
from . import schemas

app = FastAPI(
    title="Telegram Medical Insights API",
    description="Analytical API to explore Ethiopian medical business data from Telegram.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Telegram Medical Insights API. Visit /docs for documentation."}

@app.get("/api/reports/top-products", response_model=List[schemas.ProductMention])
def get_top_products(limit: int = 10, db: Session = Depends(get_db)):
    """
    Returns the most frequently mentioned products/terms across all channels.
    Note: Simplified for demonstration (counts common medical terms).
    """
    # A more robust implementation would use a proper NER model or term frequency table
    # For now, we search for common medical product keywords in the fact table
    medical_terms = ['paracetamol', 'amoxicillin', 'insulin', 'cosmetics', 'vitamin', 'mask', 'syrup', 'tablet']
    
    query = f"""
    SELECT term, count(*) as count
    FROM (
        SELECT lower(message_text) as txt FROM raw.fct_messages
    ) t, 
    unnest(array{medical_terms}) as term
    WHERE txt LIKE '%' || term || '%'
    GROUP BY term
    ORDER BY count DESC
    LIMIT :limit
    """
    
    try:
        result = db.execute(text(query), {"limit": limit})
        return [{"term": row[0], "count": row[1]} for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def get_channel_activity(channel_name: str, db: Session = Depends(get_db)):
    """
    Returns daily posting activity trends for a specific channel.
    """
    query = """
    SELECT date_key::text, count(*) as message_count
    FROM raw.fct_messages m
    JOIN raw.dim_channels c ON m.channel_key = c.channel_key
    WHERE c.channel_name = :channel_name
    GROUP BY date_key
    ORDER BY date_key
    """
    
    try:
        result = db.execute(text(query), {"channel_name": channel_name})
        data = [{"date": row[0], "message_count": row[1]} for row in result]
        if not data:
            raise HTTPException(status_code=404, detail="Channel not found or no activity.")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/search/messages", response_model=List[schemas.MessageSearchResult])
def search_messages(query: str = Query(..., min_length=3), limit: int = 20, db: Session = Depends(get_db)):
    """
    Searches for messages containing a specific keyword.
    """
    sql_query = """
    SELECT m.message_id, c.channel_name, m.date_key as message_date, m.message_text, m.view_count
    FROM raw.fct_messages m
    JOIN raw.dim_channels c ON m.channel_key = c.channel_key
    WHERE m.message_text ILIKE :search_term
    ORDER BY m.date_key DESC
    LIMIT :limit
    """
    
    try:
        result = db.execute(text(sql_query), {"search_term": f"%{query}%", "limit": limit})
        return [
            {
                "message_id": row[0],
                "channel_name": row[1],
                "message_date": row[2],
                "message_text": row[3],
                "view_count": row[4]
            } for row in result
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/reports/visual-content", response_model=List[schemas.VisualContentStat])
def get_visual_stats(db: Session = Depends(get_db)):
    """
    Returns statistics about image usage and YOLO detections across channels.
    """
    query = """
    SELECT 
        c.channel_name,
        count(i.detection_key) as image_count,
        count(CASE WHEN i.image_category = 'promotional' THEN 1 END) as promotional_count,
        jsonb_build_object(
            'lifestyle', count(CASE WHEN i.image_category = 'lifestyle' THEN 1 END),
            'product_display', count(CASE WHEN i.image_category = 'product_display' THEN 1 END),
            'other', count(CASE WHEN i.image_category = 'other' THEN 1 END)
        ) as category_distribution
    FROM raw.dim_channels c
    JOIN raw.fct_image_detections i ON c.channel_key = i.channel_key
    GROUP BY c.channel_name
    """
    
    try:
        result = db.execute(text(query))
        return [
            {
                "channel_name": row[0],
                "image_count": row[1],
                "promotional_count": row[2],
                "category_distribution": row[3]
            } for row in result
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
