from requests import Response

from adilo_api_client import exceptions


def handle_response(response: Response):
    status_code = response.status_code
    if status_code == 200:
        return response.json()
    elif status_code == 403:
        raise exceptions.ForbiddenException(
            "Error 403: Forbidden - The action is not allowed"
        )
    elif status_code == 404:
        raise exceptions.NotFoundException(
            "Error 404: Not Found - The project or parent folder not found"
        )
    elif status_code == 422:
        raise exceptions.BadRequestException(
            "Error 422: Unprocessed Entity - The input data was invalid",
            response.json(),
        )
    else:
        raise exceptions.UnknownException(
            f"Error: {response.status_code}, {response.text}"
        )
