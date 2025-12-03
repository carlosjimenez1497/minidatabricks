from celery import Celery
import os

celery_app = Celery(
    "mini_databricks",
    broker=os.environ["CELERY_BROKER_URL"],
    backend=os.environ["CELERY_RESULT_BACKEND"],
)

celery_app.autodiscover_tasks(["app.worker"])
