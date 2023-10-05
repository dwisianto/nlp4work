#
#
#




#
# [] env variables

#
# ANACONDA
#
#export af_acd_uid="${ACD_ENV}"

ACD(){
  echo
  echo "==== ANACONDA ==== "
  echo
  echo "   ACD_BIN: ${ACD_BIN}"
  echo "   ACD_ENV: ${ACD_ENV}"
  echo "   ACD_ENV: ${ACD_ENV_BASE}"
  echo
  echo " af_acd_ : activate a working environment "
  echo " af_acd_new_base_ : "
  echo " af_acd_new_env_ : "
  echo " af_acd_del_env_ : "
  echo " "

}

acd(){
  echo " "
  echo " acd_ "
  echo " acd_new_base "
  echo " acd_new_base_ "
  echo " acd_new_env "
  echo " acd_new_env_ "
}

#  $(af_acd)
acd_() {
  eval "$($(which conda) 'shell.bash' 'hook')"
  conda deactivate; conda activate ${ACD_ENV};
  conda activate ${ACD_ENV}
}


# echo "# conda create --name base38 --clone base"
acd_new_base() {
  eval "$($(which conda) 'shell.bash' 'hook')"
  conda create --name ${ACD_ENV_BASE}
}

acd_new_base_() {
  $(acd_new_base)
}

acd_new_env(){
  echo "conda create --name ${ACD_ENV} --clone ${ACD_ENV_BASE}"
}

acd_new_env_(){
  $(acd_new_env)
}

acd_del_env(){
  echo "conda env remove --name ${ACD_ENV}"
}

acd_del_env_(){
  $(acd_del_env)
}



#
# [] setup
#
af_setup() {
  echo " "
  echo " AIRFLOW_HOME : $AIRFLOW_HOME"
  echo " AF_HOME:     : $AF_HOME"
  echo " af_home      : $af_home"

  echo " "
  echo " af_setup_new "
  echo " af_setup_pip "
  echo " af_setup_cfg : copy cfg file into AF_HOME "
  echo " af_setup_dag : copy dag dir into AF_HOME "

  echo " "
  echo " af_install_pip_new: pip install "
  echo " af_install_db_init: db init "
  echo " af_install_config: configuration "
  echo " af_install_dag "
  echo " "
  echo " "
  echo " check the af_home directory "
  echo " dags is a soft link to the hom0/dags "
  echo " log directory "
  echo " check the configuration "
  echo " "

}





af_setup_pip(){

  eval "$($(which conda) 'shell.bash' 'hook')"
  conda activate ${ACD_ENV}
  which pip
  echo "ACD_PIP1: "$(wc ${ACD_PIP1})
  echo "ACD_PIP5: "$(wc ${ACD_PIP5})
}

af_setup_pip_(){

  eval "$($(which conda) 'shell.bash' 'hook')"
  conda activate ${ACD_ENV}
  which pip
  pip install -r ${ACD_PIP1}
  pip install -r ${ACD_PIP5}
}




#
# [] installation
# https://airflow.apache.org/docs/apache-airflow/stable/start.html
af_setup_pip__backup(){

  AIRFLOW_VERSION=2.6.3

  # Extract the version of Python you have installed. If you're currently using Python 3.11 you may want to set this manually as noted above, Python 3.11 is not yet supported.
  PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

  CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
  # For example this would install 2.6.3 with python 3.7: https://raw.githubusercontent.com/apache/airflow/constraints-2.6.3/constraints-3.7.txt

  pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
}

af_setup_home() {
  which airflow
  du -sh ${AIRFLOW_HOME}
  echo "rm -rf ${AIRFLOW_HOME} && mkdir ${AIRFLOW_HOME}"

}

af_setup_home_(){
  rm -rf ${AIRFLOW_HOME} && mkdir ${AIRFLOW_HOME}
}


#
# [] configuration
#
af_setup_db(){
  echo airflow db migrate
}
af_setup_db_(){
  $(af_setup_db)
}

af_setup_db_checking (){
  echo -n ' airflow : ' && which airflow
  echo -n ' af_cfg  : ' && echo ${af_cfg}
  echo -n ' AIRFLOW_CFG : ' && echo ${AIRFLOW_CFG}
  du -sh ${AIRFLOW_HOME}
}





af_setup_user_admin() {
  echo "airflow users create \
    --username admin \
    --firstname admin_first \
    --lastname admin_last \
    --role Admin \
    --password admin \
    --email admin@admin.org
    "
}

af_setup_user_admin_(){
  $(af_setup_user_admin)
}


af_setup_user_guest(){
echo "airflow users create \
    --username guest \
    --firstname guest_f \
    --lastname guest_l \
    --role Public \
    --password guest \
    --email guest@guest.org"

}

