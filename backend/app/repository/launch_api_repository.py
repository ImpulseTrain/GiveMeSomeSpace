from fastapi import APIRouter
import httpx

# Global router for the LaunchAPIRepository
router = APIRouter() 

class LaunchAPIRepository:
    base_url = (
    "https://ll.thespacedevs.com/2.3.0/launches/"
    "?limit=10&ordering=-net&net__lte=now"
    ) # API endpoint. Please check the documentation for filtering and ordering options.
    def __init__(self):
        print("Launch Repository Object Created")
    
    @staticmethod
    def check_labels(data):
        try:
            assert data['launch_service_provider']['name'] is not None, "Name is missing"
            assert data['mission']['description'] is not None, "Description is missing"
            assert data['mission']['orbit']['name'] is not None, "Orbit is missing"
            return True
        except AssertionError as e:
            print(f"Data validation error: {e}")
            return False

    @classmethod
    async def get_launches(cls):
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(cls.base_url)
        data = response.json()
        print("Data fetched from API")
        print(data)
        # Validate the data
        valid_launches = []
        for launch in data['results']:
            if cls.check_labels(launch):
                valid_launches.append(launch)
        return [
            {
            'name': value['name'],
            'date': value['net'],
            'launch_service_provider': value['launch_service_provider']['name'],
            'status': value['status']['id'],
            'status_message': value['status']['description'],
            'mission_description': value['mission']['description'],
            'orbit': value['mission']['orbit']['name']
            } for value in valid_launches
        ]
        #return data['results']



# Call class method externally
@router.get("/launches")
async def get_launches():
    return await LaunchAPIRepository.get_launches()