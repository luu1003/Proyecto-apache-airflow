from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(
    dag_id="custom_operator",
    start_date=datetime(2026, 11, 13),
    schedule="@daily",
    description="My first operador personalizado",
) as dag:


    t1 = HelloOperator(task_id="hello",
                       name="Luchi",)