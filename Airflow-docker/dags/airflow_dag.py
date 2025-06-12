from airflow import DAG
from airflow.operators.python import PythonOperator
from extract import extract_api
from datetime import datetime

default_args = {
    'owner': 'kaycee',
    'retries': 1
}

dag = DAG(
    dag_id = "extract_weather_data",
    description = "This is my dag for extracting weather data",
    schedule_interval = "@daily",
    default_args = default_args,
    catchup =  False,
    start_date = datetime(2025,6,10)
)

extract_to_s3 = PythonOperator(
    task_id = "extract_to_s3",
    dag = dag,
    python_callable = extract_api
)

extract_to_s3