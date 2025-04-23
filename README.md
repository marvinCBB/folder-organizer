# 🗂️ Folder Organizer with Restore and Date Features

A smart and flexible Python script to organize messy folders by file type or date.  
Includes collision-safe file moves, undo functionality, and auto-cleanup of empty folders on restore.

---

## 🚀 Features

- ✅ Organize files by **category** (Documents, Images, Audio, etc.)
- 📅 Organize files into **year/month folder trees**
- 🏷️ Prepend last modified date to filenames (e.g., `2024-04-18-report.pdf`)
- 🔁 **Restore** last move operation (undo)
- 🧹 Cleans up **empty folders** after restore
- 🧠 Collision-safe: renames files automatically if destination already exists

---

## 🛠 Requirements

- Python 3.6+

Install required modules (standard library only — no `pip` needed)

---

## 🧪 Example Usage

**1. Organize by file type (default):**
```bash
python folder_organizer.py
```

**2. Organize by last modified date (folder tree):**
```bash
python folder_organizer.py --by-date
```

**3. Prepend date to filenames only:**
```bash
python folder_organizer.py --prepend-date
```

**4. Combine both date folder + date prefix:**
```bash
python folder_organizer.py --by-date --prepend-date
```

**5. Restore previous organization:**
```bash
python folder_organizer.py --restore
```

---

## 📁 Example Output

```
Before:
test_folder/
├── img.jpg
├── document.pdf
├── song.mp3

After (--by-date --prepend-date):
test_folder/
└── 2024/
    └── April/
        ├── 2024-04-18-img.jpg
        ├── 2024-04-18-document.pdf
        └── 2024-04-18-song.mp3
```

---

## 👨‍💻 Author

**marvinCBB**  
Freelance automation & scripting developer  
GitHub: [https://github.com/marvinCBB](https://github.com/marvinCBB)

---

## 📌 Coming Soon

- `--dry-run` mode to preview changes before moving files  
- Config file support for custom rules  
- GUI version for non-tech users  

---

## 🆕 v3.1 Improvements

- ✅ Added support for **recursive organization** (default behavior)
- ✅ Now skips the internal `restore.txt` file during reorganization
- ✅ Improved folder cleanup logic:
  - On **organize**: deletes empty folders from file’s original location up to base folder
  - On **restore**: prevents climbing above the base folder (`target_folder`), avoiding infinite loops or accidental deletion
- ✅ Safer and more symmetric handling between organize and restore modes

These changes make the script safer and more robust in deeply nested folder structures.
