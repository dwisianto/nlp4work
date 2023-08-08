
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap4()