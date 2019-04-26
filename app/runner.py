from . import run_kubernetes
from .runner_result import RunnerResult


def run(image: str) -> RunnerResult:
    return run_kubernetes.run(image)
