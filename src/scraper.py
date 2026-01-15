import os
import json
import logging
import asyncio
from datetime import datetime
from telethon import TelegramClient, events, errors
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
CHANNELS = [
    'CheMed123',
    'lobelia4cosmetics',
    'tikvahpharma',
    'yetenaweg',
    'EAHPA'
]

# Set up logging
logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)

async def scrape_channel(client, channel_username):
    """Scrapes messages and images from a single channel."""
    try:
        logging.info(f"Starting scraping for channel: {channel_username}")
        entity = await client.get_entity(channel_username)
        
        messages_data = []
        
        # Scrape recent messages (limit can be adjusted)
        async for message in client.iter_messages(entity, limit=100):
            message_date = message.date.strftime('%Y-%m-%d')
            img_path = None
            
            # Download media if present
            if message.photo:
                img_dir = f"data/raw/images/{channel_username}"
                os.makedirs(img_dir, exist_ok=True)
                img_path = f"{img_dir}/{message.id}.jpg"
                await client.download_media(message.photo, img_path)
                logging.debug(f"Downloaded image for message {message.id} in {channel_username}")
            
            # Extract data
            data = {
                'message_id': message.id,
                'channel_name': channel_username,
                'message_date': message.date.isoformat(),
                'message_text': message.message,
                'has_media': bool(message.photo),
                'image_path': img_path,
                'views': message.views or 0,
                'forwards': message.forwards or 0
            }
            messages_data.append(data)
            
            # Store in partitioned JSON
            storage_dir = f"data/raw/telegram_messages/{message_date}"
            os.makedirs(storage_dir, exist_ok=True)
            storage_file = f"{storage_dir}/{channel_username}.json"
            
            # Writing each message append-style or overwriting list
            # Requirements say "channel_name.json" in "YYYY-MM-DD" folder
            # For simplicity, we'll write the list at the end for the channel
            
        storage_dir = f"data/raw/telegram_messages/{datetime.now().strftime('%Y-%m-%d')}"
        os.makedirs(storage_dir, exist_ok=True)
        storage_file = f"{storage_dir}/{channel_username}.json"
        
        with open(storage_file, 'w', encoding='utf-8') as f:
            json.dump(messages_data, f, ensure_ascii=False, indent=4)
            
        logging.info(f"Successfully scraped {len(messages_data)} messages from {channel_username}")

    except errors.FloodWaitError as e:
        logging.warning(f"Rate limited. Waiting for {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)
    except Exception as e:
        logging.error(f"Error scraping {channel_username}: {str(e)}")

async def main():
    client = TelegramClient('scraper_session', API_ID, API_HASH)
    await client.start()
    
    tasks = [scrape_channel(client, channel) for channel in CHANNELS]
    await asyncio.gather(*tasks)
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
