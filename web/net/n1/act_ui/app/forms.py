
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

# https://stackoverflow.com/questions/21217475/get-selected-text-from-a-form-using-wtforms-selectfield
YES_NO_CHOICES = [('yes','yes'),('no','no')]
class TaleForm(FlaskForm):
    narrative_id = StringField('Narrative Id', validators=[DataRequired()])
    narrative = StringField('Narrative', widget=TextArea())
    narrative_correctness = SelectField('Correctness',
                                        choices=YES_NO_CHOICES)


#analysis_txt_default = 'All work and no play makes Jack a dull boy'
analysis_txt_default = "In Stanley Kubrick's film The Shining, the proverb is used to illustrate how the film's central figure, named Jack, has lost his mind when his wife discovers that he procrastinated and had written the sentence over and over again on hundreds of pages with a typewriter. Jack had been aiming to write a theatrical play, but instead wrote this proverb repeatedly using the formatting of the script (including its headings)."

TXT_CHOICES = [('1',''),
            ('2','All work and no play makes Jack a dull boy'),
            ('3',"In Stanley Kubrick's film The Shining, the proverb is used to illustrate how the film's central figure, named Jack, has lost his mind when his wife discovers that he procrastinated and had written the sentence over and over again on hundreds of pages with a typewriter. Jack had been aiming to write a theatrical play, but instead wrote this proverb repeatedly using the formatting of the script (including its headings)."),
            ('4','One of Edison’s greatest stories of perseverance began when he invented the light bulb and started looking for an inexpensive light bulb filament. He was using filament made of ore from the Midwest. In order to save high shipping cost, Edison decided to open his own ore mining plant nearby. He spent a decade to run the plant smoothly. In spite of all these cumbersome efforts, his project failed due to poor quality of ore on the East Coast. But even then Edison did not quit.'),
            ]

KEYWORD_CHOICES = [('1',''),
                ('2','"one hundred and ten", "twenty two thousand", "thirty four"'),
                ('3','"thirty five", "fourty four","fifty five","sixty six"'),
                ('4','"fourty four","fifty five","sixty six"'),
            ]
class AnalysisForm(FlaskForm):

    # validators=[DataRequired()]
    txt_slct = SelectField(u'Sample Texts',choices=TXT_CHOICES)
    analysis_txt = TextAreaField('Analysis Text',
                                 default=analysis_txt_default,
                                )
    #StringField('Analysis Text', widget=TextArea())
    analyze_btn = SubmitField('Analyze')
    clear_btn = SubmitField('Clear')
    keyword_slct = SelectField(u'KeywordChoice', choices=KEYWORD_CHOICES)
    keyword_str = StringField('Keywords')
