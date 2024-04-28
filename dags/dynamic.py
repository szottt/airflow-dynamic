from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import json

bucket = "airflow-dynamic"
config = "config/"

obj = "/home/szot/projetos/eng/aws/airflow/config/dynamic.json"
file = open(obj)
arq_config = json.load(file)


def create_dag(
    dag_id,
    schedule,
    dag_number,
    default_args,
    tags,
    catchup,
):
    dag = DAG(
        dag_id,
        schedule_interval=schedule,
        default_args=default_args,
        start_date=datetime(2024, 8, 28),
        tags=tags,
        catchup=catchup,
    )

    def helloWorld():
        print("Hello World")

    with dag:
        task1 = PythonOperator(
            task_id="hello_world", python_callable=helloWorld, dag=dag
        )
    return dag


default_args = {
    "owner": "Igor",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
}

for arq in arq_config:
    dag_id = f"{str(arq)}"
    schedule = f"{arq_config[str(arq)][1]}"
    dag_number = f"{str(arq)}"
    tags = [f"{arq_config[str(arq)][2]}"]
    catchup = False

    globals()[dag_id] = create_dag(
        dag_id, schedule, dag_number, default_args, tags, catchup
    )
