from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
from random import randint


def _print_kwargs(**kwargs):
    """
    print airflow default kwargs value 
    Returns:
        None: No return value
    """
    print(f'kwargs: {kwargs}')

def _gen_random_num():
    """
    generate random number
    Returns:
        int: random integer value
    """
    return randint(1,100)

def _check_even_or_odd(**kwargs):
    ti = kwargs.get('ti')
    random_num = ti.xcom_pull(task_ids='gen_random_num')  # key='return_value' is default, so not require to include
    
    if random_num % 2 == 0:
        return "even_bash"
    else:
        return "odd_bash"


default_args = {
    "owner": "EasyCloudAPI",
    "start_date": datetime(2023,9,21),
    "depends_on_past": False,
    "schedule_interval": '@daily',
    "email": ["info.easycloudapi@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(dag_id="python_bash_operators",
         description="Learn Python and Bash Operators",
         default_args=default_args,
         catchup=False,
         max_active_runs=1,
         tags=['eca_learning', 'Python', 'Bash', 'XCom', 'TriggerRule']) as dag:
    
    start = EmptyOperator(task_id='start', dag=dag)
    end = EmptyOperator(task_id='end', trigger_rule=TriggerRule.NONE_FAILED, dag=dag)
    
    print_kwargs = PythonOperator(
        task_id='print_kwargs',
        python_callable=_print_kwargs,
        # op_kwargs={"emp_name": "Indranil Pal"},
        dag=dag
    )
    
    gen_random_num = PythonOperator(
        task_id='gen_random_num',
        python_callable=_gen_random_num
    )
    
    check_even_or_odd = BranchPythonOperator(
        task_id='check_even_or_odd',
        python_callable=_check_even_or_odd
    )
    
    even_bash = BashOperator(
        task_id='even_bash',
        bash_command='echo "even number"'
    )
    
    odd_bash = BashOperator(
        task_id='odd_bash',
        bash_command='echo "odd number"'
    )
    
    start >> print_kwargs  >> gen_random_num >> check_even_or_odd >>  \
        [even_bash, odd_bash] >> end