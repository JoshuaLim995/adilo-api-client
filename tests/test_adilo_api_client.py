import os
import unittest

from dotenv import load_dotenv

from adilo_api_client.adilo_api import AdiloAPI

load_dotenv()  # take environment variables from .env.


class TestAdiloAPI(unittest.TestCase):
    def setUp(self):
        public_key = os.getenv("ADILO_PUBLIC_KEY")
        secret_key = os.getenv("ADILO_SECRET_KEY")

        if not public_key or not secret_key:
            raise AssertionError(
                "ADILO_PUBLIC_KEY and ADILO_SECRET_KEY environment variables must be set"
            )

        self.adilo_api = AdiloAPI(public_key, secret_key)
        self.project_id = None

    def create_project(self, title: str):
        project = self.adilo_api.create_project(title)
        self.project_id = project.id
        return project

    def create_folder(self, project_id, name, parent_id=None):
        return self.adilo_api.create_folder(project_id, name, parent_id)

    def tearDown(self):
        if self.project_id:
            result = self.adilo_api.delete_project_by_id(self.project_id)
            self.assertEqual(
                result, True, f"failed to delete project {self.project_id}"
            )


if __name__ == "__main__":
    unittest.main()
