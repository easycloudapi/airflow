from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta


def _training_model_a(**kwargs):
    ti = kwargs['ti']
    print(f'ti: {ti}')
    next_ds = kwargs['next_ds']
    print(f'next_ds: {next_ds}')
    # output = kwargs.get('emp_name')
    # print(f'output: {output}')
    return True


default_args = {
    "owner": "Indranil Pal",
    "start_date": datetime(2023,9,21),
    "depends_on_past": False,
    "schedule_interval": '@daily',
    "email": ["indra.tutun@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(dag_id="task_dependencies",
         description="Learn Task Dependencies",
         default_args=default_args,
         catchup=False,
         max_active_runs=1,
         tags=['Task Dependencies', 'Python Operator']) as dag:
    
    start = EmptyOperator(task_id='start', dag=dag)
    end = EmptyOperator(task_id='end', dag=dag)
    
    training_model_a = PythonOperator(
        task_id='training_model_a',
        python_callable=_training_model_a,
        # op_kwargs={"emp_name": "Indranil Pal"},
        dag=dag
    )
    
    start >> training_model_a >> end