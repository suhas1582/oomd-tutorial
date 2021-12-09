from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class UpdateProfileDetailsForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    national_id = StringField('National ID', validators=[DataRequired()])
    phone_no = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10, message='The phone number shoud be exactly 10 numbers long')])
    dob = DateField('DOB', validators=[DataRequired()])
    submit = SubmitField('Update Profile')