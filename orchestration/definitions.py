from dagster import Definitions, ScheduleDefinition
from orchestration.jobs import medical_insights_pipeline

# Daily schedule to run at midnight
daily_pipeline_schedule = ScheduleDefinition(
    job=medical_insights_pipeline,
    cron_schedule="0 0 * * *",
)

defs = Definitions(
    jobs=[medical_insights_pipeline],
    schedules=[daily_pipeline_schedule],
)
