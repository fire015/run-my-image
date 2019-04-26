from kubernetes.client.models.v1_job import V1Job


class RunnerResult:
    def __init__(self, success: bool, job: V1Job):
        self.success = success
        self.job = job

    @property
    def name(self):
        return self.job.metadata.name
