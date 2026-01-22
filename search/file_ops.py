import os


def search_files(start_path, keyword, extension=None):
    """
    Recursively searches for files matching a keyword and/or extension.
    """
    if not os.path.exists(start_path):
        print(f"Error: The path '{start_path}' does not exist.")
        return

    print(f"[*] Searching in: {start_path}")
    print(f"[*] Keyword: '{keyword}' | Extension: {extension if extension else 'All'}")
    print("-" * 50)

    matches_found = 0
    for root, _, files in os.walk(start_path):
        for file in files:
            if extension and not file.endswith(extension):
                continue

            if keyword in file:
                full_path = os.path.join(root, file)
                try:
                    size_kb = os.path.getsize(full_path) / 1024
                    print(f"[+] Found: {full_path} ({size_kb:.2f} KB)")
                    matches_found += 1
                except OSError:
                    pass  # Skip files we can't access

    print("-" * 50)
    print(f"Search complete. Total matches: {matches_found}")


def batch_rename(directory, prefix, extension):
    """
    Batch renames files in a directory by adding a prefix.
    """
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, f"{prefix}_{filename}")
            try:
                os.rename(old_path, new_path)
                print(f"[Rename] {filename} -> {prefix}_{filename}")
                count += 1
            except OSError as e:
                print(f"[Error] Could not rename {filename}: {e}")

    print(f"Batch operation finished. Renamed {count} files.")