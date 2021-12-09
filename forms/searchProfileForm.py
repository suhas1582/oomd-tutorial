from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchUserProfiles(FlaskForm):

    id = StringField('User id', validators=[DataRequired()])
    submit = SubmitField('Submit')