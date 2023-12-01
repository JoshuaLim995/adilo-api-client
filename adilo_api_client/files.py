import dataclasses
from typing import Any

import requests

from adilo_api_client import endpoint_urls as urls
from adilo_api_client.data_classes import InitiateUpload, Part, SignedUpload
from adilo_api_client.response_helper import handle_response


def initiate_file_upload(
    headers: dict[str, str],
    filename: str,
    filesize: str,
    duration_seconds: int,
    duration_string: str,
    mime_type: str,
    project_id: str,
    folder_id: str | None = None,
    drm_protection: bool = False,
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
    if folder_id:
        data["folder_id"] = folder_id

    response = requests.post(
        f"{urls.FILES_UPLOAD_URL}/start", headers=headers, json=data
    )

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return InitiateUpload.from_dict(payload)


def get_signed_upload_url(
    headers: dict[str, str],
    key: str,
    upload_id: str,
    part_number: str,
):
    # Make a GET request to get a signed upload URL for each part of your video
    params = {"key": key}

    response = requests.get(
        f"{urls.FILES_UPLOAD_URL}/get-signed-url/{upload_id}/{part_number}",
        headers=headers,
        params=params,
    )

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return SignedUpload(**payload)


def complete_file_upload(
    headers: dict[str, str],
    key: str,
    upload_id,
    parts: list[Part],
):
    # Make a POST request to complete the multipart upload
    data = {
        "key": key,
        "uploadId": upload_id,
        "parts": [part.to_dict() for part in parts],
    }

    response = requests.post(
        f"{urls.FILES_UPLOAD_URL}/complete", headers=headers, json=data
    )

    return handle_response(response)


def get_signed_upload_url_for_update(
    headers: dict[str, str],
    file_id: str,
    filename: str,
    filesize: str,
    duration_seconds: int,
    duration_string: str,
    mime_type: str,
    drm_protection: bool,
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


def complete_file_update(headers: dict[str, str], file_id: str):
    # Make a PUT request to complete the file update
    response = requests.put(
        f"{urls.FILES_URL}/{file_id}/update/complete", headers=headers
    )

    return handle_response(response)


def get_file_by_id(headers: dict[str, str], file_id: str):
    # Make a GET request to get a project file by its ID
    response = requests.get(f"{urls.FILES_URL}/{file_id}", headers=headers)

    return handle_response(response)


def delete_file_by_id(headers: dict[str, str], file_id: str):
    # Make a DELETE request to delete a project file by its ID
    response = requests.delete(f"{urls.FILES_URL}/{file_id}", headers=headers)

    return handle_response(response)


def get_file_meta_data(headers: dict[str, str], file_id: str):
    # Make a GET request to get a project file's metadata by its ID
    response = requests.get(f"{urls.FILES_URL}/{file_id}/meta", headers=headers)

    return handle_response(response)


def download_file(headers: dict[str, str], file_id: str):
    # Make a GET request to download a project file by its ID
    response = requests.get(f"{urls.FILES_URL}/{file_id}/download", headers=headers)

    return handle_response(response)


def upload_subtitle(headers: dict[str, str], file_id: str, file: Any, language: str):
    # Make a POST request to upload a subtitle for a project file by its ID
    data = {"file_id": file_id, "file": file, "language": language}

    response = requests.post(
        "{urls.FILES_URL}/subtitle/upload", headers=headers, files=data
    )

    return handle_response(response)


def generate_subtitle(headers: dict[str, str], file_id: str, language: str):
    # Make a POST request to generate a subtitle for a project file by its ID
    data = {"file_id": file_id, "language": language}

    response = requests.post(
        "{urls.FILES_URL}/subtitle/generate", headers=headers, json=data
    )

    return handle_response(response)


def download_subtitle(headers: dict[str, str], file_id: str):
    # Make a GET request to download a subtitle for a project file by its ID
    response = requests.get(
        f"{urls.FILES_URL}/{file_id}/subtitle/download", headers=headers
    )

    return handle_response(response)


def generate_translation(headers: dict[str, str], file_id: str, language: str):
    # Make a POST request to generate a translation for a project file by its ID
    data = {"file_id": file_id, "language": language}

    response = requests.post(
        "https://adilo-api.bigcommand.com/v1/files/translation/generate",
        headers=headers,
        json=data,
    )

    return handle_response(response)


def download_translation(headers: dict[str, str], file_id: str, language: str):
    # Make a GET request to download a translation for a project file by its ID
    params = {"language": language}
    response = requests.get(
        f"https://adilo-api.bigcommand.com/v1/files/{file_id}/translation/download",
        headers=headers,
        params=params,
    )

    return handle_response(response)


def get_files_by_project_id(
    headers: dict[str, str], project_id: str, from_result=1, to_result=50
):
    # Make a GET request to fetch project files by project ID
    response = requests.get(
        f"{urls.PROJECTS_URL}/{project_id}/files",
        params={"From": from_result, "To": to_result},
        headers=headers,
    )

    return handle_response(response)
