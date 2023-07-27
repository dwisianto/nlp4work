
# 2023-07-26 flask login with a timeout feature

- https://stackoverflow.com/questions/11783025/is-there-an-easy-way-to-make-sessions-timeout-in-flask

# 2023-07-25 logging

- 
- https://stackoverflow.com/questions/46466408/flask-properly-configure-logging
- https://github.com/geoHeil/flask_logging_question
- gunicorn-logging
- https://trstringer.com/logging-flask-gunicorn-the-manageable-way/

# 2023-07-22 

- https://community.plotly.com/t/using-dash-in-flask-app-extend-base-html-using-jinja2/43298
- https://community.plotly.com/t/how-to-connect-flask-wtf-form-responses-to-a-plotly-dash-dashboard/22162

## Form

- https://pypi.org/project/json-schema-to-dash-forms/
- https://community.plotly.com/t/adding-form-to-dash-app/12698/7
- https://github.com/plotly/dash/issues/308



# 2023-07-21

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- flask.shell

```
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
```

## 2023-07-18
- Reading sqlite with sqlalchemy
- https://realpython.com/python-sqlite-sqlalchemy/
- https://stackoverflow.com/questions/58896928/how-to-connect-to-sqlite-from-sqlalchemy

## 2023-07-14
- sqlalchemy and oracle
- https://stackoverflow.com/questions/28453545/connecting-to-an-oracle-database-using-sqlalchemy

## 2023-07-13
- flask https://bootstrap-flask.readthedocs.io/en/stable/
- https://stackoverflow.com/questions/53945371/python-flask-before-first-request-funcs
 
## 2023-07-10
- ln -s app___/my_env.sh ./.flaskenv