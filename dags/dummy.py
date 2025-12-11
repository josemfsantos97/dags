from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Dummy function
def print_hello():
    print("Hello from Airflow!")

# Define the DAG
with DAG(
    dag_id="dummy_dag",
    description="A simple dummy DAG for testing",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 12, 11),
    catchup=False,
    tags=["test"],
) as dag:

    task_hello = PythonOperator(
        task_id="say_hello",
        python_callable=print_hello,
    )

    # You can chain tasks if you add more
    task_hello
