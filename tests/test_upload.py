import os
from pathlib import Path

import pytest
import requests
from dotenv import load_dotenv

from adilo_api_client.data_classes import Part
from tests.test_adilo_api_client import TestAdiloAPI
from tests.utils import get_duration_string

load_dotenv()  # take environment variables from .env.


class UploadTestCase(TestAdiloAPI):
    def setUp(self):
        super().setUp()
        self.project = self.create_project("test")

    def tearDown(self):
        if self._testMethodName == "test_upload_sample_video":
            return
        super().tearDown()

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

    @pytest.mark.skipif(os.getenv("DEV_MODE") is None, reason="not in dev mode")
    def test_upload_sample_video(self):
        from tinytag import TinyTag

        # get parent folder current directory
        parent_folder = Path(__file__).parent.parent.absolute()
        video_path = parent_folder.joinpath("sample/5Mb_video.mp4")

        video = TinyTag.get(str(video_path.absolute()))

        filesize = video.filesize
        duration = int(video.duration or 0)
        duration_string = get_duration_string(duration)

        upload = self.adilo_api.initiate_file_upload(
            filename="5Mb_video.mp4",
            filesize=filesize,
            duration_seconds=duration,
            duration_string=duration_string,
            mime_type="video/mp4",
            project_id=self.project.id,
        )
        print(upload)

        signed_upload_url = self.adilo_api.get_signed_upload_url(
            key=upload.key, upload_id=upload.upload_id, part_number="1"
        )
        print(signed_upload_url)

        with open(video_path, "rb") as f:
            response = requests.put(signed_upload_url.url, data=f)

        self.assertEqual(
            response.status_code, 200, "upload_file failed status_code is not 200"
        )

        e_tag = response.headers["ETag"]

        completed = self.adilo_api.complete_file_upload(
            key=upload.key,
            upload_id=upload.upload_id,
            parts=[Part(etag=e_tag, part_number=1)],
        )
        print(completed)


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
