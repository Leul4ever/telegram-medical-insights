# Task 1: Data Scraping and Collection (Extract & Load)

## Objective
The goal of this task was to build a robust data scraping pipeline to extract messages and images from Ethiopian medical Telegram channels and store them in a partitioned raw data lake.

## Accomplishments

### 1. Telegram API Setup
- Registered the application at [my.telegram.org](https://my.telegram.org).
- Configured Environment Variables in a `.env` file (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`).
- Implemented **Telethon** library for asynchronous communication with Telegram's MTProto API.

### 2. Scraping Pipeline (`src/scraper.py`)
- **Target Channels**: 
    - `CheMed123`
    - `lobelia4cosmetics`
    - `tikvahpharma`
    - `yetenaweg`
- **Data Extracted**:
    - Message ID, Date (ISO format), Text content.
    - Engagement metrics: Views and Forwards.
    - Media metadata: Detection of photos and storage paths.

### 3. Data Lake Storage Structure
Data is stored using a partitioned approach to optimize future processing:
- **Metadata**: `data/raw/telegram_messages/YYYY-MM-DD/channel_name.json`
- **Images**: `data/raw/images/{channel_name}/{message_id}.jpg`

### 4. Security and Reliability
- **Session Management**: Securely handled 2FA authentication.
- **Git Protection**: `.env`, `.session` files, and raw `data/` are excluded via `.gitignore`.
- **Error Handling**: Implemented logging to `logs/scraper.log` and handled `FloodWaitError` (rate limiting).

### 5. CI/CD Initialization
- Configured GitHub Actions (`.github/workflows/unittests.yml`) to run `pytest` on every push.
- Added a dummy test to ensure pipeline validation.

## Deliverables
- [x] Functional scraper script: `src/scraper.py`
- [x] Partitioned JSON data lake.
- [x] Organized image repository.
- [x] Centralized logging system.
