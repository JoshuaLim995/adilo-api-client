import requests

from adilo_api_client import endpoint_urls as urls
from adilo_api_client.data_classes import Project, ProjectList
from adilo_api_client.response_helper import handle_response


def create_project(
    headers: dict[str, str],
    title: str,
    description="",
    locked=False,
    drm=False,
    private=False,
    password="",
):
    # Define the project data
    project_data = {
        "title": title,
        "description": description,
        "locked": locked,
        "drm": drm,
        "private": private,
        "password": password,
    }

    # Make a POST request to create a new project
    response = requests.post(urls.PROJECTS_URL, json=project_data, headers=headers)

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return Project(**payload)


def list_projects(headers: dict[str, str], from_=1, to=50) -> ProjectList:
    # Define query parameters
    params = {
        "From": from_,
        "To": to,
    }

    # Make a GET request to list all projects
    response = requests.get(urls.PROJECTS_URL, params=params, headers=headers)

    response_data = handle_response(response)
    payloads = response_data.get("payload")
    meta = response_data.get("meta")

    projects = [Project(**project) for project in payloads]
    return ProjectList(
        projects=projects,
        **{
            "total": meta.get("total"),
            "from_": meta.get("from"),
            "to": meta.get("to"),
        },
    )


def update_project(
    headers: dict[str, str],
    project_id: str,
    title: str | None = None,
    description: str | None = None,
    locked=False,
    drm=False,
    private=False,
    password="",
):
    # Define the project data
    project_data = {}
    if title:
        project_data["title"] = title
    if description:
        project_data["description"] = description
    if locked:
        project_data["locked"] = locked
    if drm:
        project_data["drm"] = drm
    if private:
        project_data["private"] = private
    if password:
        project_data["password"] = password

    # Make a PUT request to update an existing project
    response = requests.put(
        f"{urls.PROJECTS_URL}/{project_id}", json=project_data, headers=headers
    )

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return Project(**payload)


def get_project_by_id(headers: dict[str, str], project_id: str):
    # Make a GET request to fetch a project by its ID
    response = requests.get(f"{urls.PROJECTS_URL}/{project_id}", headers=headers)

    response_data = handle_response(response)
    payload = response_data.get("payload")
    return Project(**payload)


def delete_project_by_id(headers: dict[str, str], project_id: str):
    # Make a DELETE request to delete a project by its ID
    response = requests.delete(f"{urls.PROJECTS_URL}/{project_id}", headers=headers)

    handle_response(response)
    return True


def search_projects(
    headers: dict[str, str],
    search_string: str,
    from_result=1,
    to_result=50,
) -> ProjectList:
    # Make a GET request to search for projects
    response = requests.get(
        f"{urls.PROJECTS_URL}/search/{search_string}",
        params={"From": from_result, "To": to_result},
        headers=headers,
    )

    response_data = handle_response(response)
    payloads = response_data.get("payload")
    meta = response_data.get("meta")

    projects = [Project(**project) for project in payloads]
    return ProjectList(
        projects=projects,
        **{
            "total": meta.get("total"),
            "from_": meta.get("from"),
            "to": meta.get("to"),
        },
    )
