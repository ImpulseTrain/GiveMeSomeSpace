from datetime import datetime, timezone, date
from fastapi import APIRouter
import httpx

class LaunchAPIRepository:
    
    now = date.today().isoformat()
    base_url = f"https://ll.thespacedevs.com/2.3.0/launches/?limit=10&ordering=-net&net__lte={now}"
    # API endpoint. Please check the documentation for filtering and ordering options.
    # ordering = -net means we want to order the launches by their net (launch date) in descending order (latest first).
    # net__lte={now} is a filter that ensures we only get launches that are scheduled to occur on or before the current date, effectively giving us past launches.

    def __init__(self):
        print("Launch Repository Object Created")
    
    @staticmethod
    def check_labels(data) -> bool:
        """
        Checks if the required labels are present in the data returned by the API (json type).

        Validated entries:

        - launch_service_provider.name
        - mission.description
        - mission.orbit.name 

        Args:
            data (json like dict): The data to be validated.

        Returns:
            bool: True if all required labels are validated with no errors, False otherwise.
        """
        try:
            assert data['launch_service_provider']['name'] is not None, "Name is missing"
            assert data['mission']['description'] is not None, "Description is missing"
            assert data['mission']['orbit']['name'] is not None, "Orbit is missing"
            return True
        except AssertionError as e:
            print(f"Data validation error: {e}")
            return False

    @classmethod
    async def get_launches(cls) -> list :
        """
        Asynchronous class method to fetch launch data from the API, validate it, and return a list of 
        launches with the required information. This is the method that helps in retrieving what is relavent 
        from the API.

        Returned data includes:
        - name
        - date
        - launch_service_provider
        - status
        - status_message
        - mission_description
        - orbit

        Args:
            None

        Returns:
            list: A list of dictionaries containing the validated launch information.
    """
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(cls.base_url)
        data = response.json()
        print("Data fetched from API")
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



