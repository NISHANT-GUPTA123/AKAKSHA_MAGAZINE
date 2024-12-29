# database.py
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

mysql = MySQL()
db = SQLAlchemy()
migrate = Migrate()