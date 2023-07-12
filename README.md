# NASA TechPort API

The NASA TechPort system provides a RESTful web services API to access technology project data. This API allows you to export TechPort data in JSON format for further processing and analysis.

## API Authentication

All TechPort API calls require an API Token, which is a unique identifier that authenticates your request to the TechPort system. To generate an API Token:

1. Access the [TechPort system](https://techport.nasa.gov/help/articles/api).
2. Copy the API Token.
3. Paste the token into your API call.

Please note that because the token reflects an active session, you’ll need a new token each time you access the TechPort API.

## API Endpoints

The TechPort API supports the following GET endpoints:

- `/api`: Returns the swagger specification for the API.
- `/api/projects`: Returns a list of available technology project IDs.
- `/api/projects/search`: Returns a list of projects matching the search term.
- `/api/projects/{projectId}`: Returns information about a specific technology project.
- `/api/organizations`: Returns a list of organizations that match a given name.
- `/api/organizations/types`: Returns a list of available organization types, including set-aside and MSI types.
- `/api/organizations/{organizationId}`: Get an organization and its information.

## Parameters

### `/api/projects`

Retrieves information about all projects.

- `updatedSince`: (string, $date) ISO 8601 full-date format (YYYY-MM-DD). Filters the list of available ID values by their lastUpdated parameter. Example: `"2023-07-10"`

### `/api/projects/search`

Searches for projects based on specific criteria.

- `projectId`: (integer, $int64) The specific ID of the project requested. Example: `13075`
- `searchQuery`: (string) The term on which to search. It checks all project fields for this term. Example: `"human/robotic exploration and commercial spaceflight missions"`
- `missionDirectorate`: (string) The mission directorate acronym of the projects. Used to filter. Example: `"STMD"`
- `program`: (string) The program acronym of the projects. Used to filter. Example: `"TDM"`
- `titleSearch`: (string) The term on which to search. It checks only project titles for this term. Example: `"solar electric propulsion"`

### `/api/organizations`

Retrieves information about all organizations.

- `name`: (string) Organization Name to filter on. Example: `"NASA"`

## HTTP Response Codes

The TechPort API uses conventional HTTP response codes to indicate the success or failure of a request:

- Codes in the 2xx range indicate success.
- Codes in the 4xx range indicate errors related to the data passed in the request.
- Codes in the 5xx range indicate errors within TechPort itself (automatically reported to the TechPort team).

For more details on the endpoints, schemas, and general API information, please refer to the [API documentation](https://techport.nasa.gov/help/articles/api) provided by TechPort.

## Example Script

Here's an example script in Python that demonstrates how to use the TechPort API:

```python
import requests

url = "https://techport.nasa.gov/api/projects"
urlWithQuery = "https://techport.nasa.gov/api/projects/search?titleSearch=solar%20electric%20propulsion"
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
