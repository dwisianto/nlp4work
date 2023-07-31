export FLASK_APP=my_app
#export FLASK_ENV=development
export FLASK_DEBUG=1
export DATABASE_URL=sqlite:///${PWD}/my_app.sqlite
export SECRET_KEY=my_secret

echo FLASK_APP: $FLASK_APP
echo FLASK_DEBUG: $FLASK_DEBUG
echo SECRET_KEY: $SECRET_KEY
echo DATABASE_URL: $DATABASE_URL