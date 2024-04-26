from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks APi"]
)


@router.post("")
async def add_tasks(
        task: Annotated[STask, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
