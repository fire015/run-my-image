from kubernetes import client, config
from .runner_result import RunnerResult
from pprint import pprint


# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/BatchV1Api.md
# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Job.md
# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1JobSpec.md
# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ObjectMeta.md

def run(image: str) -> RunnerResult:
    config.load_incluster_config()

    metadata = client.models.v1_object_meta.V1ObjectMeta(
        generate_name='rmi-',
        labels={'app': 'rmi'}
    )

    spec = client.models.v1_job_spec.V1JobSpec(
        backoff_limit=0,
        # active_deadline_seconds=30,
        ttl_seconds_after_finished=10, # currently an alpha feature (https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#ttl-mechanism-for-finished-jobs)
        template=client.models.v1_pod_template_spec.V1PodTemplateSpec(
            spec=client.models.v1_pod_spec.V1PodSpec(
                restart_policy='Never',
                containers=[
                    client.models.v1_container.V1Container(
                        name='rmi',
                        image=image,
                        image_pull_policy='IfNotPresent'
                    ),
                    client.models.v1_container.V1Container(
                        name='tcpdump',
                        image='nicolaka/netshoot',
                        command=['tcpdump'],
                        args=['-n', 'tcp[13] & 8 != 0']
                    )
                ]
            )
        )
    )

    job = client.V1Job(api_version='batch/v1', kind='Job', metadata=metadata, spec=spec)
    api = client.BatchV1Api(client.ApiClient())
    job_response = api.create_namespaced_job(namespace='default', body=job)  # type: client.models.v1_job.V1Job

    return RunnerResult(True, job_response)
