from wtforms import StringField
from wtforms.validators import DataRequired
from casadojulgamento import database
from datetime import datetime

class Participante(database.Model):
    id = database.Column('id', database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    membro_igreja = database.Column(database.String, nullable=False)
    data = database.Column(database.DateTime, nullable=False, default=datetime.now)
    horario = database.Column(database.String, nullable=False)
    grupo = database.Column(database.String, nullable=False)
