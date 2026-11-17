from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="my_dag",
    start_date=datetime(2026, 11, 13),
    schedule="@daily",
    description="My first DAG",
) as dag:

    t1 = EmptyOperator(task_id="dummy")
