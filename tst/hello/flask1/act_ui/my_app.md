
# 20230-07-28

- https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates

# 2023-07-27 Flask & Dash Front-End

- https://github.com/bw984/Flask-Dash-App-Factory-Template 

## Etc

- https://bootstrap-flask.readthedocs.io/en/stable/
- https://dash-bootstrap-components.opensource.faculty.ai/
- https://github.com/tzelleke/flask-dash-app/blob/master/app/templates/index.html
- https://github.com/naderelshehabi/dash-flask-login/tree/main
- https://stackoverflow.com/questions/59627976/integrating-dash-apps-into-flask-minimal-example

## Backup


```
def register_board0(app):
    from app.board.b0.layout import layout
    from app.board.b0.callbacks import register_callbacks

    board0_name='board0'
    board0 = dash.Dash(__name__,
                        server=app,
                        url_base_pathname='/'+board0_name+'/',
                        assets_folder=get_root_path(__name__) + '/'+board0_name+'/assets/',
                        meta_tags=[_meta_viewport],
                        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    with app.app_context():
        board0.title = board0_name
        board0.layout = layout
        register_callbacks(board0)
```



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