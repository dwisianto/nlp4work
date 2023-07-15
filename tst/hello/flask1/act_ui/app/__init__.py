
import dash

from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

from my_cfg import BaseConfig


def create_app():
    server = Flask(__name__, template_folder="template/t1")
    server.config.from_object(BaseConfig)
    server.testing = True #return a test_client inside a pytest case

    register_dash1(server)
    register_dash2(server)
    register_extensions(server)
    register_blueprints(server)

    return server




def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate
    from app.extensions import bootstrap

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)
    bootstrap.init_app(server)

def register_blueprints(server):
    from app.routes import server_bp

    server.register_blueprint(server_bp)


#
# Protect any dashboard with a login requirement
#
def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(
                dashapp.server.view_functions[view_func])


def register_dash1(app):
    from app.board.b1.layout import layout
    from app.board.b1.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    board1_name='board1'
    board1 = dash.Dash(__name__,
                        server=app,
                        url_base_pathname='/'+board1_name+'/',
                        assets_folder=get_root_path(__name__) + '/'+board1_name+'/assets/',
                        meta_tags=[meta_viewport])

    with app.app_context():
        board1.title = board1_name
        board1.layout = layout
        register_callbacks(board1)

    _protect_dashviews(board1)




def register_dash2(app):

    from app.board.b2.layout import layout
    from app.board.b2.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
        }

    board2_name='board2'
    board2 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/'+board2_name+'/',
                         assets_folder=get_root_path(__name__) + '/'+board2_name+'/assets/',
                         meta_tags=[meta_viewport])

    with app.app_context():
        board2.title = board2_name
        board2.layout = layout
        register_callbacks(board2)

    _protect_dashviews(board2)
