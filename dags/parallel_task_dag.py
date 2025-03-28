from datetime import timedelta, datetime
from time import sleep

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum.tz.timezone import Timezone

with DAG(
    dag_id="02_parallel_tasks",
    description="병렬적인 Task 의존성을 가지는 DAG 예제입니다",
    default_args={
        "owner": "minseok",
        "retries": 1,
        "retry_delay": timedelta(minutes=1)
    },
    start_date=datetime(2022, 1, 20, tzinfo=Timezone("Asia/Seoul")),
    schedule_interval="@once",
    tags=["examples", "01_writing_various_task_flows"]
) as dag:

    def dump() -> None:
        sleep(3)

    t1 = PythonOperator(task_id="task_1", python_callable=dump)
    t2 = PythonOperator(task_id="task_2", python_callable=dump)
    t3 = PythonOperator(task_id="task_3", python_callable=dump)
    t4 = PythonOperator(task_id="task_4", python_callable=dump)
    t5 = PythonOperator(task_id="task_5", python_callable=dump)

    t1 >> t2 >> t5
    t3 >> t4 >> t5