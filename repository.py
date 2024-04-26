from sqlalchemy import select

from database import new_session, TaskORM
from schemas import STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STask) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_dicts = [task_model.__dict__ for task_model in task_models]
            task_schemas = [STask(**task_dict) for task_dict in task_dicts]
            return task_schemas
