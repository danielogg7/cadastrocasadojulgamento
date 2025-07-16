from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

# if os.getenv('DATABASE_URL'):
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casadojulgamento.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Jesus28xp!@cadastrocj.cxqymaayqcnu.us-east-2.rds.amazonaws.com:3306/cadastrocj'

app.config['SECRET_KEY'] = '06f8b60c12dfb8105f0b51e54ff28dfc'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from casadojulgamento import routes