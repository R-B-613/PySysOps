import sys
from search.file_search import search_file_by_name, search_file_by_ext
from search.text_search import search_text_in_file, search_text_in_dir


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == "file":
        handle_file(sys.argv[2:])
    elif command == "text":
        handle_text(sys.argv[2:])
    else:
        print("Unknown command")
        print_usage()


def handle_file(args):
    if len(args) < 2:
        print("Usage: file <name|ext> <value> [--path PATH]")
        return

    subcommand = args[0]
    value = args[1]
    path = "."

    if "--path" in args:
        idx = args.index("--path")
        if idx + 1 < len(args):
            path = args[idx + 1]

    if subcommand == "name":
        search_file_by_name(value, path)
    elif subcommand == "ext":
        search_file_by_ext(value, path)
    else:
        print("Unknown file subcommand")


def handle_text(args):
    if len(args) < 4:
        print("Usage: text word <word> --file FILE | --path DIR")
        return

    subcommand = args[0]
    word = args[1]
    option = args[2]
    target = args[3]

    if subcommand != "word":
        print("Unknown text subcommand")
        return

    if option == "--file":
        search_text_in_file(word, target)
    elif option == "--path":
        search_text_in_dir(word, target)
    else:
        print("Unknown option")


def print_usage():
    print("Examples:")
    print("  python3 main.py file name test")
    print("  python3 main.py file ext .py --path .")
    print("  python3 main.py text word hello --file test.txt")
    print("  python3 main.py text word error --path .")


if __name__ == "__main__":
    main()
