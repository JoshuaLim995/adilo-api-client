import unittest

from tests.test_adilo_api_client import TestAdiloAPI


class ProjectTestCase(TestAdiloAPI):
    def test_create_project(self):
        self.create_project("test")

    def test_get_project_by_id(self):
        project = self.create_project("test")

        result = self.adilo_api.get_project_by_id(project.id)
        self.assertEqual(
            result.title,
            "test",
            "get_project_by_id failed title does not match",
        )

    def test_list_projects(self):
        results = self.adilo_api.list_projects()
        initial_count = results.total

        self.test_create_project()

        new_results = self.adilo_api.list_projects()
        self.assertEqual(
            new_results.total,
            initial_count + 1,
            "list_projects failed",
        )

    def test_search_projects(self):
        # Assuming there are no projects with the title "test"
        self.test_create_project()

        new_results = self.adilo_api.search_projects("test")
        self.assertEqual(
            new_results.total,
            1,
            "search_projects failed",
        )

    def test_update_project(self):
        project = self.create_project("test")

        # expecting project description to be empty
        self.assertEqual(project.description, "", "project description is not empty")

        updated_project = self.adilo_api.update_project(
            project.id, "test2", description="test description"
        )
        self.assertEqual(updated_project.title, "test2", "project title does not match")
        self.assertEqual(
            updated_project.description,
            "test description",
            "project description does not match",
        )

        project_test2 = self.adilo_api.get_project_by_id(project.id)
        self.assertEqual(
            project_test2.title,
            "test2",
            "update_project failed title does not match",
        )


if __name__ == "__main__":
    unittest.main()
