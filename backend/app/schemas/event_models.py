from pydantic import BaseModel
from datetime import datetime

class LaunchEvent(BaseModel):
    name: str
    date: datetime
    launch_service_provider: str | None = None
    status: int | None = None
    status_message: str | None = None
    mission_description: str | None = None
    orbit: str | None = None
