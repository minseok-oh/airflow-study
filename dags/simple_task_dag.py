from datetime import timedelta, datetime, timezone

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum.tz.timezone import Timezone

with DAG(
    dag_id="01_simple_tasks",
    description="가장 심플한 Task 의존성을 가지는 DAG 예제입니다",
    default_args={
        "owner": "minseok",
        "retries": 1,
        "retry_delay": timedelta(minutes=1)
    },
    start_date=datetime(2022, 1, 20, tzinfo=Timezone("Asia/Seoul")),
    schedule_interval="@once",
    tags=["examples", "01_writing_various_task_flows"],
) as daf:

    def dump() -> None:
        sleep(3)

    t1 = PythonOperator(task_id="task_1", python_callable=dump)
    t2 = PythonOperator(task_id="task_2", python_callable=dump)
    t3 = PythonOperator(task_id="task_3", python_callable=dump)

    t1 >> t2 >> t3