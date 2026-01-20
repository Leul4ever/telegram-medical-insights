
with raw_detections as (
    select * from {{ source('raw', 'image_detections') }}
),

messages as (
    select * from {{ ref('fct_messages') }}
)

select
    d.id as detection_key,
    m.message_id,
    m.channel_key,
    m.date_key,
    m.view_count,
    m.forward_count,
    d.detected_objects as detected_class,
    d.confidence_score,
    d.image_category
from raw_detections d
join messages m on d.message_id = m.message_id
