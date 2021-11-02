from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.fields.html5 import EmailField
class FormularioIngreso(FlaskForm):
    correo = EmailField(u'Correo', validators=[DataRequired(
        message='** Correo requerido **'), Email()])
    clave = PasswordField(u'Contraseña', validators=[DataRequired(
        message='** Contraseña requerida **'), Length(min=8)])
    privacidad = BooleanField('',validators = [DataRequired(
        message='** Es necesario aceptar la política de privacidad **')])
    enviar = SubmitField(u'Ingresar')

class FormularioUsuario(FlaskForm):
    nombre_usuario = StringField(u'Nombre', validators=[DataRequired(
        message='** Nombre requerido **'), Length(min=10)])
    clave = PasswordField(u'Contraseña', validators=[DataRequired(
        message='** Contraseña requerida **'), Length(min=8)])
    correo = EmailField(u'Correo', validators=[DataRequired(
        message='** Correo requerido **'), Email()])
    rol = SelectField(u'Rol', validators=[DataRequired(message='** Rol requerido **')],choices=[
                      ('usuarioFinal', 'Usuario final'), ('superAdmin', 'Super administrador'), ('administrador', 'Administrador')])
    enviar = SubmitField(u'Crear usuario')


class FormularioProveedor(FlaskForm):
    nombre_proveedor = StringField(u'Nombre', validators=[DataRequired(
        message='** Nombre requerido **'), Length(min=8)])
    nit = StringField(u'NIT', validators=[DataRequired(
        message='** NIT requerido **'), Length(min=5)])
    telefono = StringField(u'Teléfono', validators=[DataRequired(
        message='** Telefono requerido **'), Length(min=7, max=10)])
    correo = EmailField(u'Correo', validators=[DataRequired(
        message='** Correo requerido **'), Email()])
    enviar = SubmitField(u'Crear proveedor')


class FormularioProducto(FlaskForm):
    nombre_producto = StringField('Nombre', validators=[DataRequired(
        message='** Nombre requerido **'), Length(min=10)])
    nombre_proveedor = SelectMultipleField(u'Proveedor', coerce = int, validators=[DataRequired(message='** Proveedor requerido **')])
    descripcion = StringField('Descripción', validators=[DataRequired(
        message='** Correo requerido **'), Length(min=10, max=100)])
    cantidad_disponible = IntegerField(u'Cantidad disponible', validators=[DataRequired(
        message='** Cantidad disponible requerida **'), NumberRange(min=0, max=9999999)])
    cantidad_minima = IntegerField(u'Cantidad mínima', validators=[DataRequired(
        message='** Cantidad mínima requerida **'), NumberRange(min=0, max=9999999)])
    enviar = SubmitField('Crear producto')
