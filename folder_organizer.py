
from pathlib import Path
import shutil
import argparse

# Command-line interface
parser = argparse.ArgumentParser(description="Organize a folder or restore last changes.")
parser.add_argument('--restore', action='store_true', help='Restore the last operation')
args = parser.parse_args()

restore = args.restore

# Improved version of the folder organizer with restore functionality and safer handling

target_folder = Path('./test_folder')
restore_file = target_folder / 'restore.txt'


if restore is True:
    if restore_file.exists():
        backup_reg = restore_file.read_text(encoding='utf-8')
        for file in backup_reg.splitlines():
            try:
                source, destination = file.split('||')
                source_path = Path(source)
                destination_path = Path(destination)

                if source_path.exists():
                    print(f"Skipped: {source} already exists.")
                else:
                    shutil.move(destination_path, source_path)
                    print(f"Restored: {destination_path.name}")
            except Exception as e:
                print(f"Error restoring line: {file} — {e}")
        restore_file.unlink()
    else:
        print('No restore file was found.')

else:
    # List all files in the folder (ignore directories)
    files = [f for f in target_folder.iterdir() if f.is_file()]
    print(f"Found {len(files)} files to organize:\n")

    # Define categories and their associated extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".bat", ".sh"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
        "Others": []
    }

    move_log = []

    for file in files:
        file_ext = file.suffix.lower()
        category = "Others"

        # Determine file category
        for cat, ext_list in categories.items():
            if file_ext in ext_list:
                category = cat
                break

        # Create category folder if it doesn't exist
        dest_folder = target_folder / category
        dest_folder.mkdir(exist_ok=True)

        # Move file to category folder
        destination = dest_folder / file.name
        copy_number = 1

        while destination.exists():
            destination = dest_folder / f"{file.stem} ({copy_number}){file.suffix}"
            copy_number += 1
            print(destination)
            
        shutil.move(file, destination)
        move_log.append(f"{file}||{destination}")
        print(f"Moved: {file.name} → {category}/")

    # Save move log to allow restoration
    restore_file.write_text('\n'.join(move_log), encoding='utf-8')
    print("\nAll files organized. Restore log saved.")
