import argparse

parser = argparse.ArgumentParser(prog = 'PySysOps', description =
'PySysOps is a Python-based command-line utility designed for developers and system administrators.'
'It simplifies daily tasks such as recursive file searching, batch file renaming, and process '
'monitoring in Linux environments.', epilog = 'TODO - explain for help command')

parser.add_argument(default = 'file')

args = parser.parse_args()
print(args.default)
