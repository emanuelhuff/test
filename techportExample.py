import requests

url = "https://techport.nasa.gov/api/projects"
urlWithQuery = "https://techport.nasa.gov/api/projects/search?titleSearch=solar%20electric%20propulsion"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJUZWNoUG9ydCIsImV4cCI6MTY4OTI1MDM2MywibmJmIjoxNjg5MTYzOTYzLCJTRVNTSU9OX0lEIjoidHQwMlNvdmo0NFhjZzdiOGxoRTJkUHhqNnNBS2tDTm1QZ0pvIiwiRklOR0VSUFJJTlRfSEFTSCI6IjMwRjhBNEVERUE5QzgwQ0YxRTRGREVEMkE5MzYxQTgyOTQyQjM1RjA0NjI5Nzg5MzQ5RDM4QkFBMUM5RTM5NjgifQ.PQKwLdnzMx-p_JuFCOamBfyYutJ2rxatDtls_cDTxOI",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")