# Downloads Organizer – Python Automation Script

This Python script helps keep your Downloads folder clean by automatically sorting files into folders based on file type.

---

## What It Does

- Moves `.jpg`, `.jpeg`, and `.png` files to a **Photos** folder
- Moves `.pdf` files to a **Docs** folder
- Moves `.jar` files to a **Jars** folder
- Sends everything else to a **Misc** folder
- Skips folders and only touches actual files
- Creates the folders if they don’t already exist

---

## What I Learned

- How to loop through files using `os.listdir()`
- How to safely move files using `shutil.move()`
- How to check file extensions and skip directories
- How to automate a real-life problem and save time

---

## Tools & Concepts

- Python 3
- `os` and `shutil` libraries
- File path construction
- Case-insensitive string checks
- Folder creation with `os.makedirs()`

---
