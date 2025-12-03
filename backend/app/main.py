from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db import Base, engine, get_db
from app.models import Job
from app.schemas import JobCreate, JobRead
from app.celery_app import celery_app
from app.worker.tasks import run_python_job

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/jobs", response_model=JobRead)
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    job = Job(params={"value": payload.value})
    db.add(job)
    db.commit()
    db.refresh(job)

    run_python_job.delay(job.id)
    return job

@app.get("/jobs", response_model=list[JobRead])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()
