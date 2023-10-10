from airflow.providers.cncf.kubernetes.secret import Secret
from kubernetes.client import models as k8s
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled45-1010202517",
}

dag = DAG(
    "untitled45-1010202517",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.16.0.dev0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Deprecated API v1
# from airflow.kubernetes.secret import Secret
# from airflow.contrib.kubernetes.volume import Volume
# from airflow.contrib.kubernetes.volume_mount import VolumeMount


# Operator source: test.py

op_31232e44_7f56_4f0e_90b6_46694388cdfc = KubernetesPodOperator(
    name="test",
    namespace="default",
    image="continuumio/anaconda3@sha256:a2816acd3acda208d92e0bf6c11eb41fda9009ea20f24e123dbf84bb4bd4c4b8",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled45' --cos-endpoint http://minio-1696963931.default.svc.cluster.local:9000 --cos-bucket airflow --cos-directory 'untitled45-1010202517' --cos-dependencies-archive 'test-31232e44-7f56-4f0e-90b6-46694388cdfc.tar.gz' --file 'test.py' "
    ],
    task_id="test",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "rootuser",
        "AWS_SECRET_ACCESS_KEY": "rootpass123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled45-{{ ts_nodash }}",
    },
    volumes=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
