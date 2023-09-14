
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField

from wtforms.validators import DataRequired


# ToDo: Replace widgets wtforms.widgets.TextArea with wtforms.fields.TextAreaField
from wtforms.widgets import TextArea

from wtforms.fields import TextAreaField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    remember_me = BooleanField('Remember Me')


class TaleForm(FlaskForm):
    narrative_id = StringField('Narrative Id', validators=[DataRequired()])
    narrative = StringField('Narrative', widget=TextArea())
    narrative_correctness = SelectField('Correctness',
                                        choices=[('yes','yes'),
                                                 ('no','no')])


#analysis_txt_default = 'All work and no play makes Jack a dull boy'
analysis_txt_default = "In Stanley Kubrick's film The Shining, the proverb is used to illustrate how the film's central figure, named Jack, has lost his mind when his wife discovers that he procrastinated and had written the sentence over and over again on hundreds of pages with a typewriter. Jack had been aiming to write a theatrical play, but instead wrote this proverb repeatedly using the formatting of the script (including its headings)."

class AnalysisForm(FlaskForm):

    analysis_txt = TextAreaField('Analysis Text',default=analysis_txt_default)
    #StringField('Analysis Text', widget=TextArea())
    analyze_btn = SubmitField('Analyze')
    clear_btn  = SubmitField('Clear')