# Learn Airflow (Step-By-Step Process):

## To setup Airflow locally-
1. Follow the setup guidance: [developer-guide.md](developer-guide.md)


## Understand Airflow-


### Airflow Architechture-
![airflow_architecture](https://github.com/easycloudapi/learn_airflow/assets/108976294/409c8ae8-e8ff-4c2e-82ca-21c524482251)

### Airflow Components-

1.  Ref-
    1. https://docs.astronomer.io/learn/airflow-components


| ID | Name | Description | Remarks |
| :--- | :--- | :------ | --- |
| 1. | `Webserver` | A Flask server running with Gunicorn that serves the Airflow UI | |
| 2. | `Scheduler` | A Daemon responsible for scheduling jobs. This is a multi-threaded Python process that determines what tasks need to be run, when they need to be run, and where they are run. An `executor` is running within the scheduler whenever Airflow is operational. | |
| 3. | `Metadata Databse` | where all DAG and task metadata are stored. This is typically a Postgres database, but MySQL, MsSQL, and SQLite are also supported. | |
| 4. | `Executor` | The mechanism for running tasks. An executor is running within the scheduler whenever Airflow is operational. | |
    
### Airflow DAG Properties-

| ID | Name | Description | Remarks |
| :--- | :--- | :------ | --- |
| 1. | `dag` | Ref: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html <br>a. Directed Acyclic Graph <br>b. Its collects the tasks and execute them based on the dependencies | Main Component of Airflow (dag_id) | |
| 2. | `operator` | Its similar like tasks, which executes the actual job/operations | |
| 3. | | | |
| 4. | | | |
| 5. | | | |
| 6. | | | |

