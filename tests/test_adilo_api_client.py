import os
import unittest

from dotenv import load_dotenv

from adilo_api_client.adilo_api import AdiloAPI

load_dotenv()  # take environment variables from .env.


class TestAdiloAPI(unittest.TestCase):
    def setUp(self):
        public_key = os.getenv("ADILO_PUBLIC_KEY")
        secret_key = os.getenv("ADILO_SECRET_KEY")

        self.adilo_api = AdiloAPI(public_key, secret_key)
        self.project_id = None

    def test_environment_variables(self):
        public_key = os.getenv("ADILO_PUBLIC_KEY")
        secret_key = os.getenv("ADILO_SECRET_KEY")

        self.assertIsNotNone(public_key)
        self.assertIsNotNone(secret_key)

    def tearDown(self):
        if self.project_id:
            result = self.adilo_api.delete_project_by_id(self.project_id)
            self.assertEqual(result["status"], "success", "delete_project_by_id failed")

    def test_create_project(self):
        project = self.adilo_api.create_project("test")
        self.assertEqual(project["status"], "success", "create_project failed")
        self.project_id = project["payload"]["id"]

    def test_get_project_by_id(self):
        self.test_create_project()

        result = self.adilo_api.get_project_by_id(self.project_id)
        self.assertEqual(
            result["payload"]["title"],
            "test",
            "get_project_by_id failed title does not match",
        )

    def test_list_projects(self):
        results = self.adilo_api.list_projects()
        self.assertEqual(results["status"], "success", "list_projects failed")

    def test_update_project(self):
        self.test_create_project()

        result = self.adilo_api.update_project(self.project_id, "test2")
        self.assertEqual(result["status"], "success", "update_project failed")

        result = self.adilo_api.get_project_by_id(self.project_id)
        self.assertEqual(
            result["payload"]["title"],
            "test2",
            "update_project failed title does not match",
        )

    def test_create_folder(self):
        self.test_create_project()

        result = self.adilo_api.create_folder(self.project_id, "test_folder")
        self.assertEqual(result["status"], "success", "create_folder failed")
        self.assertEqual(
            result["payload"]["name"],
            "test_folder",
            "create_folder failed name does not match",
        )
        self.assertEqual(
            result["payload"]["project"]["id"],
            self.project_id,
            "create_folder failed project id does not match",
        )
        self.folder_id = result["payload"]["id"]

    def test_get_folder_by_id(self):
        self.test_create_folder()

        result = self.adilo_api.get_folder_by_id(self.folder_id)
        self.assertEqual(result["status"], "success", "get_folder_by_id failed")
        self.assertEqual(
            result["payload"]["name"],
            "test_folder",
            "get_folder_by_id failed name does not match",
        )
        self.assertEqual(
            result["payload"]["project"]["id"],
            self.project_id,
            "get_folder_by_id failed project id does not match",
        )

    def test_update_folder(self):
        self.test_create_folder()

        result = self.adilo_api.update_folder(
            self.folder_id, "test_folder2", self.project_id
        )
        self.assertEqual(result["status"], "success", "update_folder failed")

        result = self.adilo_api.get_folder_by_id(self.folder_id)
        self.assertEqual(
            result["payload"]["name"],
            "test_folder2",
            "update_folder failed name does not match",
        )

    def test_delete_folder_by_id(self):
        self.test_create_folder()

        result = self.adilo_api.delete_folder_by_id(self.folder_id)
        self.assertEqual(result["status"], "success", "delete_folder_by_id failed")


if __name__ == "__main__":
    unittest.main()
