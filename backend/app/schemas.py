from pydantic import BaseModel
from typing import Any, Dict, Optional

class JobCreate(BaseModel):
    value: int

class JobRead(BaseModel):
    id: int
    status: str
    params: Dict[str, Any]
    result: Optional[Dict[str, Any]]

    class Config:
        orm_mode = True
