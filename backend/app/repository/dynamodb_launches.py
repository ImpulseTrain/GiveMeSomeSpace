from app.repository.s3_repository import s3Repository
import pydantic

class DynamoDBLaunches:
    def __init__(self):
        self.s3_repo = s3Repository()

    def write_launches_to_dynamodb(self, table_name: str, launches: list[pydantic.BaseModel]) -> None:
        """
        Writes a list of launch data dictionaries to a DynamoDB table using the s3Repository's write_to_dynamodb method.

        Args:
            table_name (str): The name of the DynamoDB table to write to.
            launches (list[dict]): A list of dictionaries, each representing a launch with its relevant information.

        Returns:
            None unless an exception occurs during the writing process.
        """
        launches_dicts = [launch.model_dump() for launch in launches]  # Convert Pydantic models to dictionaries
        self.s3_repo.write_to_dynamodb(table_name, launches_dicts)