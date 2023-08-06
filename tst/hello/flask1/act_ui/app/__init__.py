

#
#
#
import os
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

import dash
import dash_bootstrap_components as dbc

from my_cfg import MyConfigObject, my_log


def create_app():

    server = Flask(__name__,
                   template_folder=MyConfigObject.LOC_TEMPLATE,
                   static_folder=MyConfigObject.LOC_STATIC)
    server.config.from_object(MyConfigObject)
    server.logger.addHandler(my_log)
    server.testing = True  # return a test_client inside a pytest case

    # [] extension
    register_extensions(server)

    # [] register dash app
    b0_title = 'Board0'
    from app.board.b0.layout import layout as b0_layout
    from app.board.b0.callbacks import register_callbacks as b0_callbacks
    register_dash_view(flask_server=server,
                       title=b0_title,
                       base_pathname=b0_title.lower()+'0',
                       layout=b0_layout,
                       callback_func_list=[b0_callbacks])

    b1_title = 'Board1'
    from app.board.b1.layout import layout as b1_layout
    from app.board.b1.callbacks import register_callbacks as b1_callbacks
    register_dash_view(flask_server=server,
                       title=b1_title,
                       base_pathname=b1_title.lower()+'0',
                       layout=b1_layout,
                       callback_func_list=[b1_callbacks])

    b2_title = 'Board2'
    from app.board.b2.layout import layout as b2_layout
    from app.board.b2.callbacks import register_callbacks as b2_callbacks
    register_dash_view(flask_server=server,
                       title=b2_title,
                       base_pathname=b2_title.lower()+'0',
                       layout=b2_layout,
                       callback_func_list=[b2_callbacks])

    b3_title = 'Board3'
    from app.board.b3.layout import layout as b3_layout
    from app.board.b3.callbacks import register_callbacks as b3_callbacks
    register_dash_view(flask_server=server,
                       title=b3_title,
                       base_pathname=b3_title.lower()+'0',
                       layout=b3_layout,
                       callback_func_list=[b3_callbacks])

    #register_board0(server)
    #register_board1(server)
    #register_board2(server)
    #register_board3(server)

    # [] blueprint
    register_blueprints(server)

    # []
    server.logger.info(f'Flask Server PID {str(os.getpid())}.')
    return server


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate
    from app.extensions import bootstrap

    server.logger.info("create_app > register_extensions")

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)
    bootstrap.init_app(server)


def register_blueprints(server):
    from app.routes import server_bp

    server.logger.info("create_app > register_blueprints ")

    server.register_blueprint(server_bp)


#
# Protect any dashboard with a login requirement
#
def register_dash_view_and_protect_dash_view(a_dash_view):
    for view_func in a_dash_view.server.view_functions:
        if view_func.startswith(a_dash_view.config.url_base_pathname):
            a_dash_view.server.view_functions[view_func] = login_required(
                a_dash_view.server.view_functions[view_func])


# Meta tags for viewport responsiveness
register_dash_view_with_meta_viewport={
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
}


def register_dash_view(
        flask_server,
        title,
        base_pathname,
        layout,
        callback_func_list):

    from my_cfg import my_debug

    a_dash_view = dash.Dash(
        __name__,
        server=flask_server,
        url_base_pathname=f'/{base_pathname}/',
        assets_folder=get_root_path(__name__) + '/static/',
        meta_tags=[ register_dash_view_with_meta_viewport],
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        # external_scripts=[],
    )

    with flask_server.app_context():
        a_dash_view.title = title
        a_dash_view.layout = layout
        a_dash_view.css.config.serve_locally = True
        a_dash_view.enable_dev_tools(debug=my_debug.dash_debug, dev_tools_hot_reload=my_debug.dash_auto_reload)
        for a_call_back_func in callback_func_list:
            a_call_back_func(a_dash_view)

        register_dash_view_and_protect_dash_view(a_dash_view)
