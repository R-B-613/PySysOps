import os


def search_file_by_name(pattern, path="."):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if pattern in filename:
                print(os.path.join(root, filename))


def search_file_by_ext(ext, path="."):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(ext):
                print(os.path.join(root, filename))
