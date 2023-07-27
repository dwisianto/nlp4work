

#
#
#
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

import dash
import dash_bootstrap_components as dbc

from my_cfg import MyConfigObject, my_log


def create_app():
    server = Flask(__name__, template_folder="template/t2")
    server.config.from_object(MyConfigObject)
    server.testing = True #return a test_client inside a pytest case

    # [] logging
    server.logger.addHandler(my_log)
    server.logger.info("create_app")
   
    # [] extension
    register_extensions(server)
    register_blueprints(server)
    register_board0(server)
    register_board1(server)
    register_board2(server)
    register_board3(server)

    return server




def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate
    from app.extensions import bootstrap

    server.logger.info("registering_extension")
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

# Meta tags for viewport responsiveness
_meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}


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

    _protect_dashviews(board0)


def register_board1(app):
    from app.board.b1.layout import layout
    from app.board.b1.callbacks import register_callbacks

    board1_name='board1'
    board1 = dash.Dash(__name__,
                        server=app,
                        url_base_pathname='/'+board1_name+'/',
                        assets_folder=get_root_path(__name__) + '/'+board1_name+'/assets/',
                        meta_tags=[_meta_viewport],
                        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    with app.app_context():
        board1.title = board1_name
        board1.layout = layout
        register_callbacks(board1)

    _protect_dashviews(board1)




def register_board2(app):

    from app.board.b2.layout import layout
    from app.board.b2.callbacks import register_callbacks

    board2_name='board2'
    board2 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/'+board2_name+'/',
                         assets_folder=get_root_path(__name__) + '/'+board2_name+'/assets/',
                         meta_tags=[_meta_viewport],
                         external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    with app.app_context():
        board2.title = board2_name
        board2.layout = layout
        register_callbacks(board2)

    _protect_dashviews(board2)


def register_board3(app):

    from app.board.b3.layout import layout
    from app.board.b3.callbacks import register_callbacks

    board_name='board3'
    board = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/'+board_name+'/',
                         assets_folder=get_root_path(__name__) + '/'+board_name+'/assets/',
                         meta_tags=[_meta_viewport],
                         external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    with app.app_context():
        board.title = board_name
        board.layout = layout
        register_callbacks(board)

    _protect_dashviews(board)
