from flask import Flask

from app.config import Config

from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Setup nameing conventions for constraints in database
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app,db,render_as_batch=True)

# Initialise login manager
login = LoginManager(app)
login.login_view = 'auth.login'

# Include all modules
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

#from app.admin import bp as admin_bp
#app.register_blueprint(admin_bp, url_prefix="/admin")

from app.main import bp as main_bp
app.register_blueprint(main_bp)

# At last import the db structure
from app import models
