from time import strftime
from datetime import datetime
from casadojulgamento import app, database, bcrypt
from flask import render_template, request, flash, url_for, redirect
import secrets

from casadojulgamento.forms import ParticipanteForm, ListarParticipantesForm
from casadojulgamento.models import Participante


@app.route("/")
def home():
    quantidade_total = Participante.query.count()
    quantidade_cristaos = Participante.query.filter_by(membro_igreja="Sim").count()
    quantidade_nao_cristaos = Participante.query.filter_by(membro_igreja="Não").count()
    percentual_cristaos = (quantidade_cristaos / quantidade_total) * 100
    percentual_nao_cristaos = (quantidade_nao_cristaos / quantidade_total) * 100
    return render_template("home.html", quantidade_total=quantidade_total, quantidade_cristaos=quantidade_cristaos, quantidade_nao_cristaos= quantidade_nao_cristaos, percentual_cristaos= percentual_cristaos, percentual_nao_cristaos = percentual_nao_cristaos)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form_cadastro = ParticipanteForm()

    quantidade = 0

    if form_cadastro.validate_on_submit():
        data = form_cadastro.data.data
        horario = form_cadastro.horario.data
        print(data)
        grupo = data + horario
        quantidade = Participante.query.filter_by(grupo=grupo).count()
        if form_cadastro.membro_igreja.data:
            membro_igreja = "Sim"
        else:
            membro_igreja = "Não"

        if quantidade < 15:
            participante = Participante(nome=form_cadastro.nome.data, membro_igreja=membro_igreja, horario=horario, grupo=grupo)
            database.session.add(participante)
            database.session.commit()
            quantidade = Participante.query.filter_by(grupo=grupo).count()
            flash('Cadastro realizado com sucesso', 'alert-success')

        #return redirect(url_for("cadastro", horario=horario))
        elif  quantidade >= 15:
            flash('O grupo não pode ter mais de 15 participantes.', 'alert-danger')

    return render_template("cadastro.html", form_cadastro=form_cadastro, quantidade=quantidade)


@app.route('/participantes', methods=['GET', 'POST'])
def participantes():
    form_listar = ListarParticipantesForm()
    grupo=""
    horario = request.args.get('horario')
    data = request.args.get('data')

    if request.method == "GET":
        form_listar.horario.data = horario
        form_listar.data.data = data

    if form_listar.validate_on_submit():
        horario = form_listar.horario.data
        data = form_listar.data.data
        grupo = data + horario

    participantes = Participante.query.filter_by(grupo=grupo).all()

    return render_template('participantes.html', participantes=participantes, grupo=grupo, form_listar=form_listar)


@app.route('/editar/<participante_id>', methods=['GET', 'POST'])
def editar(participante_id):
    form_cadastro = ParticipanteForm()
    participante = Participante.query.get(participante_id)

    horario_participante = participante.horario
    grupo = participante.grupo
    quantidade = Participante.query.filter_by(grupo=grupo).count()
    data = participante.grupo[0:10]

    if request.method == "GET":
        form_cadastro.nome.data = participante.nome
        form_cadastro.horario.data = participante.horario
        form_cadastro.data.data = participante.grupo[0:10]
        if participante.membro_igreja == "Sim":
            form_cadastro.membro_igreja.data = True
        else:
            form_cadastro.membro_igreja.data = False

    elif form_cadastro.validate_on_submit() and 'botao_submit' in request.form:

        horario_novo = form_cadastro.horario.data
        data = form_cadastro.data.data
        grupo_novo = data + horario_novo
        quantidade = Participante.query.filter_by(grupo=grupo_novo).count()

        participante.nome = form_cadastro.nome.data
        membro_igreja = ""
        if form_cadastro.membro_igreja.data:
            membro_igreja = "Sim"
        else:
            membro_igreja = "Não"
        participante.membro_igreja = membro_igreja
        participante.horario = horario_novo
        participante.grupo = grupo_novo
        participante.data = datetime.now()
        if quantidade >= 15 and grupo_novo != grupo:
            flash('O grupo não pode ter mais de 15 participantes.', 'alert-danger')
        else:
            database.session.commit()
            flash('Cadastro alterado com sucesso', 'alert-success')
            return redirect(url_for("participantes", horario=horario_novo, data=data))
    else:
        return redirect(url_for("participantes", horario=horario_participante, data=data))



    return render_template('editar.html', quantidade=quantidade, participante=participante, form_cadastro=form_cadastro)


@app.route('/editar/<participante_id>/excluir', methods=['GET', 'POST'])
def excluir(participante_id):

    participante = Participante.query.get(participante_id)
    print(participante)
    horario = participante.horario
    data = participante.grupo[0:10]

    database.session.delete(participante)
    database.session.commit()
    flash('Excluído com sucesso', 'alert-success')

    return redirect(url_for('participantes', horario=horario, data=data))