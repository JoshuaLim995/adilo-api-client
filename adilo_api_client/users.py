import requests

from adilo_api_client import endpoint_urls as urls
from adilo_api_client.response_helper import handle_response

# supported permissions
SUPPORTED_PERMISSIONS = [
    "Create Project",
    "Delete Project",
    "Upload Video",
    "Customize Video",
    "Delete Video",
    "Project Analytics",
    "Experimentation",
    "Collaboration",
    "Playlists",
    "Edit Stage",
    "View Snaps",
    "Edit Snaps",
    "Delete Snaps",
    "Create Snaps",
    "Request Snaps (Shared Snaps)",
    "View Analytics",
    "Notification",
    "Global video settings",
    "View Integrations",
    "Add Integrations",
    "Delete Integrations",
    "View Channels",
    "Add Channels",
    "Edit Channels",
    "Delete Channels",
    "View Domains",
    "Add Domains",
    "Edit Domains",
    "Delete Domains",
    "View Brands",
    "Add Brands",
    "Edit Brands",
    "Delete Brands",
    "View Contacts",
    "Export Contacts",
    "Edit Contacts",
    "Delete Contacts",
]


def _validate_permissions(permissions: list[str]):
    # Validate permissions
    for permission in permissions:
        if permission not in SUPPORTED_PERMISSIONS:
            raise ValueError(
                f"Permission '{permission}' is not supported. Supported permissions are: {', '.join(SUPPORTED_PERMISSIONS)}"
            )


def create_user(
    headers: dict[str, str],
    name,
    email,
    password,
    permissions: list[str] = [],
):
    # Validate permissions
    _validate_permissions(permissions)

    # Make a POST request to create a new user
    data = {
        "name": name,
        "email": email,
        "password": password,
        "permissions": permissions,
    }

    response = requests.post(urls.USERS_URL, headers=headers, json=data)

    return handle_response(response)


def list_users(headers: dict[str, str], from_=1, to=50):
    # Make a GET request to list all users
    params = {"From": from_, "To": to}
    response = requests.get(urls.USERS_URL, headers=headers, params=params)

    return handle_response(response)


def get_user_by_id(headers: dict[str, str], user_id):
    # Make a GET request to get a user by ID
    response = requests.get(f"{urls.USERS_URL}/{user_id}", headers=headers)

    return handle_response(response)


def update_user(
    headers: dict[str, str],
    user_id,
    name=None,
    email=None,
    password=None,
    permissions: list[str] | None = None,
):
    # Validate permissions if provided
    if permissions is not None:
        _validate_permissions(permissions)

    # Make a PUT request to update a user
    data = {
        "name": name,
        "email": email,
        "password": password,
        "permissions": permissions,
    }
    data = {k: v for k, v in data.items() if v is not None}  # Remove None values

    response = requests.put(f"{urls.USERS_URL}/{user_id}", headers=headers, json=data)

    return handle_response(response)


def delete_user(headers: dict[str, str], user_id: str):
    # Make a DELETE request to delete a user by ID
    response = requests.delete(f"{urls.USERS_URL}/{user_id}", headers=headers)

    return handle_response(response)
