from pydantic import BaseModel
from datetime import datetime

class LaunchModel(BaseModel):
    name: str
    launchid: str
    launchdate: str
    launch_service_provider: str | None = None
    status: int | None = None
    status_message: str | None = None
    mission_description: str | None = None
    orbit: str | None = None
