from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuration settings
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_name = 'flask'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from app.models import User
from app import routes