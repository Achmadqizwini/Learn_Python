from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

apps = Flask(__name__)
apps.config.from_object(Config)

db = SQLAlchemy(apps)
migrate = Migrate(apps, db)

from app import routes, models