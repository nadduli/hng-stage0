from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hire/python-developers/")
async def get_info():
    """
    Returns basic information in Json Format
    """

    return {
        "email": "naddulidaniel94@gmail.com",
        "current_datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/nadduli/hng-stage0.git",
    }