af_setup_user_guest_(){
  $(af_setup_user_guest)
}


af_setup_user__listing(){
  echo "airflow users list"
}

af_setup_user__listing_(){
  $(af_setup_user__listing)
}




#
# [] configuration
#
#
#  Number of seconds after which a DAG file is parsed. The DAG file is parsed every
# ``min_file_process_interval`` number of seconds. Updates to DAGs are reflected after
# this interval. Keeping this number low will increase CPU usage.
# min_file_process_interval = 10

# How often (in seconds) to scan the DAGs directory for new files. Default to 5 minutes.
# dag_dir_list_interval = 60

# Whether to load the DAG examples that ship with Airflow. It's good to
# get started, but you probably want to set this to ``False`` in a production
# environment
# load_examples = True
#
#
# To deactivate the authentication and allow users to be identified as Anonymous, the following entry in $AIRFLOW_HOME/webserver_config.py needs to be set with the desired role that the Anonymous user will have by default:
# AUTH_ROLE_PUBLIC = 'Admin'
#
#
#
af_setup_cfg(){
  echo
  echo " AIRFLOW_CFG : $AIRFLOW_CFG "
  echo " AF_CFG    : $AF_CFG "
  echo " af_cfg    : $af_cfg "
  echo
  echo " Config    : "
  echo "   min_file_process_interval = 3  : "
  echo "   dag_dir_list_interval = 30     : "
  echo "   load_examples = False          : "
  echo "   AUTH_ROLE_PUBLIC = 'Admin' : "
  echo "   max_tis_per_query : 0 so core.parallelism is used "
  echo
  wc $af_cfg
  wc $AF_CFG
  diff $af_cfg $AF_CFG
}
af_setup_cfg_(){
  echo "cp $af_cfg $AF_CFG"
  echo "  |- af_cfg : $af_cfg "
  echo "  |- AF_CFG : $AF_CFG "
  cp $af_cfg $AF_CFG
}

af_setup_dag(){
  echo
  echo "af_dag : $af_dag"
  echo "AF_DAG : $AF_DAG"
  echo
  echo "cp -rf $af_dag $AF_DAG"
  du -sh $af_dag
  du -sh $AF_DAG
}
af_setup_dag_(){
  cp -rf $af_dag $AF_DAG
}

af_setup_log(){
  echo "af_log : $af_log "
  echo "AF_LOG : $AF_LOG "
  du -sh $AF_LOG
}

af_setup_log_(){
  rm -rf $AF_LOG && mkdir $AF_LOG
}


#
# Connection
# 35 | oracle_default
#
af_setup_con(){
  echo "airflow connections list"
}

af_setup_con_(){
  $(af_exe_con)
}


af_setup_con_add(){
  echo "airflow connections add "
}


af_setup_con_add1(){
    echo " airflow connections add ${AF_CON1_ID} \
--conn-type ${AF_CON1_TYPE} \
--conn-login ${AF_CON1_LOGIN} \
--conn-password ${AF_CON1_PASS} \
--conn-host ${AF_CON1_HOST} \
--conn-port ${AF_CON1_PORT} \
--conn-schema ${AF_CON1_SCHEMA} "
}


af_setup_con_add1_(){
  $(af_con_add1)
}

af_setup_con_add1_get(){
  echo "airflow connections get ${AF_CON1_ID} "
}

af_setup_con_add1_get_(){
  $(af_con_add1_get)
}


af_setup_con_add2(){
    echo " airflow connections add ${AF_CON2_ID} \
--conn-type ${AF_CON2_TYPE} \
--conn-login ${AF_CON2_LOGIN} \
--conn-password ${AF_CON2_PASS} \
--conn-host ${AF_CON2_HOST} \
--conn-port ${AF_CON2_PORT} \
--conn-schema ${AF_CON2_SCHEMA} "
}

af_setup_con_add2_(){
  $(af_con_add2)
}

af_setup_con_add2_get(){
  echo "airflow connections get ${AF_CON2_ID} "
}

af_setup_con_add2_get_(){
  $(af_con_add2_get)
}


af_setup_misc_dot(){
  which dot
}

af_setup_misc_dot_(){
  $(af_setup_dot)
}



#
# [] run
#
af_start(){
  echo " "
  echo " af_start:"
  echo " |- af_start_sch : starging airflow "
  echo " |_ af_start_web : airflow webserver --port $AIRFLOW_PORT"
  echo
}

af_start_sch(){
  eval "$($(which conda) 'shell.bash' 'hook')"
  echo -n "airflow: "
  which airflow
  echo "airflow scheduler"
}

