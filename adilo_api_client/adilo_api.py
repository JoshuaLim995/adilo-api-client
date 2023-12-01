from adilo_api_client import files, folders, projects, users
from adilo_api_client.data_classes import Part


class AdiloAPI:
    def __init__(self, public_key: str, secret_key: str):
        self.headers: dict[str, str] = {
            "X-Public-Key": public_key,
            "X-Secret-Key": secret_key,
            "Content-Type": "application/json",
        }

    def create_project(
        self,
        title: str,
        description: str = "",
        locked: bool = False,
        drm: bool = False,
        private: bool = False,
        password: str = "",
    ):
        return projects.create_project(
            self.headers, title, description, locked, drm, private, password
        )

    def list_projects(self, from_: int = 1, to: int = 50):
        return projects.list_projects(self.headers, from_, to)

    def search_projects(self, query: str, from_: int = 1, to: int = 50):
        return projects.search_projects(self.headers, query, from_, to)

    def update_project(
        self,
        project_id: str,
        title: str,
        description: str = "",
        locked: bool = False,
        drm: bool = False,
        private: bool = False,
        password: str = "",
    ):
        return projects.update_project(
            self.headers, project_id, title, description, locked, drm, private, password
        )

    def get_project_by_id(self, project_id: str):
        return projects.get_project_by_id(self.headers, project_id)

    def delete_project_by_id(self, project_id: str):
        return projects.delete_project_by_id(self.headers, project_id)

    def create_folder(
        self,
        project_id: str,
        name: str,
        parent_folder_id: str | None = None,
    ):
        return folders.create_folder(self.headers, project_id, name, parent_folder_id)

    def update_folder(
        self,
        folder_id: str,
        project_id: str,
        name: str | None = None,
        parent_folder_id=None,
    ):
        return folders.update_folder(
            self.headers, folder_id, project_id, name, parent_folder_id
        )

    def get_folder_by_id(self, folder_id: str):
        return folders.get_folder_by_id(self.headers, folder_id)

    def delete_folder_by_id(self, folder_id: str):
        return folders.delete_folder_by_id(self.headers, folder_id)

    def initiate_file_upload(
        self,
        filename: str,
        filesize: str,
        duration_seconds: int,
        duration_string: str,
        mime_type: str,
        project_id: str,
        folder_id: str | None = None,
        drm_protection: bool = False,
    ):
        return files.initiate_file_upload(
            self.headers,
            filename,
            filesize,
            duration_seconds,
            duration_string,
            mime_type,
            project_id,
            folder_id,
            drm_protection,
        )

    def get_signed_upload_url(self, key: str, upload_id: str, part_number: str):
        return files.get_signed_upload_url(self.headers, key, upload_id, part_number)

    def complete_file_upload(self, key: str, upload_id: str, parts: list[Part]):
        return files.complete_file_upload(self.headers, key, upload_id, parts)

    def get_signed_upload_url_for_update(
        self,
        file_id: str,
        filename: str,
        filesize: str,
        duration_seconds: int,
        duration_string: str,
        mime_type: str,
        drm_protection: bool,
        clear_statistics=False,
    ):
        return files.get_signed_upload_url_for_update(
            self.headers,
            file_id,
            filename,
            filesize,
            duration_seconds,
            duration_string,
            mime_type,
            drm_protection,
            clear_statistics,
        )

    def complete_file_update(self, file_id: str):
        return files.complete_file_update(self.headers, file_id)

    def get_file_by_id(self, file_id: str):
        return files.get_file_by_id(self.headers, file_id)

    def delete_file_by_id(self, file_id: str):
        return files.delete_file_by_id(self.headers, file_id)

    def get_file_meta_data(self, file_id: str):
        return files.get_file_meta_data(self.headers, file_id)

    def get_file_download_url(self, file_id: str):
        return files.download_file(self.headers, file_id)

    def upload_subtitle(self, file_id: str, file, language: str):
        return files.upload_subtitle(self.headers, file_id, file, language)

    def get_subtitle_download_url(self, file_id: str):
        return files.download_subtitle(self.headers, file_id)

    def generate_translation(self, file_id: str, language: str):
        return files.generate_translation(self.headers, file_id, language)

    def get_translation_download_url(self, file_id: str, language: str):
        return files.download_translation(self.headers, file_id, language)

    def create_user(
        self,
        name: str,
        email: str,
        password: str,
        permissions: list[str],
    ):
        return users.create_user(self.headers, name, email, password, permissions)

    def list_users(self, from_=1, to=50):
        return users.list_users(self.headers, from_, to)

    def get_user_by_id(self, user_id: str):
        return users.get_user_by_id(self.headers, user_id)

    def update_user(
        self,
        user_id: str,
        name: str | None = None,
        email: str | None = None,
        password: str | None = None,
        permissions: list[str] | None = None,
    ):
        return users.update_user(
            self.headers, user_id, name, email, password, permissions
        )

    def delete_user(self, user_id: str):
        return users.delete_user(self.headers, user_id)
