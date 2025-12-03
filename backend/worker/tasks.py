from celery import shared_task
from app.db import SessionLocal
from app.models import Job

@shared_task
def run_python_job(job_id: int):
    db = SessionLocal()
    job = db.query(Job).get(job_id)

    job.status = "RUNNING"
    db.commit()

    try:
        value = job.params["value"]
        result = {"squared": value * value}

        job.result = result
        job.status = "COMPLETED"

    except Exception as e:
        job.status = "FAILED"
        job.result = {"error": str(e)}

    db.commit()
    db.close()
