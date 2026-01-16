
with staging as (
    select * from {{ ref('stg_telegram_messages') }}
)

select
    row_number() over (order by channel_name) as channel_key,
    channel_name,
    case 
        when channel_name in ('CheMed123', 'tikvahpharma') then 'Medical'
        when channel_name = 'lobelia4cosmetics' then 'Cosmetics'
        else 'Health'
    end as channel_type,
    min(message_date) as first_post_date,
    max(message_date) as last_post_date,
    count(*) as total_posts,
    avg(view_count) as avg_views
from staging
group by channel_name
