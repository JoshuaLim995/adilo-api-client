import dataclasses

import requests

from . import endpoint_urls as urls
from .response_helper import handle_response


@dataclasses.dataclass
class Part:
    part_number: int
    etag: str

    def to_dict(self):
        return dataclasses.asdict(self)


def initiate_file_upload(
    headers,
    filename,
    filesize,
    duration_seconds,
    duration_string,
    mime_type,
    project_id,
    drm_protection,
):
    # Make a POST request to initiate a file upload
    data = {
        "filename": filename,
        "filesize": filesize,
        "duration_seconds": duration_seconds,
        "duration_string": duration_string,
        "mime_type": mime_type,
        "project_id": project_id,
        "drm_protection": drm_protection,
    }

    response = requests.post(
        f"{urls.FILES_UPLOAD_URL}/start", headers=headers, json=data
    )

    return handle_response(response)


def get_signed_upload_url(headers, upload_id, part_number, key):
    # Make a GET request to get a signed upload URL for each part of your video
    params = {"key": key}

    response = requests.get(
        f"{urls.FILES_UPLOAD_URL}/get-signed-url/{upload_id}/{part_number}",
        headers=headers,
        params=params,
    )

    return handle_response(response)


def complete_file_upload(headers, key, upload_id, parts: list[Part]):
    # Make a POST request to complete the multipart upload
    data = {"key": key, "uploadId": upload_id, "parts": parts}

    response = requests.post(
        f"{urls.FILES_UPLOAD_URL}/complete", headers=headers, json=data
    )

    return handle_response(response)


def get_signed_upload_url_for_update(
    headers,
    file_id,
    filename,
    filesize,
    duration_seconds,
    duration_string,
    mime_type,
    drm_protection,
    clear_statistics=False,
):
    # Make a GET request to get a signed upload URL for file upload
    data = {
        "filename": filename,
        "filesize": filesize,
        "duration_seconds": duration_seconds,
        "duration_string": duration_string,
        "mime_type": mime_type,
        "drm_protection": drm_protection,
        "clear_statistics": clear_statistics,
    }

    response = requests.get(
        f"{urls.FILES_URL}/{file_id}/update/get-signed-url", headers=headers, json=data
    )

    return handle_response(response)


def complete_file_update(headers, file_id):
    # Make a PUT request to complete the file update
    response = requests.put(
        f"{urls.FILES_URL}/{file_id}/update/complete", headers=headers
    )

    return handle_response(response)


def get_file_by_id(headers, file_id):
    # Make a GET request to get a project file by its ID
    response = requests.get(f"{urls.FILES_URL}/{file_id}", headers=headers)

    return handle_response(response)


def delete_file_by_id(headers, file_id):
    # Make a DELETE request to delete a project file by its ID
    response = requests.delete(f"{urls.FILES_URL}/{file_id}", headers=headers)

    return handle_response(response)


def get_file_meta_data(headers, file_id):
    # Make a GET request to get a project file's metadata by its ID
    response = requests.get(f"{urls.FILES_URL}/{file_id}/meta", headers=headers)

    return handle_response(response)


def download_file(
    headers,
    file_id,
):
    # Make a GET request to download a project file by its ID
    response = requests.get(f"{urls.FILES_URL}/{file_id}/download", headers=headers)

    return handle_response(response)


def upload_subtitle(headers, file_id, file, language):
    # Make a POST request to upload a subtitle for a project file by its ID
    data = {"file_id": file_id, "file": file, "language": language}

    response = requests.post(
        "{urls.FILES_URL}/subtitle/upload", headers=headers, files=data
    )

    return handle_response(response)


def generate_subtitle(headers, file_id, language):
    # Make a POST request to generate a subtitle for a project file by its ID
    data = {"file_id": file_id, "language": language}

    response = requests.post(
        "{urls.FILES_URL}/subtitle/generate", headers=headers, json=data
    )

    return handle_response(response)


def download_subtitle(headers, file_id):
    # Make a GET request to download a subtitle for a project file by its ID
    response = requests.get(
        f"{urls.FILES_URL}/{file_id}/subtitle/download", headers=headers
    )

    return handle_response(response)


def generate_translation(headers, file_id, language):
    # Make a POST request to generate a translation for a project file by its ID
    data = {"file_id": file_id, "language": language}

    response = requests.post(
        "https://adilo-api.bigcommand.com/v1/files/translation/generate",
        headers=headers,
        json=data,
    )

    return handle_response(response)


def download_translation(headers, file_id, language):
    # Make a GET request to download a translation for a project file by its ID
    params = {"language": language}
    response = requests.get(
        f"https://adilo-api.bigcommand.com/v1/files/{file_id}/translation/download",
        headers=headers,
        params=params,
    )

    return handle_response(response)
