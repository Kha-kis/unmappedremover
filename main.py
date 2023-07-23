import argparse
import sonarr_api
import media_operations

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Delete unmapped folders in the media directory.")
    parser.add_argument("sonarr_url", help="The Sonarr API URL.")
    parser.add_argument("api_key", help="Your Sonarr API key.")
    parser.add_argument("root_folder_ids", nargs="+", help="List of root folder IDs.")
    parser.add_argument("--delete", action="store_true", help="Perform the actual delete instead of dry run.")
    args = parser.parse_args()

    # Get the media directory path and the list of unmapped folders for each root folder
    for root_folder_id in args.root_folder_ids:
        media_directory, unmapped_folders = sonarr_api.get_unmapped_folders(args.sonarr_url, args.api_key, root_folder_id)

        # Perform a dry run or actual delete based on the command-line argument
        if args.delete:
            media_operations.delete_unmapped_folders(media_directory, unmapped_folders)
        else:
            media_operations.dry_run_remove_unmapped_folders(media_directory, unmapped_folders)

if __name__ == "__main__":
    main()
