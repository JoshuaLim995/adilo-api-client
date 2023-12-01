import requests

from adilo_api_client import endpoint_urls as urls
from adilo_api_client.response_helper import handle_response


def create_project(
    headers, title, description="", locked=False, drm=False, private=False, password=""
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

    return handle_response(response)


def list_projects(headers, from_=1, to=50):
    # Define query parameters
    params = {
        "From": from_,
        "To": to,
    }

    # Make a GET request to list all projects
    response = requests.get(urls.PROJECTS_URL, params=params, headers=headers)

    return handle_response(response)


def update_project(
    headers,
    project_id,
    title,
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

    # Make a PUT request to update an existing project
    response = requests.put(
        f"{urls.PROJECTS_URL}/{project_id}", json=project_data, headers=headers
    )

    return handle_response(response)


def get_project_by_id(headers, project_id):
    # Make a GET request to fetch a project by its ID
    response = requests.get(f"{urls.PROJECTS_URL}/{project_id}", headers=headers)

    return handle_response(response)


def delete_project_by_id(headers, project_id):
    # Make a DELETE request to delete a project by its ID
    response = requests.delete(f"{urls.PROJECTS_URL}/{project_id}", headers=headers)

    return handle_response(response)


def search_project(headers, search_string, from_result=1, to_result=50):
    # Make a GET request to search for projects
    response = requests.get(
        f"{urls.PROJECTS_URL}/search/{search_string}",
        params={"From": from_result, "To": to_result},
        headers=headers,
    )

    return handle_response(response)


def get_folders_by_project_id(headers, project_id, from_result=1, to_result=50):
    # Make a GET request to fetch project folders by project ID
    response = requests.get(
        f"{urls.PROJECTS_URL}/{project_id}/folders",
        params={"From": from_result, "To": to_result},
        headers=headers,
    )

    return handle_response(response)


def get_files_by_project_id(headers, project_id, from_result=1, to_result=50):
    # Make a GET request to fetch project files by project ID
    response = requests.get(
        f"{urls.PROJECTS_URL}/{project_id}/files",
        params={"From": from_result, "To": to_result},
        headers=headers,
    )

    return handle_response(response)
