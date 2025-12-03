from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="PENDING")
    params = Column(JSON)
    result = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
