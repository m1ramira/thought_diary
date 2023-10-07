from fastapi import FastAPI

from app.entries.router import router as entries_router
from app.users.router import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(entries_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
