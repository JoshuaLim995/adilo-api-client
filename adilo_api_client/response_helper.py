from requests import Response


def handle_response(response: Response):
    status_code = response.status_code
    if status_code == 200:
        return response.json()
    elif status_code == 403:
        return "Error 403: Forbidden - The action is not allowed"
    elif status_code == 404:
        return "Error 404: Not Found - The project or parent folder not found"
    elif status_code == 422:
        return "Error 422: Unprocessed Entity - The input data was invalid"
    else:
        return f"Error: {response.status_code}, {response.text}"
