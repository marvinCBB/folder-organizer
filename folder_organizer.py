from pathlib import Path
import shutil
import argparse
from datetime import datetime

# Command-line interface
parser = argparse.ArgumentParser(description="Organize a folder by category or date, with optional date prefix, or restore last changes.")
parser.add_argument('--restore', action='store_true', help='Restore the last operation')
parser.add_argument('--by-date', action='store_true', help='Organize files by last modified year/month')
parser.add_argument('--prepend-date', action='store_true', help='Add date prefix to filename (YYYY-MM-DD-)')
parser.add_argument('--recursive', action='store_true', help='Organize files recursively in all folders and subfolders')

args = parser.parse_args()

restore = args.restore
organize_by_date = args.by_date
prepend_date = args.prepend_date
organize_by_category = not args.by_date and not args.restore
recursive=args.recursive
# Setup
target_folder = Path('./test_folder')
restore_file = target_folder / 'restore.txt'

if restore:
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
                    source_path.parent.mkdir(exist_ok=True)
                    shutil.move(destination_path, source_path)
                    print(f"Restored: {destination_path.name}")
                    remove_folder=destination_path.parent
                    while target_folder != remove_folder:                        
                        if not any(remove_folder.iterdir()):  
                            print(f'folder to delete:{remove_folder}')                   
                            remove_folder.rmdir()                            
                        else: 
                            break
                        remove_folder=remove_folder.parent
                    
            except Exception as e:
                print(f"Error restoring line: {file} — {e}")
        restore_file.unlink()
    else:
        print('No restore file was found.')

else:
    if recursive:
        files=[i for i in target_folder.glob('**/*')if i.is_file() and i != restore_file]
    else:
        files = [f for f in target_folder.iterdir() if f.is_file()]
    print(f"Found {len(files)} files to organize:\n")

    move_log = []

    for file in files:
        # Decide destination folder
        if organize_by_date:
            mod_time = file.stat().st_mtime
            mod_datetime = datetime.fromtimestamp(mod_time)
            year = mod_datetime.strftime("%Y")
            month = mod_datetime.strftime("%B")
            dest_folder = target_folder / year / month
            dest_folder.mkdir(parents=True, exist_ok=True)
            print(f"Target: {year}/{month}/")

        elif organize_by_category:
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

            file_ext = file.suffix.lower()
            category = "Others"
            for cat, ext_list in categories.items():
                if file_ext in ext_list:
                    category = cat
                    break

            dest_folder = target_folder / category
            dest_folder.mkdir(exist_ok=True)
            print(f"Target: {category}/")

        # Optional: prepend date to filename
        filename = file.name
        if prepend_date:
            mod_datetime = datetime.fromtimestamp(file.stat().st_mtime)
            date_prefix = mod_datetime.strftime("%Y-%m-%d")
            filename = f"{date_prefix}-{file.name}"

        # Build destination path
        destination = dest_folder / filename
        copy_number = 1
        while destination.exists():
            destination = dest_folder / f"{destination.stem} ({copy_number}){destination.suffix}"
            copy_number += 1

        shutil.move(file, destination)
        move_log.append(f"{file}||{destination}")
        print(f"Moved: {file.name} → {destination}")
        remove_folder=file.parent
        while target_folder != remove_folder:                        
            if not any(remove_folder.iterdir()):  
                print(f'folder to delete:{remove_folder}')                   
                remove_folder.rmdir()                            
            else: 
                break
            remove_folder=remove_folder.parent

    restore_file.write_text('\n'.join(move_log), encoding='utf-8')
    print("\nAll files organized. Restore log saved.")
