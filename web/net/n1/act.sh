#!/bin/bash

source act___/dot_env.sh

#
# information
#
help(){
    arg='act.sh'
    if [ "$#" -ne 1 ]
    then
	    echo
	    echo " USAGE: "
	    echo "   ./${arg}    OPTION"
	    echo "   bash ${arg} OPTION"
	    echo " "
	    echo " OPTION: "
	    echo "     anaconda: acd, acd-save, acd-load"
	    echo "     pytest  : tst, tst-, tst-info, tst-info-, tst-path "
	    echo "     clean   : clean, clean-"
	    echo " "
	    echo " TEST: "
	    echo "   ./${arg}    tst"
	    echo "   bash ${arg} tst-"
	    echo
	    exit 1
    fi
}

clean(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      find ./ -name "*~"
      find ./ -name ".pytest_cache"
      find ./ -name "__pycache__"
      ;;
    ${arg}- )
      find ./ -name "*~" -delete
      find ./ -name ".pytest_cache" -exec rm -rf {} \;
      find ./ -name "__pycache__" -exec rm -rf {} \;
      ;;
  esac
}

acd_env='web904a'
acd_env_file=${acd_env}'.yml'
acd(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      eval "$($(which conda) 'shell.bash' 'hook')"
      conda activate ${acd_env}
      echo -n "acd_env : ${acd_env}"
      echo -n "conda   : " && which conda 
      echo -n "pip     : " && which pip 
      echo -n "python  : " && which python 
      echo -n "pytest  : " && which pytest 
      echo
      ;;
    ${arg}- )
      echo -n "arg      : " && echo ${arg}
      ;;
  esac
}


acd_list(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      echo -n " arg      : " && echo ${arg}
      echo -n "conda env list: "
      conda env list
      ;;
    ${arg}- )
      echo -n "arg      : " && echo ${arg}
      echo ${arg}
      ;;
  esac
}





acd_save(){
  arg=${FUNCNAME[0]}

  out_name='req.tmp.yml'
  case "$@" in
    ${arg} )
      echo -n " arg       : " && echo ${arg}
      echo -n " out_name : " && echo ${out_name}
      echo -n " out file : " && [ -f ${out_name} ] && echo " exists " && echo " missing "
      [ -f ${out_name} ] ||  echo 'conda env export --from-history > req.tmp.yml'
      ;;
    ${arg}- )
      echo -n "arg      : " && echo ${arg}
      conda env export --from-history > req.tmp.yml
      ;;
  esac
}


acd_load(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      echo -n " arg       : " && echo ${arg}
      echo -n " out_name : " && echo ${out_name}
      echo -n " out file : " && [ -f ${out_name} ] && echo " exists " || echo " missing "
      [ -f ${out_name} ] && echo 'conda env create --name myEnv --file=req.tmp.yml' || echo ' ${out_name} is needed'
      ;;
    ${arg}- )
      echo -n " arg      : " && echo ${arg}
      ;;
  esac
}







tst(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      eval "$($(which conda) 'shell.bash' 'hook')"
      conda activate ${acd_env}
      which pytest
      pytest --collect-only
      ;;
    ${arg}- )
      eval "$($(which conda) 'shell.bash' 'hook')"
      conda activate ${acd_env}
      pytest
      ;;
  esac
}

tst_info(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      echo python act/actions.py info
      ;;
    ${arg}- )
      python act/actions.py info
      ;;
  esac
}


tst_path(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      echo " python conftest.py"
      ;;
    ${arg}- )
      python conftest.py
      ;;
  esac
}


template(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
      echo -n "arg      : " && echo ${arg}
      ;;
    ${arg}- )
      echo -n "arg      : " && echo ${arg}
      ;;
  esac
}



main(){
    arg=${FUNCNAME[0]}

    help "$@"
    clean "$@"

    acd "$@"
    acd_list "$@"
    acd_save "$@"
    acd_load "$@"

    tst "$@"
    tst_info "$@"
    tst_path "$@"

}
main "$@"
