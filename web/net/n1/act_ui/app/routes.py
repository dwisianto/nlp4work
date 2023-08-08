

import os

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import abort
from flask import flash
from flask import session  # flask-login timeout
from flask import send_from_directory  # static directory to favicon.ido

from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse


from app.forms import LoginForm, TaleForm
from app.models import User, Tale
from app.extensions import db
from my_cfg import my_log, MyConfigObject



#
#
#
server_bp_id = 'main'
server_bp = Blueprint(server_bp_id, __name__)


@server_bp.route('/')
def index():
    session.permanent = True # flask login timeout
    my_log.info('server_bp_route_index_slash')

    out_url = redirect(url_for('main.login'))
    if current_user.is_authenticated:
        out_url = render_template("c_index.html", title='Home Page', user=current_user)

    return out_url


@server_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(server_bp.root_path, MyConfigObject.LOC_STATIC_FAVICON),
                               MyConfigObject.LOC_STATIC_FAVICON_NAME,
                               mimetype='image/vnd.microsoft.icon' )


@server_bp.route('/login/', methods=['GET', 'POST'])
def login():
    my_log.info('login'+str(current_user))
    if current_user.is_authenticated:
        redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            error_msg = 'Invalid username or password'
            flash(error_msg)
            return render_template('c_login.html', form=form, error=error_msg)

        if form.remember_me.data:
            login_user(user, remember=True, duration=MyConfigObject.PERMANENT_SESSION_LIFETIME)
        else:
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


@server_bp.route('/exploration/')
@login_required
def board0a():
    return render_template('c_dash.html', dash_url='/board30/')


@server_bp.route('/feedback4/', methods=['GET', 'POST'])
@login_required
def feedback4a():
    form = NarrationForm()
    if form.validate_on_submit():

        # filter by current_user
        u0 = User.query.filter_by(username=current_user.username).first_or_404()
        my_log.info(" feedback {} {} ".format(u0.id, u0.username))

        p0 = Tale(body=form.narrative.data, author=u0)
        db.session.add(p0)
        db.session.commit()

        # user = User(username=form.username.data)
        # user.set_password(form.password.data)
        # db.session.add(user)
        # db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('c_feedback.html', title='Feedback', form=form)






@server_bp.route('/datatable7/', methods=['GET'])
@login_required
def datatable7():
    return render_template('c_datatable.html', title='Example Ajax Table')


@server_bp.route('/datatable7/info')
@login_required
def datatable7_data():
    #tale_query = Tale.query

    # filter by current_user
    user_now = User.query.filter_by(username=current_user.username).first_or_404()
    tale_query = Tale.query.filter_by(user_id=user_now.id)

    return {'data': [ a_tale.to_dict() for a_tale in tale_query]}




@server_bp.route('/overview/', methods=['GET'])
@login_required
def overview():
    return render_template('c_overview.html', title='Overview', user=current_user)

@server_bp.route('/overview/info')
@login_required
def overview_info():

    # filter by current_user
    #user_now = User.query.filter_by(username=current_user.username).first_or_404()
    #tale_query = Tale.query.filter_by(user_id=user_now.id)
    tale_query = Tale.query.all()

    return {'data': [ a_tale.to_dict() for a_tale in tale_query]}



@server_bp.route('/narration/', methods=['GET', 'POST'])
@login_required
def narration():

    form = TaleForm()
    if form.validate_on_submit():

        # get the current_user
        u0 = User.query.filter_by(username=current_user.username).first_or_404()
        my_log.info(" narration user_id: {} and username: {} ".format(u0.id, u0.username))

        # current form
        my_log.info("narration form_narrative_id:" + str(form.narrative_id))
        my_log.info("narration narrative_correctness:" + str(form.narrative_correctness))
        my_log.info("narration form:" + str(form.narrative_id))

        # check for existing tale
        t0 = Tale.query.filter_by(tale_narrative_id=form.narrative_id.data).first()
        my_log.info(" narration tale n0: {} ".format(t0))

        now_tale_id=len(Tale.query.all())
        if t0 is not None and t0.tale_id is not None: # existing tale
            t0.tale_narrative_id = form.narrative_id.data
            t0.tale_narrative = form.narrative.data
            t0.tale_narrative_correctness = form.narrative_correctness.data

        if t0 is None:
            p0 = Tale(user_id=u0.id,
                      tale_narrative=form.narrative.data,
                      tale_narrative_id=form.narrative_id.data,
                      tale_narrative_correctness=form.narrative_correctness.data,
                      author=u0)

            db.session.add(p0)

        db.session.commit()

        #return redirect(url_for('main.login'))
        return render_template('c_narration.html',
                               title='Narration',
                               form=TaleForm(),
                               user=current_user)

    return render_template('c_narration.html',
                           title='Narration',
                           form=form,
                           user=current_user)

@server_bp.route('/narration/info', methods=['GET'])
@login_required
def narration_info():
    tale_query = Tale.query

    # filter by current_user
    user_now = User.query.filter_by(username=current_user.username).first_or_404()
    tale_query = Tale.query.filter_by(user_id=user_now.id)

    total = tale_query.count()

    # response
    return {
        'data': [a_post.to_dict() for a_post in tale_query],
        'total': total,
    }


@server_bp.route('/narration/info', methods=['POST'])
def narration_info_update():

    from datetime import datetime

    request_json = request.get_json()
    my_log.info(' narration_info_update ' + str(request_json))
    if 'id' not in request_json:
        abort(400)

    request_post = Post.query.get(request_json['id'])
    my_log.info(' editable_info_posts_update > request_post:' + str(request_post) )
    for field in ['body']:
        if field in request_json:
            my_log.info(' editable_info_posts_update > field > updating' + str(field) + ' with ' + request_json[field] + 'timestamp' + str(datetime.utcnow) )
            setattr(request_post, field, request_json[field])
            setattr(request_post, 'timestamp', datetime.utcnow())
    db.session.commit()
    return '', 204
