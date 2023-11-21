import subprocess


def run_command(command):
    try:
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
