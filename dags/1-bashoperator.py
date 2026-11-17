from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bashoperator", start_date=datetime(2026, 11, 13), schedule="@daily", description="My first DAG") as dag:
    t1 = EmptyOperator(task_id="hello_with_bash"),
    bash_command = "echo 'Hello World!'"