import requests
import json

BASE_URL = "http://localhost:8001"

def test_root():
    r = requests.get(f"{BASE_URL}/")
    print(f"Root: {r.status_code}")
    print(r.json())

def test_top_products():
    r = requests.get(f"{BASE_URL}/api/reports/top-products?limit=5")
    print(f"\nTop Products: {r.status_code}")
    print(json.dumps(r.json(), indent=2))

def test_channel_activity():
    # Test with one of our channels
    channel = "CheMed123" 
    r = requests.get(f"{BASE_URL}/api/channels/{channel}/activity")
    print(f"\nChannel Activity ({channel}): {r.status_code}")
    # Show first 3 entries
    data = r.json()
    if isinstance(data, list):
        print(json.dumps(data[:3], indent=2))
    else:
        print(json.dumps(data, indent=2))

def test_search():
    query = "paracetamol"
    r = requests.get(f"{BASE_URL}/api/search/messages?query={query}&limit=2")
    print(f"\nSearch ({query}): {r.status_code}")
    print(json.dumps(r.json(), indent=2))

def test_visual_stats():
    r = requests.get(f"{BASE_URL}/api/reports/visual-content")
    print(f"\nVisual Stats: {r.status_code}")
    print(json.dumps(r.json(), indent=2))

if __name__ == "__main__":
    try:
        test_root()
        test_top_products()
        test_channel_activity()
        test_search()
        test_visual_stats()
    except Exception as e:
        print(f"Error: {e}")
