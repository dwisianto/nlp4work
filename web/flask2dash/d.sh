#!/bin/bash




install(){

    ACD_UID=b39fl1
    conda create --name ${ACD_UID} python=3.9
  
    pip install -r requirements.txt
    which flask

    source dot_env  
    
    pip uninstall numpy
    pip install numpy

    flask db init
    flask db migrate -m 'init'
    flask db upgrade

    flask run

}

main(){
    clean "$@"
}

main "$@"

# This is a standard setup with most Flask applications. 
# Steps and code on how to implement the infrastructure used in my repo are adapted directly from the excellent Flask Mega Tutorial by Miguel Grinberg.
# a Flask app which uses:
#  -  the application factory pattern and blueprints
#  -  a database to manage users (sqlite with Flask-SQLAlchemy and Flask-Migrate)
#  -  authentication (Flask-Login)

# 