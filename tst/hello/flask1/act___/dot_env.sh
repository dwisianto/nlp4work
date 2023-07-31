
#
#
#
echo "ENV VARS:"

#
#
#
#export MY_BASH="/opt/homebrew/Cellar/bash/5.2.9/bin/bash"
export MY_BASH=""
export MY_CONDA=$(which conda)
export MY_CONDA_ENV='web904a'
export MY_ENV=${MY_CONDA_ENV}
echo "MY_BASH ${MY_BASH}"
echo "MY_CONDA ${MY_CONDA}"
echo "MY_CONDA_ENV ${MY_CONDA_ENV}"

#
#
#
export MY_DATA=$HOME/d/db
export MY_DAT=$MY_DATA
echo MY_DATA: $MY_DATA
echo MY_DAT: $MY_DAT

export PYTHONPATH=$PWD:$PYTHONPATH
echo PYTHONPATH: $PYTHONPATH