af_start_sch_(){
  eval "$($(which conda) 'shell.bash' 'hook')"
  airflow scheduler &
}

af_start_web(){
  eval "$($(which conda) 'shell.bash' 'hook')"
  which airflow
  echo "airflow webserver --port AIRFLOW_PORT"
}

af_start_web_(){
  eval "$($(which conda) 'shell.bash' 'hook')"
  airflow webserver --port $AIRFLOW_PORT 1>
}


AF() {
    echo
    echo "AIRFLOW_HOME : $AIRFLOW_HOME"
    echo "     AF_HOME : $AF_HOME"
    echo "     AF_LOG  : $AF_LOG"
    echo "     AF_CFG  : $AF_CFG"
    echo "     AF_DAG  : $AF_DAG"
    echo
}

#
# airflow id
#
#export af_uid=n4af8




# SCHEDULER
# export af_sd=$HOME
# UI
# export af_ui_user="admin"
# export af_ui_pass="pass"






#
#
#
export af__vsc=$HOME/d2/s3/m8/vsc/n4af/$af_uid
export af__home=$af__vsc/${af_uid}home0
export af__dag=$af__vsc/dags
export af__cfg=$af__vsc/airflow.cfg
export af__cfg_ui=$af__vsc/webserver_config.cfg
export af__charm=$af__vsc/${af_uid}home0charm


#
# test
#
export af_tst_url=https://github.com/godatadriven/airflow-testing-examples



#
# ENV VAR
#
#af_src_(){     echo "source ~/.bash_af" }
#af_src__(){    source ~/.bash_af }
#alias af_src_-=``
#
af(){
    echo
    echo   ANACONDA
    echo    ACD_ENV    : $ACD_ENV
    echo    ACD_BIN    : $ACD_BIN
    echo
}

af_home_cd(){
  echo "cd ${af_home}"
}

# alias af_cd="cd $af_home"
af_home_cd_(){
  $(af_home_cd)
}

af_cfg_lst(){
  echo "airflow config list"
}

af_cfg_lst_(){
  $(af_cfg_lst)
}



#
#
#
af_exe_help(){
  echo
  echo af_ops  : $af_ops
  echo af_home : $af_home
  echo af_house : $af_house
  echo  af_log  : $af_log
  echo  af_dag  : $af_dag
  echo
  echo  af_src_  : source ~/.bash_af
  echo  af_acd_  : deactivate and activate conda env
  echo
  echo  af_cfg: $af_cfg
  echo  af_db:  $af_db
  echo  af_sch: scheduler: $af_sd
  echo  af_ui: $af_ui
  echo   localhost:8080/home
  echo   USER: $af_ui_user
  echo   PASS: $af_ui_pass

}

af_exe_help_(){

    echo af__vsc     : $af__vsc
    echo af__home    : $af__home
    echo af__dag     : $af__dag
    echo af__cfg     : $af__cfg
    echo af__cfg_ui  : $af__cfg_ui
    echo af__charm   : $af__charm

}
#alias af__-=`echo 'cd af_home' && cd $af__home`



af_exe_info(){
  echo "airflow info"
}
af_exe_info_(){
  $(af_info)
}

af_exe_ver(){
  echo "airflow version"
}

af_exe_ver_(){
  $(af_ver)
}


