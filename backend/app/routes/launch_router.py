from fastapi import APIRouter
from app.services.launch_service import LaunchService


# Global router for the LaunchAPIRepository
launchRouter = APIRouter() 

# Call class method externally
@launchRouter.get("/launches")
async def get_launches():
    """
    Router get endpoint to fetch and return launch data from the LaunchAPIRepository.
    FastAPI registers this function as an endpoint at the path "/launches". When a GET request is made to this endpoint, 
    FastAPI will call this function, which in turn calls the asynchronous class method fetch_launches() 
    from the LaunchService to retrieve the launch data. 
    The result is returned as a JSON response to the client making the request.

    Args:
        None
    Returns:
        list: A list of dictionaries containing the validated launch information.
    """
    return await LaunchService.fetch_launches()