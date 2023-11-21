import pytest
from pytainer import Pytainer
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ALPINE_DOCKER_REMOTE_IMAGE = "docker://alpine:latest"
ALPINE_APPTAINER_REMOTE_IMAGE = "library://alpine:latest"
ALPINE_APPTAINER_DEFINITION = os.path.join(ROOT_PATH, "alpine.def")
ALPINE_APPTAINER_SINGULARITY = os.path.join(ROOT_PATH, "alpine.sif")


def clean_env():
    if os.path.exists(ALPINE_APPTAINER_SINGULARITY):
        os.remove(ALPINE_APPTAINER_SINGULARITY)


# Test for the build method
def test_build():
    clean_env()
    pytainer = Pytainer()
    result = pytainer.build(ALPINE_APPTAINER_DEFINITION, ALPINE_APPTAINER_SINGULARITY)
    assert result.returncode == 0


# Test for the pull method
def test_pull():
    clean_env()
    pytainer = Pytainer()
    result = pytainer.pull(ALPINE_APPTAINER_REMOTE_IMAGE, ALPINE_APPTAINER_SINGULARITY)
    assert result.returncode == 0


def test_exec_success():
    pytainer = Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytainer.exec("ls /")
    assert result.returncode == 0


def test_exec_failure():
    pytainer = Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytainer.exec("unkown command")
    assert result.returncode != 0


# Test for the exec method
def test_exec():
    pytainer = Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytainer.exec("ls /")
    assert result.returncode == 0


# Test for the run method
def test_run():
    pytainer = Pytainer(ALPINE_DOCKER_REMOTE_IMAGE)
    result = pytainer.run('echo "Hello from container"')
    assert result.returncode == 0


if __name__ == "__main__":
    test_build()
    test_pull()
    test_exec_success()
    test_exec_failure()
    test_exec()
    test_run()
    print("All tests passed!")
