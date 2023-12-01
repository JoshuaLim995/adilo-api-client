import unittest

from tests.test_adilo_api_client import TestAdiloAPI


class FolderTestCase(TestAdiloAPI):
    def setUp(self):
        super().setUp()
        self.project = self.create_project("test")

    def test_create_folder(self):
        folder = self.create_folder(self.project.id, "test_folder")

        self.assertEqual(
            folder.name,
            "test_folder",
            "create_folder failed name does not match",
        )

        self.assertEqual(
            folder.project_id,
            self.project.id,
            "create_folder failed project id does not match",
        )

    def test_create_subfolder(self):
        parent_folder = self.create_folder(self.project.id, "test_parent_folder")
        sub_folder = self.create_folder(
            self.project.id, "test_sub_folder", parent_folder.id
        )

        self.assertEqual(
            sub_folder.name,
            "test_sub_folder",
            "create_folder test_sub_folder name does not match",
        )

        self.assertEqual(
            sub_folder.project_id,
            self.project.id,
            "create_folder failed project id does not match",
        )

        self.assertEqual(
            sub_folder.parent_folder_id,
            parent_folder.id,
            "create_folder failed parent_folder id does not match",
        )

    def test_get_folder_by_id(self):
        folder = self.create_folder(self.project.id, "test_folder")

        result = self.adilo_api.get_folder_by_id(folder.id)

        self.assertEqual(
            result.name,
            "test_folder",
            "get_folder_by_id failed name does not match",
        )
        self.assertEqual(
            result.project_id,
            self.project.id,
            "get_folder_by_id failed project id does not match",
        )

    def test_update_folder(self):
        folder = self.create_folder(self.project.id, "test_folder")

        updated_folder = self.adilo_api.update_folder(
            folder.id,
            self.project.id,
            "test_folder2",
        )

        self.assertEqual(
            updated_folder.name,
            "test_folder2",
            "update_folder failed name does not match",
        )

        result = self.adilo_api.get_folder_by_id(folder.id)
        self.assertEqual(
            result.name,
            "test_folder2",
            "update_folder failed name does not match",
        )

    def test_delete_folder_by_id(self):
        folder = self.create_folder(self.project.id, "test_folder")

        result = self.adilo_api.delete_folder_by_id(folder.id)

        self.assertTrue(result, "delete_folder_by_id failed")


if __name__ == "__main__":
    unittest.main()
