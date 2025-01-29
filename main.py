
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


@app.get("/")
async def get_info():
    """
    Returns basic information in Json Format
    """
    return {
        "email": "naddulidaniel94@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "github_url": "https://github.com/nadduli/hng-stage0.git",
    }
