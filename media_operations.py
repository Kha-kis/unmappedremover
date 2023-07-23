from pathlib import Path
import shutil

def delete_unmapped_folders(media_directory, unmapped_folders):
    media_directory_path = Path(media_directory)

    for folder in unmapped_folders:
        folder_path = media_directory_path / folder
        if folder_path.exists():
            try:
                shutil.rmtree(folder_path)
                print(f"Deleted folder and its contents: {folder_path}")
            except OSError as e:
                print(f"Error deleting folder: {folder_path} - {e}")
        else:
            print(f"Folder not found: {folder_path}")

    for folder in unmapped_folders:
        folder_path = media_directory_path / folder
        for sub_item in folder_path.glob("**/*"):
            if sub_item.is_file():
                try:
                    sub_item.unlink()
                    print(f"Deleted file: {sub_item}")
                except OSError as e:
                    print(f"Error deleting file: {sub_item} - {e}")

def dry_run_remove_unmapped_folders(media_directory, unmapped_folders):
    media_directory_path = Path(media_directory)

    for folder in unmapped_folders:
        folder_path = media_directory_path / folder
        if folder_path.exists():
            if not any(folder_path.iterdir()):
                print(f"Would delete empty folder: {folder_path}")
            else:
                print(f"Would delete folder (contains files): {folder_path}")
        else:
            print(f"Folder not found: {folder_path}")
