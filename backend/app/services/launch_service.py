import json
from app.repository.launch_api_repository import LaunchAPIRepository
from app.schemas.launch_models import LaunchModel

class LaunchService:

    @classmethod
    async def fetch_launches(cls) -> list[LaunchModel]:
        """
        Fetches launch data from the LaunchAPIRepository asynchronously, validates it against the pydantic LaunchModel schema and
        returns a list of validated launch data meant to be stored on S3. This method serves as a service layer that abstracts 
        the data retrieval and validation logic, providing a clean interface for the rest of the application to 
        interact with launch data.

        Args:
            None

        Returns:
            list[LaunchModel]: A list of LaunchModel instances containing the validated launch information. 
        """
        data = await LaunchAPIRepository.get_launches()

        validated_launches = []

        for launch in data:
            try:
                validated_launches.append(LaunchModel(**launch))
            except Exception as e:
                print(f"Invalid launch skipped: {e}")
            
        print(validated_launches)

        return validated_launches