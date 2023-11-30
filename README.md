# Adilo API Client

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

This is a Python client for interacting with the Adilo API.

## Installation

```bash
pip install adilo-api-client
```

## Usage

```python
from adilo_api.adilo_api import AdiloAPI

# Replace 'your_public_key' and 'your_secret_key' with your actual API keys
api = AdiloAPI(public_key='your_public_key', secret_key='your_secret_key')

# Create a new project
project_title = 'Project Title'
result_create = api.create_project(title=project_title, description="Project Description", locked=False, drm=False, private=False, password="")
print(result_create)

# List all projects
result_list = api.list_projects()
print(result_list)
```

Replace `your_public_key` and `your_secret_key` with your actual API keys. Customize the project_title and other parameters according to your needs.

## API Documentation

For more details on the Adilo API, refer to the [official documentation](https://developers.adilo.com/).

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## Testing

1. Copy and rename `.env.sample` to `.env`
2. Copy the API Key and API Secret from [Adilo API Setting](https://adilo.bigcommand.com/settings/api) to `.env`

You can run your tests using:

```bash
python -m unittest tests/test_adilo_api.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
