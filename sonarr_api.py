import requests

def get_unmapped_folders(sonarr_url, api_key, root_folder_id):
    # Function to fetch the list of unmapped folders from Sonarr
    unmapped_folders = []

    headers = {
        "X-Api-Key": api_key,
    }

    try:
        # Fetch the media directory path from the Sonarr API
        media_directory = get_media_directory(sonarr_url, api_key, root_folder_id)

        # Fetch unmapped folders
        url = f"{sonarr_url.rstrip('/')}/api/v3/rootFolder/{root_folder_id}?timeout=false"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        unmapped_folders = [folder["name"] for folder in data["unmappedFolders"]]

    except requests.exceptions.RequestException as e:
        print("Error connecting to Sonarr:", e)

    return media_directory, unmapped_folders

def get_media_directory(sonarr_url, api_key, root_folder_id):
    # Function to fetch the media directory path from Sonarr
    media_directory = ""

    headers = {
        "X-Api-Key": api_key,
    }

    try:
        url = f"{sonarr_url.rstrip('/')}/api/v3/rootFolder/{root_folder_id}?timeout=false"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        media_directory = data.get("path", "")

    except requests.exceptions.RequestException as e:
        print("Error connecting to Sonarr:", e)

    return media_directory
