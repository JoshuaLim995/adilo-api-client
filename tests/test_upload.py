import unittest
from adilo_api_client.data_classes import Part

from tests.test_adilo_api_client import TestAdiloAPI


class UploadTestCase(TestAdiloAPI):
    def setUp(self):
        super().setUp()
        self.project = self.create_project("test")

    def test_initiate_file_upload(self):
        upload = self.adilo_api.initiate_file_upload(
            filename="test_file.mp4",
            filesize="1000",
            duration_seconds=300,
            duration_string="00:05:00",
            mime_type="video/mp4",
            project_id=self.project.id,
        )

        self.assertIsNotNone(upload.key, "initiate_file_upload failed key is None")
        self.assertIsNotNone(
            upload.upload_id, "initiate_file_upload failed upload_id is None"
        )

    def test_get_signed_upload_url(self):
        upload = self.adilo_api.initiate_file_upload(
            filename="test_file.mp4",
            filesize="1000",
            duration_seconds=300,
            duration_string="00:05:00",
            mime_type="video/mp4",
            project_id=self.project.id,
        )

        assert (
            upload.key is not None and upload.upload_id is not None
        ), "initiate_file_upload failed key or upload_id is None"

        signed_upload_url = self.adilo_api.get_signed_upload_url(
            key=upload.key, upload_id=upload.upload_id, part_number="1"
        )

        self.assertIsNotNone(
            signed_upload_url.method, "get_signed_upload_url failed method is None"
        )
        self.assertIsNotNone(
            signed_upload_url.url, "get_signed_upload_url failed url is None"
        )


class UploadToFolderTestCase(TestAdiloAPI):
    def setUp(self):
        super().setUp()
        self.project = self.create_project("test")
        self.folder = self.create_folder(self.project.id, "test_folder")

    def test_initiate_file_upload_to_folder(self):
        upload = self.adilo_api.initiate_file_upload(
            filename="test_file.mp4",
            filesize="1000",
            duration_seconds=300,
            duration_string="00:05:00",
            mime_type="video/mp4",
            project_id=self.project.id,
            folder_id=self.folder.id,
        )

        self.assertIsNotNone(upload.key, "initiate_file_upload failed key is None")
        self.assertIsNotNone(
            upload.upload_id, "initiate_file_upload failed upload_id is None"
        )

    def test_get_signed_upload_url_to_folder(self):
        upload = self.adilo_api.initiate_file_upload(
            filename="test_file.mp4",
            filesize="1000",
            duration_seconds=300,
            duration_string="00:05:00",
            mime_type="video/mp4",
            project_id=self.project.id,
            folder_id=self.folder.id,
        )

        assert (
            upload.key is not None and upload.upload_id is not None
        ), "initiate_file_upload failed key or upload_id is None"

        signed_upload_url = self.adilo_api.get_signed_upload_url(
            key=upload.key, upload_id=upload.upload_id, part_number="1"
        )

        self.assertIsNotNone(
            signed_upload_url.method, "get_signed_upload_url failed method is None"
        )
        self.assertIsNotNone(
            signed_upload_url.url, "get_signed_upload_url failed url is None"
        )
