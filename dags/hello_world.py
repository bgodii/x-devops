from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world from Airflow DAG!'

with DAG(
    dag_id='hello_world',
    schedule_interval='@once',
    start_date=datetime(2017, 3, 20),
    catchup=False
) as dag:
    hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
    
    hello_operator