from application import app, database, bcrypt
from flask import redirect, render_template, url_for, flash
from application.forms import FormLogin, FormCadastro, FormCadastroSUS
from application.models import Usuario, UsuarioSUS
from flask_login import login_user, logout_user, login_required



@app.route("/", methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nome=form.usuario.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user)
            flash(f'Login feito com sucesso para o user: {form.usuario.data}', 'alert alert-success')
            return redirect(url_for('exibir_usuarios'))
        elif form.validate_on_submit():
            user1 = UsuarioSUS.query.filter_by(nome=form.usuario.data).first()
            print(user1)
            if user1 and bcrypt.check_password_hash(user1.senha, form.senha.data):
                login_user(user1)
                flash(f'Login feito com sucesso para o user: {form.usuario.data}', 'alert alert-success')
                return redirect(url_for('exibir_usuarios'))
            else:
                flash(f'Usuário ou senha inválidos', 'alert alert-danger')
    return render_template('index.html', form=form)

@app.route("/sair")
@login_required
def sair():
    logout_user()
    flash('Sessão encerrada', 'alert alert-info')
    return redirect(url_for('login'))

@app.route("/lista_usuarios")
@login_required
def exibir_usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template('doadores.html', lista_usuarios=lista_usuarios)

@app.route("/cadastrar_usuario", methods=['GET', 'POST'])
def cadastro_usuario():
    form = FormCadastro()
    if form.validate_on_submit():
        senha_crypto = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        try:
            user = Usuario(nome=form.nome.data, email=form.email.data, senha=senha_crypto, telefone=form.telefone.data, tiposanguineo=form.tipoSanguineo.data)
            database.session.add(user)
            database.session.commit()
            return redirect(url_for('login'))
        except:
            flash('Cadastro não completado com sucesso', 'alert alert-danger')
    return render_template('cadastro.html', form=form)
@app.route("/cadastrar_sistema_saude", methods=['GET', 'POST'])
def cadastro_SUS():
    form1 = FormCadastroSUS()
    if form1.validate_on_submit():
        senha_crypto = bcrypt.generate_password_hash(form1.senha.data).decode('utf-8')
        try:
            user1 = UsuarioSUS(nome=form1.nome.data, cnpj=form1.cnpj.data, senha=senha_crypto)
            database.session.add(user1)
            database.session.commit()
            return redirect(url_for('exibir_usuarios'))
            flash('Cadastro completado com sucesso, agora poderá ver uma lista de possíveis doadores o qual poderá entrar em contato', 'alert alert-success')
        except:
            flash('Cadastro não completado com sucesso', 'alert alert-danger')
    return render_template('cadastroSUS.html', form1=form1)

