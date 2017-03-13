from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=80)])
    firstname = StringField('First Name', validators=[InputRequired(), Length(max=80)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(max=80)])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    biography = StringField('Short Biography', validators=[Length(max=127)])
