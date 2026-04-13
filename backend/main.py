from app.repository.s3_repository import s3Repository
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# buckets = s3Repository().list_buckets()
# s3Repository().upload_file('test.txt', buckets[0]['Name'])