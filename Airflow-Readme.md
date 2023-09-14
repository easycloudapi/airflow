# Learn Airflow (Step-By-Step Process):

## To setup Airflow locally-
1. Follow the setup guidance: [developer-guide.md](developer-guide.md)


## Understand Airflow-


### Airflow Architechture-
![airflow_architecture](https://github.com/easycloudapi/learn_airflow/assets/108976294/409c8ae8-e8ff-4c2e-82ca-21c524482251)

### Airflow Components-

| Name | Description | Links | Comments |
| :--- | :------ | :---: | --- |
| `1. Webserver` | A Flask server running with Gunicorn that serves the Airflow UI | https://docs.astronomer.io/learn/airflow-components | |
| `2. Scheduler` | A Daemon responsible for scheduling jobs. This is a multi-threaded Python process that determines what tasks need to be run, when they need to be run, and where they are run. `Executor` - The mechanism for running tasks. An executor is running within the scheduler whenever Airflow is operational. | | |
| `3. Metadata Databse` | where all DAG and task metadata are stored. This is typically a Postgres database, but MySQL, MsSQL, and SQLite are also supported. | | |
| | | | |
    
### Airflow DAG Properties-

| Name | Description | Comments
| :--- | :---: | :---
| | |

