from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def print_world() -> None:
    print("world")


with DAG(
        dag_id="hello_world",
        description="hello_world",
        start_date=days_ago(2),
        schedule_interval=timedelta(days=1),
        tags=["example"],
        default_args={
            "owner": "minseok",
            "retries": 5,
            "retry_delay": timedelta(minutes=5)
        }
) as dag:
    t1 = BashOperator(
        task_id="print_hello",
        bash_command="echo Hello",
    )

    t2 = PythonOperator(
        task_id="print_world",
        python_callable=print_world,
    )

    t1 >> t2
