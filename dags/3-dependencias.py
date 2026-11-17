from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_hello():
    print("Hello World!")

with DAG(
    dag_id="Pimer dag con dependencias",
    start_date=datetime(2026, 11, 13),
    schedule="@once",
    description="My first DAG",
) as dag:

    t1 = PythonOperator(task_id="hello_with_python", python_callable=print_hello)
    t2 = BashOperator(task_id="tarea_2", bash_command="echo 'tarea 2'")
    t3 = BashOperator(task_id="tarea_3", bash_command="echo 'tarea 3'")
    t4 = BashOperator(task_id="tarea_4", bash_command="echo 'tarea 4'")


    t1>>[T2, t3]>>t4