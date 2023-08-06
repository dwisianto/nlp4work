
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField

from wtforms.validators import DataRequired
from wtforms.widgets import TextArea



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    remember_me = BooleanField('Remember Me')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class FeedbackForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    feedback = StringField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TaleForm(FlaskForm):
    narrative_id = StringField('Narrative Id', validators=[DataRequired()])
    narrative = StringField('Narrative', widget=TextArea())
    narrative_correctness = SelectField('Correctness',
                                        choices=[('yes','yes'),
                                                 ('no','no')])
    submit = SubmitField('Submit')
