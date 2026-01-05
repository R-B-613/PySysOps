import os


def search_text_in_file(word, file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_number, line in enumerate(f, start=1):
                if word in line:
                    print(f"{file_path}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def search_text_in_dir(word, path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            full_path = os.path.join(root, filename)
            search_text_in_file(word, full_path)
