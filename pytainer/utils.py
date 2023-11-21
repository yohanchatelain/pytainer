import subprocess


class CommandHandler(subprocess.CompletedProcess):
    def __init__(self, command):
        self.command = command
        self.result = run_command(self.command)
        self.stdout = self.result.stdout
        self.stderr = self.result.stderr
        self.returncode = self.result.returncode

    def has_failed(self):
        if self.result.returncode != 0:
            return True
        else:
            return False

    def has_succeeded(self):
        if self.result.returncode == 0:
            return True
        else:
            return False

    def get_stdout(self):
        return self.result.stdout

    def get_stderr(self):
        return self.result.stderr

    def get_returncode(self):
        return self.result.returncode

    def get_command(self):
        return self.command


def run_command(command):
    try:
        command = flatten(command)
        command = " ".join(command)
        result = subprocess.run(
            command, capture_output=True, shell=True, text=True, check=True
        )
        return result
    except subprocess.CalledProcessError as e:
        result = subprocess.CompletedProcess(
            args=command, stderr=e.stderr, returncode=e.returncode
        )
        return result


def flatten(lst):
    """
    Flatten a list of arbitrary depth.

    Args:
    lst (list): A list, potentially nested to arbitrary depth.

    Returns:
    list: A flattened version of the input list.
    """
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursive call for nested lists
        else:
            flat_list.append(item)
    return flat_list
