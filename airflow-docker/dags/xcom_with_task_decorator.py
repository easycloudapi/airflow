from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
import pendulum


val1 = [1, 2, 3]
val2 = {"key1": "value1", "key2": "value2"}

@task(task_id='xcom_push_by_ti')
def _xcom_push_by_ti(ti=None):
    ti.xcom_push(key='direct_xcom_push_1', value=val1)
    
@task(task_id='xcom_push_by_returning')
def _xcom_push_by_returning():
    return val2

default_args = {
    "owner": "EasyCloudAPI",
    "start_date": pendulum.datetime(2023, 9, 1, tz="UTC"),
    "schedule_interval": "@once",
    "depends_on_past": False,
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3)
}

with DAG(
    dag_id='xcom_with_task_decorator',
    default_args=default_args,
    catchup=False,
    tags=['eca_learning', 'task decorator', 'XCom']
) as dag:
    
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end', trigger_rule=TriggerRule.NONE_FAILED)
    
    xcom_push_by_ti = _xcom_push_by_ti()
    xcom_push_by_returning = _xcom_push_by_returning()
    
    bash_push_xcom_by_manual_return = BashOperator(
        task_id='bash_push_xcom_by_manual_return',
        bash_command='echo "Manually set xcom values '
        '{{ ti.xcom_push(key="manually_pushed_xcom_from_bash", value="manually pushed values from bash command") }}" && '
        'echo "value by return"',
        do_xcom_push=True
    )
    
    bash_push_xcom_by_return = BashOperator(
        task_id='bash_push_xcom_by_return',
        bash_command='echo "return only xcom values"',
        do_xcom_push=True
    )
    
    start >> [xcom_push_by_ti, xcom_push_by_returning] >> end
    start >> [bash_push_xcom_by_manual_return, bash_push_xcom_by_return] >> end
