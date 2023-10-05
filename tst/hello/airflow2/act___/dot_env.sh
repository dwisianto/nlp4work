
#
# echo " ===== ENV VARS ==== "
#

#
# [] shortcuts to re-load variables and functions
#
alias af_env_='source ./act___/dot_env.sh'
alias af_src_='source ./act_af/af.sh'
# alias af_src_
# alias af_env_


#
# [] CONDA
#
export ACD_BIN=$(which conda)  # conda executable binary
export ACD_ENV=base38af27      # a working environment
export ACD_ENV_BASE=base38     # a base env to clone from

export ACD_PIP1=${PWD}/act___/requirement1_pytest.txt
export aCD_PIP2=${PWD}/act___/requirement2.txt
export aCD_PIP3=${PWD}/act___/requirement3.txt
export aCD_PIP4=${PWD}/act___/requirement4.txt
export ACD_PIP5=${PWD}/act___/requirement5_airflow.txt


#
# [] AIRFLOW
#
export AIRFLOW_HOME=${PWD}/act_af_home
export AIRFLOW_CONFIG=${AIRFLOW_HOME}
export PYTHONPATH=${AIRFLOW_HOME}:$PYTHONPATH


export AIRFLOW__CORE__DAGS_FOLDER=${AIRFLOW_HOME}/dags
export AIRFLOW__CORE__PLUGINS_FOLDER=${AIRFLOW_HOME}/plugins
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:///${AIRFLOW_HOME}/act_af_home/airflow.db
export AIRFLOW__LOGGING__BASE_LOG_FOLDER=${AIRFLOW_HOME}/logs
export AIRFLOW__LOGGING__DAG_PROCESSOR_MANAGER_LOG_LOCATION=${AIRFLOW_HOME}/logs/dag_processor_manager/dag_processor_manager.log
export AIRFLOW__WEBSERVER__CONFIG_FILE=${AIRFLOW_HOME}/webserver_config.py
export AIRFLOW__SCHEDULER__CHILD_PROCESS_LOG_DIRECTORY=${AIRFLOW_HOME}

export AIRFLOW_DB=${AIRFLOW__DATABASE__SQL_ALCHEMY_CONN}
export AIRFLOW_LOG=${AIRFLOW__LOGGING__BASE_LOG_FOLDER}
export AIRFLOW_DAG=${AIRFLOW__CORE__DAGS_FOLDER}
export AIRFLOW_CFG_UI=${AIRFLOW__WEBSERVER__CONFIG_FILE}




export AF_HOME=$AIRFLOW_HOME
export AF_PORT=8080
export AF_LOG=$AIRFLOW_LOG
export AF_CFG=${AIRFLOW_HOME}/airflow.cfg
export AF_DAG=${AIRFLOW_HOME}/dags


#
#
#
#export af_ops=$HOME/d2/s3/m8-/vsc/n4af/$af_uid/${af_uid}home
#export af_home=$af_ops
#export AIRFLOW_HOME=$af_home
#export AF_HOME=$(PWD)
export af_home=${PWD}
export af_db=${af_home}
export af_log=${af_home}/log
export af_dag=${af_home}/act_af/dags
export af_cfg=${af_home}/act_af/airflow.cfg
export af_cfg_ui=${af_home}/webserver_config.cfg


#
# Unique Identifier
#

export af_date_now=$(date +"%m_%d_%Y_%M_%S")
export af_dag_id_hw23a="hw23a"
export af_dag_id=${af_dag_uid_hw23a}
export af_task_id="daf_task_uid"   # unique identifier

#
#
#
#echo af_home      : $af_home
#echo af_cfg       : $af_cfg


#
#
#
#export MY_DATA=$HOME/d/db
#export MY_DAT=$MY_DATA
#echo MY_DATA: $MY_DATA
#echo MY_DAT: $MY_DAT


#
# Connections
#
export AF_CON1_ID='my-con1'
export AF_CON1_TYPE='my-type1'
export AF_CON1_LOGIN="my-login1"
export AF_CON1_PASS='my-pass1'
export AF_CON1_HOST='my-host1'
export AF_CON1_PORT='my-port1'
export AF_CON1_SCHEMA='my-schema1'


export AF_CON2_ID='my-con'
export AF_CON2_TYPE='my-type2'
export AF_CON2_LOGIN="my-login2"
export AF_CON2_PASS='my-pass2'
export AF_CON2_HOST='my-host2'
export AF_CON2_PORT='my-port2'
export AF_CON2_SCHEMA='my-schema2'

