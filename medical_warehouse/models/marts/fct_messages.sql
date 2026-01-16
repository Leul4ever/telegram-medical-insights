
with staging as (
    select * from {{ ref('stg_telegram_messages') }}
),
channels as (
    select * from {{ ref('dim_channels') }}
)

select
    s.message_id,
    c.channel_key,
    s.message_date::date as date_key,
    s.message_text,
    s.message_length,
    s.view_count,
    s.forward_count,
    s.has_image
from staging s
join channels c on s.channel_name = c.channel_name
