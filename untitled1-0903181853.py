from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
# from airflow.contrib.kubernetes.volume_mount import VolumeMount
# from airflow.contrib.kubernetes.volume import Volume
# from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled1-0903181853",
}

dag = DAG(
    "untitled1-0903181853",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `untitled1.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: mainTest.py

# op_fdbddb78_18cb_448a_a9ec_fdbaa75cdf74 = KubernetesPodOperator(
#     name="mainTest",
#     namespace="default",
#     image="continuumio/anaconda3@sha256:a2816acd3acda208d92e0bf6c11eb41fda9009ea20f24e123dbf84bb4bd4c4b8",
#     cmds=["sh", "-c"],
#     arguments=[
#         "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled1' --cos-endpoint http://minio-1693764492.minio.svc.cluster.local:9000 --cos-bucket testbucket --cos-directory 'untitled1-0903181853' --cos-dependencies-archive 'mainTest-fdbddb78-18cb-448a-a9ec-fdbaa75cdf74.tar.gz' --file 'mainTest.py' "
#     ],
#     task_id="mainTest",
#     env_vars={
#         "ELYRA_RUNTIME_ENV": "airflow",
#         "AWS_ACCESS_KEY_ID": "rootuser",
#         "AWS_SECRET_ACCESS_KEY": "rootpass123",
#         "ELYRA_ENABLE_PIPELINE_INFO": "True",
#         "ELYRA_RUN_NAME": "untitled1-{{ ts_nodash }}",
#     },
#     volumes=[],
#     volume_mounts=[],
#     secrets=[],
#     annotations={},
#     labels={},
#     tolerations=[],
#     in_cluster=True,
#     config_file="None",
#     dag=dag,
# )

write_xcom = KubernetesPodOperator(
    namespace="default",
    image="alpine",
    cmds=["sh", "-c", "mkdir -p /airflow/xcom/;echo '[1,2,3,4]' > /airflow/xcom/return.json"],
    name="write-xcom",
    do_xcom_push=True,
    on_finish_action="delete_pod",
    in_cluster=True,
    task_id="write-xcom",
    get_logs=True,
)

pod_task_xcom_result = BashOperator(
    bash_command="echo \"{{ task_instance.xcom_pull('write-xcom')[0] }}\"",
    task_id="pod_task_xcom_result",
)

write_xcom >> pod_task_xcom_result
