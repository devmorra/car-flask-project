from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit_button = SubmitField()

class UserSignupForm(FlaskForm):
    # email, password, submit_button
    first_name = StringField("First Name (Optional)")
    last_name = StringField("Last Name (Optional)")
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit_button = SubmitField()

class CarAddForm(FlaskForm):
    make = StringField('make', validators=[DataRequired()])
    model = StringField('model', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    topSpeed = StringField('topSpeed', validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired()])
    mileage = StringField('mileage', validators=[DataRequired()])
    submit_button = SubmitField()
    