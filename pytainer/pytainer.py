from .utils import run_command


class Pytainer:
    def __init__(self, image_path=None):
        self.image_path = image_path

    def exec(self, command):
        cmd = ["apptainer", "exec", self.image_path, command]
        return run_command(cmd)

    def pull(self, image_uri, save_path=None):
        save_path = save_path or self.image_path
        cmd = ["apptainer", "pull", save_path, image_uri]
        return run_command(cmd)

    def build(self, definition_file, image_path):
        cmd = ["apptainer", "build", image_path, definition_file]
        return run_command(cmd)

    def inspect(self, options=None):
        options = options or ""
        cmd = ["apptainer", "inspect", options, self.image_path]
        return run_command(cmd)

    def run(self, command):
        cmd = ["apptainer", "run", self.image_path, command]
        return run_command(cmd)

    # Additional methods can be added here for other Apptainer functionalities
