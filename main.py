from app import runner, monitor
from pprint import pprint

DOCKER_IMAGE = 'fire015/python-rmi-test:latest'

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def init():
    result = runner.run(DOCKER_IMAGE)

    if result.success:
        print(OKGREEN + ">>> Success: " + result.name + ENDC)
        monitor.monitor(result)
    else:
        print(FAIL + ">>> Failed" + ENDC)


if __name__ == '__main__':
    init()
