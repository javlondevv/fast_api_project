from typing import Optional

from pydantic import BaseModel


class STask(BaseModel):
    name: str
    description: Optional[str] = None


class Task(STask):
    id: int


class STaskID(BaseModel):
    ok: bool = True
    task_id: int
