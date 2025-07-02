#Import Libraries
import os
import shutil

#Set folder path
downloads_path = '/Users/kaihu/Downloads'

#Define where the organized folders will go
photos_folder = os.path.join(downloads_path, 'Photos')
docs_folder = os.path.join(downloads_path, 'Docs')
jar_folder = os.path.join(downloads_path, 'Jars')
misc_folder = os.path.join(downloads_path, 'Misc')

#Make the folders if they don't exist already
os.makedirs(photos_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(jar_folder, exist_ok=True)
os.makedirs(misc_folder, exist_ok=True)

#Loop through the files in Downloads
for filename in os.listdir(downloads_path):
    filepath = os.path.join(downloads_path, filename)

    #Skip folders, we only want files
    if os.path.isdir(filepath):
        continue

    #Check file type and move
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        shutil.move(filepath, os.path.join(photos_folder, filename))
        print(f"Moved {filename} to Photos")

    elif filename.lower().endswith('.jar'):
        shutil.move(filepath, os.path.join(jar_folder, filename))
        print(f"Moved {filename} to Jars")

    elif filename.lower().endswith('.pdf'):
        shutil.move(filepath, os.path.join(docs_folder, filename))
        print(f'Moved {filename} to Docs')

    else:
        shutil.move(filepath, os.path.join(misc_folder, filename))


print("Downloads folder cleaned up!")
