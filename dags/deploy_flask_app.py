# deploy_flask_app.py

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 3, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'deploy_flask_app',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

build_image = BashOperator(
    task_id='build_image',
    bash_command='docker build -t my-flask-app .',
    dag=dag
)

run_container = BashOperator(
    task_id='run_container',
    bash_command='docker run -p 5000:5000 my-flask-app',
    dag=dag
)

build_image >> run_container