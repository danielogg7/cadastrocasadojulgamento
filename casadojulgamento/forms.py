from time import strftime

from flask_wtf import FlaskForm
from sqlalchemy.cyextension.processors import str_to_date
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
from casadojulgamento.models import Participante
from datetime import datetime

class ParticipanteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    membro_igreja = BooleanField('Membro de igreja?')
    horario = SelectField('Horário', choices=['14:00', '14:10', '14:20', '14:30', '14:40', '14:50', '15:00', '15:10', '15:20',
                                   '15:30', '15:40', '15:50', '16:00', '16:10', '16:20', '16:30', '16:40', '16:50',
                                   '17:00', '17:10', '17:20', '17:30', '17:40', '17:50', '18:00', '18:10', '18:20',
                                   '18:30', '18:40', '18:50', '19:00', '19:10', '19:20', '19:30', '19:40', '19:50',
                                   '20:00', '20:10', '20:20', '20:30', '20:40', '20:50', '21:00',
                                   '21:00', '21:10', '21:20', '21:30', '21:40', '21:50','22:00',
                                   '22:00', '22:10', '22:20', '22:30', '22:40', '22:50','23:00',
                                   '23:00', '23:10', '23:20', '23:30', '23:40', '23:50','00:00'])
    if datetime.today().strftime('%Y%m%d') > '20250819' and datetime.today().strftime('%Y%m%d') <= '20250823':
        data = SelectField('Data', choices = ['23/08/2025', '24/08/2025', '30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    elif datetime.today().strftime('%Y%m%d') > '20250823' and datetime.today().strftime('%Y%m%d') <= '20250824':
        data = SelectField('Data', choices=['24/08/2025', '30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    elif datetime.today().strftime('%Y%m%d') > '20250824' and datetime.today().strftime('%Y%m%d') <= '20250830':
        data = SelectField('Data', choices=['30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    elif datetime.today().strftime('%Y%m%d') > '20250830' and datetime.today().strftime('%Y%m%d') <= '20250831':
        data = SelectField('Data', choices = ['31/08/2025'],
                           validators=[DataRequired()])
    else:
        data = SelectField('Data', choices=['19/08/2025', '23/08/2025', '24/08/2025', '30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])

    botao_submit = SubmitField('Enviar')


class ListarParticipantesForm(FlaskForm):
    horario = SelectField('Horário',
                          choices=['14:00', '14:10', '14:20', '14:30', '14:40', '14:50', '15:00', '15:10', '15:20',
                                   '15:30', '15:40', '15:50', '16:00', '16:10', '16:20', '16:30', '16:40', '16:50',
                                   '17:00', '17:10', '17:20', '17:30', '17:40', '17:50', '18:00', '18:10', '18:20',
                                   '18:30', '18:40', '18:50', '19:00', '19:10', '19:20', '19:30', '19:40', '19:50',
                                   '20:00', '20:10', '20:20', '20:30', '20:40', '20:50', '21:00',
                                   '21:00', '21:10', '21:20', '21:30', '21:40', '21:50','22:00',
                                   '22:00', '22:10', '22:20', '22:30', '22:40', '22:50','23:00',
                                   '23:00', '23:10', '23:20', '23:30', '23:40', '23:50','00:00'])
    if datetime.today().strftime('%Y%m%d') > '20250819' and datetime.today().strftime('%Y%m%d') <= '20250823':
        data = SelectField('Data', choices=['23/08/2025', '24/08/2025', '30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    elif datetime.today().strftime('%Y%m%d') > '20250823' and datetime.today().strftime('%Y%m%d') <= '20250824':
        data = SelectField('Data', choices=['24/08/2025', '30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    elif datetime.today().strftime('%Y%m%d') > '20250824' and datetime.today().strftime('%Y%m%d') <= '20250830':
        data = SelectField('Data', choices=['30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    elif datetime.today().strftime('%Y%m%d') > '20250830' and datetime.today().strftime('%Y%m%d') <= '20250831':
        data = SelectField('Data', choices=['31/08/2025'],
                           validators=[DataRequired()])
    else:
        data = SelectField('Data', choices=['19/08/2025', '23/08/2025', '24/08/2025', '30/08/2025', '31/08/2025'],
                           validators=[DataRequired()])
    botao_submit_listar = SubmitField('Listar')