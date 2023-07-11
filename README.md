# NASA TechPort API Documentation

The NASA TechPort system provides a RESTful web services API to access technology project data. This API allows you to export TechPort data in JSON format for further processing and analysis.

## API Authentication

All TechPort API calls require an API Token, which is a unique identifier that authenticates your request to the TechPort system. To generate an API Token:

1. Access the TechPort system.
2. Copy the current session's token.
3. Paste the token into your API call.

Please note that each API Token corresponds to an authenticated TechPort session, so you'll need a new token for each access.

## API Endpoints

The TechPort API supports the following GET endpoints:

- `/api`: Retrieves general information about the API.
- `/api/projects`: Retrieves information about all projects.
- `/api/projects/search`: Searches for projects based on specific criteria.
- `/api/projects/{projectId}`: Retrieves information about a specific project.
- `/api/organizations`: Retrieves information about all organizations.
- `/api/organizations/types`: Retrieves information about organization types.
- `/api/organizations/{organizationId}`: Retrieves information about a specific organization.

## HTTP Response Codes

The TechPort API uses conventional HTTP response codes to indicate the success or failure of a request:

- Codes in the 2xx range indicate success.
- Codes in the 4xx range indicate errors related to the data passed in the request.
- Codes in the 5xx range indicate errors within TechPort itself (automatically reported).

For more details on available objects, properties, and RESTful URIs, please refer to the [API documentation](https://techport.nasa.gov/help/articles/api) provided by NASA TechPort.

## Example Script

Here's an example script in Python that demonstrates how to use the TechPort API:

```python
import requests

url = "https://techport.nasa.gov/api/projects/18162"
headers = {
    "Authorization": "<API Token>",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")
