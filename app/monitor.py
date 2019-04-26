from kubernetes import client, config, watch
from .runner_result import RunnerResult
from pprint import pprint

MAX_OUTGOING_MESSAGES = 10


def monitor(result: RunnerResult):
    config.load_incluster_config()

    w = watch.Watch()
    api = client.CoreV1Api()
    selector = 'job-name={}'.format(result.name)
    pod_name = None

    for event in w.stream(api.list_pod_for_all_namespaces, label_selector=selector, timeout_seconds=30):
        # print("Event: %s %s %s" % (event['type'], event['object'].metadata.name, event['object'].status.phase))

        if event['object'].status.phase == 'Running':
            pod_name = event['object'].metadata.name
            w.stop()

    if pod_name is None:
        return

    total = 0

    for message in w.stream(api.read_namespaced_pod_log, name=pod_name, namespace='default', container='tcpdump',
                            follow=True):
        outgoing = process_log(message)

        if outgoing:
            total += 1

            if total > MAX_OUTGOING_MESSAGES:
                print("Stopping")
                w.stop()


def process_log(message: str) -> bool:
    words = message.split(' ')

    if words[1] == 'IP' and words[2][0:3] == '10.':
        print(message)
        return True

    return False
