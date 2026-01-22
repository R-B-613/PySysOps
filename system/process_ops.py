import os
import subprocess
import signal


def list_processes(user_only=False):
    """
    Lists running processes using 'ps'.
    """
    cmd = ['ps', '-aux']
    if user_only:
        current_user = os.environ.get('USER')
        print(f"[*] Showing processes for user: {current_user}")
        cmd = ['ps', '-u', current_user]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.split('\n')

        # Print header and limited output
        print(lines[0])
        for line in lines[1:16]:
            if line:
                print(line)
        if len(lines) > 16:
            print("... (Output truncated for readability)")

    except Exception as e:
        print(f"Error fetching processes: {e}")


def kill_process(pid, force=False):
    """
    Terminates a process by PID.
    """
    try:
        pid = int(pid)
        sig = signal.SIGKILL if force else signal.SIGTERM
        os.kill(pid, sig)
        print(f"[*] Process {pid} has been terminated successfully.")
    except ProcessLookupError:
        print(f"Error: Process {pid} not found.")
    except PermissionError:
        print(f"Error: Permission denied. Try running with sudo.")
    except ValueError:
        print("Error: PID must be an integer.")