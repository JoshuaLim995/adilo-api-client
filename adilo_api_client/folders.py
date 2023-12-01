import requests

from adilo_api_client import endpoint_urls as urls
from adilo_api_client.data_classes import Folder, FolderList
from adilo_api_client.response_helper import handle_response


def create_folder(
    headers: dict[str, str],
    project_id: str,
    name: str,
    parent_id: str | None = None,
):
    # Make a POST request to create a new folder in a project
    data = {"name": name, "project_id": project_id}
    if parent_id:
        data["parent_id"] = parent_id

    response = requests.post(f"{urls.FOLDERS_URL}", headers=headers, json=data)

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return Folder(**payload)


def update_folder(
    headers: dict[str, str],
    folder_id: str,
    project_id: str,
    name: str | None = None,
    parent_id: str | None = None,
):
    # Make a PUT request to update a folder in a project
    data = {"project_id": project_id}
    if name:
        data["name"] = name
    if parent_id:
        data["parent_id"] = parent_id

    response = requests.put(
        f"{urls.FOLDERS_URL}/{folder_id}", headers=headers, json=data
    )

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return Folder(**payload)


def get_folder_by_id(headers: dict[str, str], folder_id: str):
    # Make a GET request to fetch a folder by its ID
    response = requests.get(f"{urls.FOLDERS_URL}/{folder_id}", headers=headers)

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return Folder(**payload)


def delete_folder_by_id(headers: dict[str, str], folder_id: str):
    # Make a DELETE request to delete a folder by its ID
    response = requests.delete(f"{urls.FOLDERS_URL}/{folder_id}", headers=headers)

    handle_response(response)
    return True


def get_folders_by_project_id(
    headers: dict[str, str],
    project_id: str,
    from_result=1,
    to_result=50,
):
    # Make a GET request to fetch project folders by project ID
    response = requests.get(
        f"{urls.PROJECTS_URL}/{project_id}/folders",
        params={"From": from_result, "To": to_result},
        headers=headers,
    )

    response_data = handle_response(response)
    payloads = response_data.get("payload")
    meta = response_data.get("meta")

    folders = [Folder(**folder) for folder in payloads]
    return FolderList(
        folders=folders,
        **{
            "total": meta.get("total"),
            "from_": meta.get("from"),
            "to": meta.get("to"),
        },
    )
