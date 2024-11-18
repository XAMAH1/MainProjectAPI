import os

import uvicorn
from dotenv import load_dotenv
from starlette.responses import HTMLResponse
from user.view import autohorizen

load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


async def get_file(path: str = "html_model/html.html"):
    if not os.path.exists(path):
        return "Error"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


app = FastAPI()


app.include_router(autohorizen, tags=["Пользователь"], prefix=f"/{os.getenv("VERSION")}/user")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def html_main_form():
    return HTMLResponse(content= await get_file(), status_code=200)


if __name__ == "__main__":
    uvicorn.run(app)