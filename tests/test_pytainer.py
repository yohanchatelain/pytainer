import pytainer
import os
import io

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ALPINE_DOCKER_REMOTE_IMAGE = "docker://alpine:latest"
ALPINE_APPTAINER_REMOTE_IMAGE = "library://alpine:latest"
ALPINE_APPTAINER_DEFINITION = os.path.join(ROOT_PATH, "alpine.def")
ALPINE_APPTAINER_IMAGE = os.path.join(ROOT_PATH, "alpine.sif")


def clean_env():
    if os.path.exists(ALPINE_APPTAINER_IMAGE):
        os.remove(ALPINE_APPTAINER_IMAGE)


# Test for the build method
def test_build():
    clean_env()
    pytnr = pytainer.Pytainer()
    result = pytnr.build(ALPINE_APPTAINER_DEFINITION, ALPINE_APPTAINER_IMAGE)
    assert result.returncode == 0


# Test for the pull method
def test_pull():
    clean_env()
    pytnr = pytainer.Pytainer()
    result = pytnr.pull(ALPINE_APPTAINER_REMOTE_IMAGE, ALPINE_APPTAINER_IMAGE)
    assert result.returncode == 0


def test_exec_success():
    pytnr = pytainer.Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytnr.exec("ls /")
    assert result.returncode == 0


def test_exec_failure():
    pytnr = pytainer.Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytnr.exec("unkown command")
    assert result.returncode != 0


# Test for the exec method
def test_exec():
    pytnr = pytainer.Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytnr.exec("ls /")
    assert result.returncode == 0


def test_inspect():
    pytnr = pytainer.Pytainer(ALPINE_APPTAINER_IMAGE)
    options = pytainer.PytainerOptionsInspect()
    options.all()
    result = pytnr.inspect(options=options)
    assert result.returncode == 0


# Test for the run method
def test_run():
    pytnr = pytainer.Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytnr.run('echo "Hello from container"')
    assert result.returncode == 0


def test_pytainer_option_exec():
    options = pytainer.PytainerOptionsExec()
    options.workdir("/home")
    options.env("ENV_VAR", "1")
    options.env("ENV_VAR", "2")
    fmt = options.to_string()
    assert fmt == "--workdir /home --env ENV_VAR=1 --env ENV_VAR=2"


def test_pytainer_option_run():
    options = pytainer.PytainerOptionsRun()
    options.workdir("/home")
    options.env("ENV_VAR", "1")
    options.env("ENV_VAR", "2")
    fmt = options.to_string()
    assert fmt == "--workdir /home --env ENV_VAR=1 --env ENV_VAR=2"


def test_pytainer_option_pull():
    options = pytainer.PytainerOptionsPull()
    options.force()
    options.disable_cache()
    _repr = options.__repr__()
    assert _repr == "PytainerOptionsPull(--force --disable-cache)"


if __name__ == "__main__":
    test_build()
    test_pull()
    test_exec_success()
    test_exec_failure()
    test_exec()
    test_run()
    print("All tests passed!")
