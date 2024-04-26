from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("All datas deleted")
    await create_tables()
    print("All tables created")
    yield

    print("Turned off")


app = FastAPI(lifespan=lifespan)
# app = FastAPI()
app.include_router(tasks_router)
