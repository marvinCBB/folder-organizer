# Folder Organizer with Restore Capability

This is a simple and practical Python script that automatically organizes files in a given folder by file type. It also includes a **restore feature** to undo the last organization operation, and supports command-line flags for flexibility.

---

## 🚀 Features

- 📂 Automatically sorts files into categorized subfolders (Images, Documents, Videos, etc.)
- 🔄 Restore functionality: moves files back to their original locations
- 🧠 Collision-safe: renames duplicates to prevent overwriting (e.g., file (1).pdf)
- 🖥️ Command-line flag `--restore` to reverse the last organization
- ✅ Uses `pathlib` and `shutil` for clean and modern file operations

---

## 🛠 Requirements

- Python 3.x (tested with 3.9+)

---

## 📦 How to Use

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/folder-organizer.git
cd folder-organizer
```

2. Set your target folder path inside the script (default: `./test_folder`)

3. Run to organize files:
```bash
python folder_organizer.py
```

4. Run to restore files:
```bash
python folder_organizer.py --restore
```

---

## 📁 Example Folder Structure

Before:
```
test_folder/
├── file1.pdf
├── photo.jpg
├── script.py
```

After:
```
test_folder/
├── Documents/
│   └── file1.pdf
├── Images/
│   └── photo.jpg
├── Code/
│   └── script.py
```

---

## 🧪 Upcoming Improvements

- Organize by file date (Year/Month)
- Organize by file size (Small, Medium, Large)
- Dry-run preview mode
- Config file support for user-defined rules

---

## 👨‍💻 Author

**Marvin C. Bustillos Barcaya**  
Freelance automation & coding enthusiast  
GitHub: [https://github.com/marvinCBB](https://github.com/marvinCBB)

---

Feel free to fork or contribute if you find it useful!
