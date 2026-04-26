from fastapi import FastAPI
from app.repository.s3_repository import s3Repository
from app.repository.launch_api_repository import LaunchAPIRepository, router

app = FastAPI()


launch_repository = LaunchAPIRepository()
return_json = launch_repository.get_launches()
app.include_router(router)

print(return_json)
# buckets = s3Repository().list_buckets()
# s3Repository().upload_file('test.txt', buckets[0]['Name'])