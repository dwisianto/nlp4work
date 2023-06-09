#!/bin/bash

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

ana_env='mine'
ana_env_file=${ana_env}'.yml'
acd(){
  arg=${FUNCNAME[0]}

  case "$@" in
    ${arg} )
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


acd-list(){
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





acd-save(){
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


acd-load(){
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
      pytest --collect-only
      ;;
    ${arg}- )
      pytest
      ;;
  esac
}

tst-info(){
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


tst-path(){
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



act(){
    arg=${FUNCNAME[0]}

    help "$@"
    clean "$@"

    tst "$@"
    tst-info "$@"
    tst-path "$@"

    acd "$@"
    acd-list "$@"
    acd-save "$@"
    acd-load "$@"

}
act "$@"
