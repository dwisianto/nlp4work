
export ACD_ENV=p9net8
export ACD_BIN=$(which conda)


export FLASK_APP=my_app
#export FLASK_ENV=development
export FLASK_DEBUG=1
export DATABASE_URL=sqlite:///${PWD}/act_ui/my_app.sqlite
export SECRET_KEY=my_secret
export PYTHONPATH=${PWD}:$PYTHONPATH

export SEED_XLSX='my_app.xlsx'
export SEED_XLSX_FULL_PATH=${PWD}/act_ui


echo 
echo ACD_BIN: ${ACD_BIN}
echo ACD_ENV: ${ACD_ENV}
echo
echo SEED_XLSX: ${SEED_XLSX}
echo SEED_FULL_PATH: ${SEED_FULL_PATH}
echo 
echo FLASK_APP: ${FLASK_APP}
echo FLASK_DEBUG: ${FLASK_DEBUG}
echo SECRET_KEY: ${SECRET_KEY}
echo DATABASE_URL: ${DATABASE_URL}
echo
echo PYTHONPATH: ${PYTHONPATH}
echo
