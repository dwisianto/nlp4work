
#
#
#
echo "ENV VARS:"

#
#
#
MY_BASH="/opt/homebrew/Cellar/bash/5.2.9/bin/bash"
MY_CONDA=$(which conda)
echo "MY_BASH ${MY_BASH}"
echo "MY_CONDA ${MY_CONDA}"

#
#
#
export MY_DATA=$HOME/d/db
export MY_DAT=$MY_DATA
echo MY_DATA: $MY_DATA
echo MY_DAT: $MY_DAT

