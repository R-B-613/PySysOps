import argparse
from search.file_ops import search_files, batch_rename
from system.process_ops import list_processes, kill_process

def main():
    parser = argparse.ArgumentParser(description="PySysOps: Linux System Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Search Command ---
    search_parser = subparsers.add_parser("search", help="Recursive file search")
    search_parser.add_argument("path", help="Root directory to start search")
    search_parser.add_argument("--key", required=True, help="Keyword to search in filename")
    search_parser.add_argument("--ext", help="Filter by file extension (e.g., .py)")

    # --- Rename Command ---
    rename_parser = subparsers.add_parser("rename", help="Batch rename files")
    rename_parser.add_argument("dir", help="Target directory")
    rename_parser.add_argument("--prefix", required=True, help="Prefix to add to files")
    rename_parser.add_argument("--ext", required=True, help="Target extension")

    # --- Process List Command ---
    ps_parser = subparsers.add_parser("ps", help="List active processes")
    ps_parser.add_argument("--my", action="store_true", help="Show only my processes")

    # --- Kill Command ---
    kill_parser = subparsers.add_parser("kill", help="Terminate a process")
    kill_parser.add_argument("pid", help="Process ID to terminate")
    kill_parser.add_argument("--force", action="store_true", help="Force kill (SIGKILL)")

    args = parser.parse_args()

    if args.command == "search":
        search_files(args.path, args.key, args.ext)
    elif args.command == "rename":
        batch_rename(args.dir, args.prefix, args.ext)
    elif args.command == "ps":
        list_processes(args.my)
    elif args.command == "kill":
        kill_process(args.pid, args.force)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()