#
#
#
af_log(){
  find $AF_LOG/* -name "*log" | xargs wc -l
}

af_log_(){
  find $AF_LOG/* -name "*log" | xargs wc -l
}

af_log_reset(){
  #echo "rm -rf $AF_LOG && mkdir $AF_LOG "
  echo "rm -rf ${AF_LOG}"
}

af_log_reset_(){
  $(af_log_reset)
}



af_dag(){
  echo
  echo "af_dag:"
  echo "  af_dag_list"
  echo "  af_dag_list_job"
  echo "  af_dag_list_run"
  echo "  af_dag_list_err"
  echo
}

af_dag_report(){
  echo "airflow dags report"
}

af_dag_report_(){
  $(af_dag_report)
}

af_dag_list(){
  echo "airflow dags list"
}

af_dag_list_(){
  $(af_dag_list)
}

af_dag_list_job(){
  echo "airflow dags list-jobs"
}

af_dag_list_job_(){
  $(af_dag_list_job)
}

af_dag_list_run(){
  echo "airflow dags list-runs"
}

af_dag_list_run_(){
  $(af_dag_list_job)
}


af_dag_list_err(){
  echo "airflow dags list-import-errors"
}



af_dag_trigger(){
  echo
  echo
  echo "af_dag_trigger1 : ${af_dag_id}"
  echo
}

# echo ""
af_dag_trigger1(){
  echo "airflow dags trigger --run-id ${af_dag_id}_$(date +"%m_%d_%Y_%H_%M_%S") ${af_dag_id} "
}

af_dag_trigger1_(){
  $(af_dag_trigger1_unpause)
  $(af_dag_trigger1)
}

af_dag_trigger1_pause(){
  echo " airflow dags pause ${af_dag_id} "
}

af_dag_trigger1_pause_(){
  $(af_dag_trigger1_unpause)
}

af_dag_trigger1_unpause(){
  echo " airflow dags unpause ${af_dag_id} "
}

af_dag_trigger1_unpause_(){
  $(af_dag_trigger1_unpause)
}

af_dag_trigger1_details(){
  echo "airflow dags details ${af_dag_id}"
}

af_dag_trigger1_details_(){
  $(af_dag_trigger1_details)
}

#   find $AF_LOG -type d -name "${af_dag_id}"
af_dag_trigger1_log(){
  #find $AF_LOG -name "*${af_dag_id}*"
  echo "find $AF_LOG -type d -or -type f -name '*${af_dag_id}*'"
  #find $AF_LOG -type d -or -type f -name "*dag_id=${af_dag_id}*"
}

af_dag_trigger1_log_(){
  echo AF_LOG     : $AF_LOG
  echo af_dag_uid : $af_dag_uid
  $(af_dag_trigger1_log)
}

af_dag_trigger1_log_reset(){
  echo "rm -rf $AF_LOG"
}

af_dag_trigger1_log_reset_(){
  $(af_dag_trigger1_log_reset)
}



af_dag_tst(){
  echo
  echo " af_dag_tst    : "
  echo " af_dag_tst_hw : $af_dag_uid"
}


# airflow dags test dag_id_here 2021-11-10T14:20:00Z
af_dag_tst_hw(){
  echo "airflow dags test  --save-dagrun $AF_LOG/${af_dag_uid}.dot --show-dagrun $af_dag_uid"
}

af_dag_tst_hw_(){
  $(af_dag_tst_hw)
}

af_dag_tst_hw_log(){
  find $AF_LOG -name "${af_dag_uid}"
}

af_dag_tst_hw_log_(){
  $(af_dag_tst_hw_log)
}



# run a backfill over 2 days
#airflow dags backfill example_bash_operator \
#    --start-date 2015-01-01 \
#    --end-date 2015-01-02
#
#
#
af_dag_backfill(){

  date_start='2015-06-01'
  date_end='2015-06-07'

  echo " airflow dags backfill tutorial \
  --start-date $date_start \
  --end-date $date_end "
}


#
#
#
af_task(){
  echo "airflow tasks list"
}

af_task_list(){
  tmp_dag_id='tutorial'
  echo "airflow tasks list ${tmp_dag_id}"
}

af_task_test(){
  echo "airflow tasks test ${tmp_dag_id} "
}


# run your first task instance
#airflow tasks test example_bash_operator runme_0 2015-01-01
# command layout: command subcommand [dag_id] [task_id] [(optional) date]
af_test(){
  tmp_dag_id="tutorial"
  tmp_task_id="templated"
  tmp_date="2023-01-01"
  echo " airflow tasks test " ${tmp_dag_id}" "${tmp_task_id}" "${tmp_date}
}

af_test_(){
  airflow
}



af_role_list(){
  echo "airflow roles list"
}

af_role_create(){
  role_new_name="dev"
  echo "airflow roles create $role_new_name"
}

af_role_delete(){
  role_new_name="dev"
  echo "airflow roles create $role_new_name"
}

af_role_perm_add(){
  echo "airflow roles "
}

af_role_perm_del(){
  echo "airflow roles "
}


#
#
#
af_template(){
  echo $FUNCNAME[0]
  echo
  echo " af_uid"
  echo " source ~/.bash_af "
  echo " wc ~/.bash_af.md "
  echo
}


#af_run(){ which airflow }
#af_run_hw23a(){ echo "airflow run ${af_dag_uid} ${af_task_uid}" }3
#af_run_hw23a_(){ $(af_run_hw23a) }







# https://stackoverflow.com/questions/44360354/airflow-unpause-dag-programmatically
# https://stackoverflow.com/questions/65059259/debugging-airflow-tasks-using-airflow-test-vs-using-debugexecutor
#
# command layout: command subcommand dag_id task_id date
#
## testing print_date
#airflow test tutorial print_date 2015-06-01
#
## testing sleep
#airflow test tutorial sleep 2015-06-01
#
# Oracle HOOk
# https://stackoverflow.com/questions/36945811/how-to-connect-airflow-to-oracle-database
#

