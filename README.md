# unmappedremover

## Description

A Python script to delete unmapped folders in the media directory using the Sonarr API.

## Features

- Fetches the media directory path and unmapped folders from the Sonarr API.
- Performs an actual delete of unmapped folders and associated files (optional).
- Provides a dry run (preview) of the delete operation without actually deleting anything.
- Uses the `requests` library to interact with the Sonarr API.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## How to Use

1. Clone this repository to your local machine.
2. Install the required `requests` library by running: `pip install requests`.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the script with the following command:

```bash
python main.py http://sonarr_url your_api_key root_folder_id1 root_folder_id2 --delete
```

Replace `http://sonarr_url`with the actual Sonarr URL, `your_api_key` with the correct API key, and `root_folder_id1`, `root_folder_id2`, etc., with the root folder IDs you want to process.

`Caution`: The --delete flag will perform the actual delete operation. Ensure you have backups of your data before using this option.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**Use this script at your own risk.** Deleting folders and files can result in data loss. Make sure you have backups of your data before running the script.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

---
