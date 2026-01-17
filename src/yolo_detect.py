import os
import csv
from ultralytics import YOLO
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_objects():
    # Load model
    logging.info("Loading YOLOv8n model...")
    model = YOLO('yolov8n.pt') 

    image_dir = 'data/raw/images'
    results_csv = 'data/raw/yolo_detections.csv'
    
    # YOLO Class IDs for COCO: 0: person, 39: bottle, 41: cup, 45: bowl
    # We'll use these as indicators
    PRODUCT_CLASSES = [39, 41, 45, 64, 66] # bottle, cup, bowl, mouse, keyboard (latter two for tech/electronics)
    PERSON_CLASS = 0

    detection_data = []

    if not os.path.exists(image_dir):
        logging.error(f"Image directory {image_dir} does not exist.")
        return

    logging.info(f"Scanning images in {image_dir}...")
    
    # Walk through the channel directories
    for channel_name in os.listdir(image_dir):
        channel_path = os.path.join(image_dir, channel_name)
        if not os.path.isdir(channel_path):
            continue
            
        for img_file in os.listdir(channel_path):
            if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            
            img_path = os.path.join(channel_path, img_file)
            message_id = os.path.splitext(img_file)[0]
            
            # Run detection
            results = model(img_path, verbose=False)
            
            for result in results:
                detected_boxes = result.boxes
                classes = detected_boxes.cls.tolist()
                confidences = detected_boxes.conf.tolist()
                
                # Analyze detections
                has_person = PERSON_CLASS in classes
                has_product = any(cls in PRODUCT_CLASSES for cls in classes)
                
                # Determine category
                if has_person and has_product:
                    category = 'promotional'
                elif has_product and not has_person:
                    category = 'product_display'
                elif has_person and not has_product:
                    category = 'lifestyle'
                else:
                    category = 'other'
                
                # Get the highest confidence or a summary
                detected_names = [model.names[int(cls)] for cls in classes]
                max_conf = max(confidences) if confidences else 0
                
                detection_data.append({
                    'message_id': message_id,
                    'channel_name': channel_name,
                    'detected_objects': ', '.join(detected_names),
                    'confidence_score': round(max_conf, 4),
                    'image_category': category
                })
                
                logging.info(f"Processed {img_file}: Detected {category} ({len(classes)} objects)")

    # Save to CSV
    os.makedirs(os.path.dirname(results_csv), exist_ok=True)
    keys = detection_data[0].keys() if detection_data else ['message_id', 'channel_name', 'detected_objects', 'confidence_score', 'image_category']
    
    with open(results_csv, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(detection_data)
        
    logging.info(f"Detection results saved to {results_csv}")

if __name__ == "__main__":
    detect_objects()
