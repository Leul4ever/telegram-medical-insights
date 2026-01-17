# Task 3: Data Enrichment with Object Detection (YOLO)

## 1. Objective
The goal of Task 3 was to leverage computer vision (YOLOv8) to analyze the visual content of Telegram messages and integrate these findings into the data warehouse to uncover patterns in promotional strategies.

## 2. Methodology
### 2.1 Environmental Setup
- Installed `ultralytics` for YOLOv8.
- Utilized the `yolov8n.pt` (nano) model for optimal performance.

### 2.2 Classification Logic
Images were categorized into four business-relevant classes based on detected objects:
- **Promotional**: Contains both a `person` and a `product` (bottle, cup, etc.), indicating an active promotion.
- **Product Display**: Contains a `product` (bottle, container) but no person.
- **Lifestyle**: Contains a `person` but no recognizable products.
- **Other**: Neither detected.

## 3. Findings & Analysis

### 3.1 Engagement by Category
| Image Category | Post Count | Avg Views |
| :--- | :--- | :--- |
| **Lifestyle** | 53 | 3,413 |
| **Other** | 155 | 1,814 |
| **Promotional** | 7 | 828 |
| **Product Display** | 55 | 738 |

**Analysis:**
- **Promotional vs. Product Display**: Posts featuring people alongside products (promotional) receive higher engagement (**828 avg views**) compared to those showing only products (**738 avg views**).
- **Lifestyle Content**: Interestingly, posts with people only (lifestyle) have the highest engagement (**3,413 avg views**), suggesting that human-centric content resonates most with the audience in these channels.

### 3.2 Visual Volume by Channel
| Channel | Image Count |
| :--- | :--- |
| **lobelia4cosmetics** | 100 |
| **CheMed123** | 69 |
| **yetenaweg** | 63 |
| **tikvahpharma** | 38 |

**Analysis:**
- `lobelia4cosmetics` is the most visually active channel, fitting for a cosmetics business where product appearance is paramount.
- `tikvahpharma` uses the least amount of visual content among the analyzed channels.

## 4. Technical Limitations
While YOLOv8 provides immediate analytical value, using pre-trained models on COCO datasets for medical tasks has specific drawbacks:
1. **Lack of Domain Specificity**: The model detects a "bottle" but cannot differentiate between life-saving medication and common liquids.
2. **Medical Packaging Anomalies**: Many medical items (pills, blister packs, specialized syringes) are not represented in the COCO dataset, often resulting in them being classified as "other" or misidentified as common objects like "cell phone" or "remote".
3. **Context Misinterpretation**: The model cannot identify the *role* of a person (e.g., a pharmacist in a lab coat vs. a random customer), which is crucial for medical business insights.

## 5. Conclusion
Task 3 successfully added a new layer of "Visual Intelligence" to the data warehouse. By joining the images facts with engagement metrics, we've demonstrated that human presence in photos positively correlates with higher message views.
