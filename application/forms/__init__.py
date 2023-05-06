from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, email, equal_to, length


class FormLogin(FlaskForm):
    usuario = StringField('login', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit_entrar = SubmitField('Entrar')

class FormCadastro(FlaskForm):
    nome = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])
    telefone = StringField('Telefone', validators=[DataRequired()])
    tipoSanguineo = StringField('Tipo Sanguineo', validators=[DataRequired()])
    submit_cadastrar = SubmitField('Cadastrar')

class FormCadastroSUS(FlaskForm):
    nome = StringField('Nome da Instituição', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired(), length(14,18)])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])

