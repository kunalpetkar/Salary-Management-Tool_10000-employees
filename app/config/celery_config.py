from celery import Celery

celery_app = Celery(
    "salary_tasks",
    broker="redis://localhost:6379/0"
)
