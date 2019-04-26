import docker
from .runner_result import RunnerResult
from docker.models.containers import Container
from requests.exceptions import RequestException

READ_TIMEOUT = 10


def run(image: str) -> RunnerResult:
    client = docker.from_env()
    container = client.containers.run(image=image, detach=True)  # type: Container

    try:
        result = container.wait(timeout=READ_TIMEOUT)

        return RunnerResult(result['StatusCode'], container.logs())
    except RequestException:
        return RunnerResult(-1, container.logs())
    finally:
        container.remove(force=True)
