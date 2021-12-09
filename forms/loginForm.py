from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    national_id = StringField('National Id', validators=[DataRequired()])
    dob = DateField('DOB', validators=[DataRequired()])
    submit = SubmitField()