from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def load_csv_to_bq():
    print("Simulate loading CSV from GCS to BigQuery")

with DAG('gcs_to_bq_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    task = PythonOperator(
        task_id='load_csv',
        python_callable=load_csv_to_bq
    )
