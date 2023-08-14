from app import create_app

server = create_app()


#
#
#
# export FLASK_APP=my_app.py
# (venv) $ flask shell
# >>> db
# >>> User
# >>> Tale
#
from app.extensions import db
from app.models import User, Tale


@server.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Tale': Tale}
