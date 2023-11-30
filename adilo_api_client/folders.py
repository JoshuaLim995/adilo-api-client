import requests

from . import endpoint_urls as urls
from .response_helper import handle_response


def create_folder(headers, project_id: str, name, parent_id=None):
    # Make a POST request to create a new folder in a project
    data = {"name": name, "project_id": project_id}
    if parent_id:
        data["parent_id"] = parent_id

    response = requests.post(f"{urls.FOLDERS_URL}", headers=headers, json=data)

    return handle_response(response)


def update_folder(headers, folder_id: str, name: str, project_id: str, parent_id=None):
    # Make a PUT request to update a folder in a project
    data = {"name": name, "project_id": project_id}
    if parent_id:
        data["parent_id"] = parent_id

    response = requests.put(
        f"{urls.FOLDERS_URL}/{folder_id}", headers=headers, json=data
    )

    return handle_response(response)


def get_folder_by_id(headers, folder_id):
    # Make a GET request to fetch a folder by its ID
    response = requests.get(f"{urls.FOLDERS_URL}/{folder_id}", headers=headers)

    return handle_response(response)


def delete_folder_by_id(headers, folder_id):
    # Make a DELETE request to delete a folder by its ID
    response = requests.delete(f"{urls.FOLDERS_URL}/{folder_id}", headers=headers)

    return handle_response(response)
