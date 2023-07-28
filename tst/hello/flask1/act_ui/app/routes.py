

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session # flask-login timeout

from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse


from app.forms import LoginForm
from app.forms import FeedbackForm
from app.models import User, Post
from app.extensions import db
from my_cfg import my_log


#
#
#
server_bp_id = 'main'
server_bp = Blueprint(server_bp_id, __name__)


@server_bp.route('/')
def index():
    session.permanent = True
    my_log.info('server_bp_route_slash')

    #return redirect(url_for('/board0a/'))
    out_url = redirect(url_for('main.login'))
    if current_user.is_authenticated:
        out_url = render_template("c_index.html", title='Home Page', user=current_user)

    return out_url


@server_bp.route('/login/', methods=['GET', 'POST'])
def login():
    my_log.info('login'+str(current_user))
    if current_user.is_authenticated:
        redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            error = 'Invalid username or password'
            return render_template('c_login.html', form=form, error=error)

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('c_login.html', title='Sign In', form=form)


@server_bp.route('/logout/')
@login_required
def logout():
    my_log.info('logging_out ')
    logout_user()
    # return redirect(url_for('/board0a/'))
    return redirect(url_for('main.index'))


#@server_bp.route('/register/', methods=['GET', 'POST'])
#def register():
#    if current_user.is_authenticated:
#        return redirect(url_for('main.index'))
#
#    form = RegistrationForm()
#    if form.validate_on_submit():
#        user = User(username=form.username.data)
#        user.set_password(form.password.data)
#        db.session.add(user)
#        db.session.commit()
#
#        return redirect(url_for('main.login'))
#
#    return render_template('register.html', title='Register', form=form)


#@server_bp.route('/feedback/', methods=['GET', 'POST'])
#@login_required
#def feedback():
#    form = FeedbackForm()
#    if form.validate_on_submit():
#
#        for u in User.query.all():
#            if current_user.username == u.username:
#                u0 = u
#        my_log.info(" feedback {} {} ".format(u0.id, u0.username))
#
#        p0 = Post(body=form.feedback.data, author=u0)
#        db.session.add(p0)
#        db.session.commit()
#
# user = User(username=form.username.data)
# user.set_password(form.password.data)
# db.session.add(user)
# db.session.commit()
#        return redirect(url_for('main.login'))
# return render_template('feedback.html', title='Feedback', form=form)


@server_bp.route('/board0/')
@login_required
def board0a():
    return render_template('c_dash.html', dash_url='/board00/')


@server_bp.route('/board1/')
@login_required
def board1a():
    return render_template('c_dash.html', dash_url='/board10/')


@server_bp.route('/board2/')
@login_required
def board2a():
    return render_template('c_dash.html', dash_url='/board20/')


@server_bp.route('/board3/')
@login_required
def board3a():
    return render_template('c_dash.html', dash_url='/board30/')

@server_bp.route('/feedback4/', methods=['GET', 'POST'])
@login_required
def feedback4a():
    form = FeedbackForm()
    if form.validate_on_submit():

        for u in User.query.all():
            if current_user.username == u.username:
                u0 = u
        my_log.info(" feedback {} {} ".format(u0.id, u0.username))

        p0 = Post(body=form.feedback.data, author=u0)
        db.session.add(p0)
        db.session.commit()

        # user = User(username=form.username.data)
        # user.set_password(form.password.data)
        # db.session.add(user)
        # db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('c_feedback.html', title='Feedback', form=form)
