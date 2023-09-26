
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

import datetime 


# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

# [START instantiate_dag]
with DAG(
    "ner23a",
    description="A simple tutorial DAG",
    schedule=datetime.timedelta(days=1),
    start_date=datetime.datetime(2023, 1, 1),
    catchup=False,
    tags=["ner"],
) as dag:
    # [END instantiate_dag]
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )
    
    t1
