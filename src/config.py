import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath('.')
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir}/people.db"
# turns the SQLAlchemy event system off
# TODO
# read https://docs.sqlalchemy.org/en/14/core/event.html
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# TODO
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/
ma = Marshmallow(app)