






# 2023

## 09



## 08

### 25 airflow dags reload interval

- https://stackoverflow.com/questions/43606311/refreshing-dags-without-web-server-restart-apache-airflow
- after how much time a new DAGs should be picked up from the filesystem
min_file_process_interval = 0


### 24

af_dev_ops
- af_op: 
- af_de: 
- backup: /Users/dwyk/d2/s3/m8/vsc/n4af9 


### 12

https://stackoverflow.com/questions/29957456/change-default-terminal-app-in-visual-studio-code-on-mac

### 

AIRFLOW_HOME
AF3_HOME
AF3_BIN
AF3_ACD=p9af9

### 12

https://airflow.apache.org/docs/apache-airflow/stable/start.html
https://stackoverflow.com/questions/43410836/how-to-remove-default-example-dags-in-airflow


```


AIRFLOW_VERSION=2.6.3

# Extract the version of Python you have installed. If you're currently using Python 3.11 you may want to set this manually as noted above, Python 3.11 is not yet supported.
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.6.3 with python 3.7: https://raw.githubusercontent.com/apache/airflow/constraints-2.6.3/constraints-3.7.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

```

## 07

/Users/dwyk/d2/s2/m6-/ve-/air39/flow1
/Users/dwyk/d2/s2/m6-/ve-/air39/a39a
