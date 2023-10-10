from airflow.providers.cncf.kubernetes.secret import Secret
from kubernetes.client import models as k8s
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled999-1010205531",
}

dag = DAG(
    "untitled999-1010205531",
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
    image="amancevice/pandas@sha256:f74bef70689b19d3cd610ef67227fce1c9a6ed8fa950ac2aff39ce72310d5520",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled999' --cos-endpoint http://minio-1696963931.default.svc.cluster.local:9000 --cos-bucket airflow --cos-directory 'untitled999-1010205531' --cos-dependencies-archive 'test-31232e44-7f56-4f0e-90b6-46694388cdfc.tar.gz' --file 'test.py' "
    ],
    task_id="test",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "rootuser",
        "AWS_SECRET_ACCESS_KEY": "rootpass123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled999-{{ ts_nodash }}",
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
