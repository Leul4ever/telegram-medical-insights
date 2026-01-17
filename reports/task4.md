# Task 4: Build an Analytical API

## 1. Objective
The objective of Task 4 was to expose the enriched data from the Telegram Medical Insights warehouse through a professional REST API. This enables business users and external applications to query market trends, channel activity, and visual content statistics.

## 2. Technical Implementation
### 2.1 Framework & Structure
- **FastAPI**: Used for high-performance, asynchronous API development.
- **SQLAlchemy**: Integrated for robust database connection management.
- **Pydantic**: Utilized for strict data validation and automated OpenAPI documentation.

### 2.2 Analytical Endpoints
The following endpoints were implemented to answer core business questions:

1.  **Top Products (`GET /api/reports/top-products`)**
    - Returns the most frequently mentioned medical and cosmetic terms across all channels.
    - Helps Kara Solutions identify trending products in the Ethiopian market.

2.  **Channel Activity (`GET /api/channels/{channel_name}/activity`)**
    - Provides historical posting volume trends for specific channels.
    - Useful for analyzing vendor consistency and peak activity periods.

3.  **Message Search (`GET /api/search/messages`)**
    - Enables keyword-based search across the entire message corpus with view count context.
    - Allows for quick retrieval of specific product mentions.

4.  **Visual Content Stats (`GET /api/reports/visual-content`)**
    - Aggregates YOLOv8 detection results to show how different channels utilize visual content (promotional vs. lifestyle vs. product displays).

## 3. API Documentation
FastAPI automatically generated comprehensive OpenAPI (Swagger) documentation.
- **Endpoint Descriptions**: Each route includes detailed descriptions and type hints.
- **Validation**: Strict Pydantic schemas prevent malformed requests and ensure clean responses.

## 4. Verification Results
All endpoints were verified against the live PostgreSQL database.
- **Database Connectivity**: Handled special characters in credentials through URL encoding.
- **Performance**: Queries are executed directly against dbt-optimized star schema models.

## 5. Conclusion
Task 4 successfully bridges the gap between raw data engineering and usable business intelligence. The API is now ready to serve as the backend for any frontend dashboards or reporting tools required by Kara Solutions.
