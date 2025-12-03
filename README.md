# Mini Databricks – Distributed Job Orchestrator (MVP)

A small distributed backend platform that executes computation jobs using:

- **FastAPI** – REST API service
- **Celery** – distributed task queue
- **Redis** – message broker
- **PostgreSQL** – job metadata storage
- **Docker Compose** – runs everything locally

This project simulates how platforms like Databricks orchestrate jobs across multiple workers.

---

## Features
- Submit jobs through `/jobs`
- Jobs are stored in PostgreSQL
- Celery workers pick up jobs asynchronously
- Results are stored and retrievable
- Fully containerized

---

## Run it

```bash
docker-compose up --build
