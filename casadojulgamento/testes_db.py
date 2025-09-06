from casadojulgamento import app, database
from casadojulgamento.models import Participante

#with app.app_context():
    #database.create_all()
 #   part = Participante().query.all()
  #  print(part[6].nome)
   # print(part[6].grupo)
    #print(part[6].membro_igreja)
    #print(part[6].horario)
with app.app_context():
    part = Participante.query.filter(Participante.grupo.like('%19/08/2025%'), Participante.membro_igreja=="Sim").count()
    print(part)