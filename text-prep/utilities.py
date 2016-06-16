import os


def scan_folder(folder_path, pattern):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if pattern in filename:
                yield os.path.join(root, filename)
