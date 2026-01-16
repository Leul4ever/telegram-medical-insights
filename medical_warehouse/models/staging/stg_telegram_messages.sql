
with raw_data as (
    select * from {{ source('raw', 'telegram_messages') }}
)

select
    message_id,
    channel_name,
    message_date::timestamp as message_date,
    message_text,
    has_media,
    image_path,
    views as view_count,
    forwards as forward_count,
    length(message_text) as message_length,
    case when image_path is not null then true else false end as has_image
from raw_data
where message_id is not null
