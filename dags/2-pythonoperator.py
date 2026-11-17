from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello World!")

with DAG(
    dag_id="pythonoperator",
    start_date=datetime(2026, 11, 13),
    schedule="@once",
    description="My first DAG",
) as dag:

    t1 = PythonOperator(task_id="hello_with_python", python_callable=print_hello)