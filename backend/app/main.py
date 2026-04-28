from fastapi import FastAPI
from app.repository.s3_repository import s3Repository
from app.repository.launch_api_repository import LaunchAPIRepository
from app.routes.launch_router import launchRouter
from app.schemas.launch_models import LaunchModel

app = FastAPI()

app.include_router(launchRouter) # Register the router from the LaunchAPIRepository to make its endpoints available in the FastAPI application.


# Create a launch model schema instance


# buckets = s3Repository().list_buckets()
# s3Repository().upload_file('test.txt', buckets[0]['Name'])