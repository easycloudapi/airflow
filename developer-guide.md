# Learn Airflow


### Python Virtual Env Setup
1. Create Virtual Env on powershell
    ```shell
    python -m virtualenv .venv 

    Set-ExecutionPolicy Unrestricted -Scope Process
    .venv\\Scripts\\activate
    ```
2. Create Virtual Env on WSL2
    ```shell
    sudo apt-get update
    sudo apt install python3-pip
    sudo pip3 install virtualenv

    python3 -m virtualenv .venv
    source .venv/bin/activate
    ```

### Install Airflow (Local Windows Machine)
1. `Install WSL2`: (guide youtube link: https://www.youtube.com/watch?v=aCRMnDLnWmU)
    1. Windows search - "Turn Windows features on or off" 
        1. Select "Virtual Machine Platform" and "Windows Subsystem for Linux"
        2. Restart the windows OS
    2. open CMD
        ```shell
        >wsl --install
        >wsl --status
        >wsl --update

        # if WSL default version is 1 then execute below
        >wsl --set-default-version 2
        ```
    3. Windows Search: "Ubuntu" and install the same.
    

2. `Install Docker and Docker-Compose`
    1. Docker Desktop (link: `https://docs.docker.com/desktop/install/windows-install/`)
        1. Its includes -
            1. Docker Daemon (engine)
            2. Docker Compose: Its allows to run multi container applications
            3. Docker Client: Cli
            4. Kubernetes
        2. Check the version
            ```shell
            docker version
            ```
    2. Docker-Compose: Its allows to run multi container applications and airflow need 3 minimum components
        1. Check the version:
            ```shell
            docker compose version
            ```
3. Follow Below Commands on WSL2 to Install Airflow Locally (Link: https://www.youtube.com/watch?v=aTaytcxy2Ck)
    ```shell
    mkdir airflow-docker
    cd airflow-docker
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
    mkdir ./dags ./plugins ./config ./logs
    echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

    docker-compose up airflow-init
    docker-compose up
    # or
    docker-compose down && docker-compose up

    # in another WSL2 window, run 
    # # Check Docker Containers
    docker ps 

    # # Access Airflow CLI, airflow_commands, airflow version
    docker exec <webserver container_id> airflow version

    # # Access Airflow API
    curl -X GET "http://localhost:8080/api/v1/dags" # will not work
    curl -X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags" # will work
    ```
4. Then open the link "http://localhost:8080/" in browser.