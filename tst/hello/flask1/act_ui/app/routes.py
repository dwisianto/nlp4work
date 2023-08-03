

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session # flask-login timeout
from flask import abort

from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse


from app.forms import LoginForm, FeedbackForm, TaleForm
from app.models import User, Post, Tale
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


@server_bp.route('/editable5/', methods=['GET', 'POST'])
@login_required
def editable5():
    return render_template('c_editable.html', title='Feedback')


@server_bp.route('/api/data')
@login_required
def editable_info_posts():
    post_query = Post.query

    # filter by current_user
    user_now = User.query.filter_by(username=current_user.username).first_or_404()
    post_query = Post.query.filter_by(user_id=user_now.id)

    # search filter
    search = request.args.get('search')
    if search:
        post_query = post_query.filter(db.or_(
            Post.body.like(f'%{search}%'),
        ))
    total = post_query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['body']:
                name = 'body'
            col = getattr(Post, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            post_query = post_query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = post_query.offset(start).limit(length)

    # response
    return {
        'data': [a_post.to_dict() for a_post in post_query],
        'total': total,
    }


@server_bp.route('/api/data', methods=['POST'])
def editable_info_posts_update():

    from datetime import datetime

    request_json = request.get_json()
    my_log.info(' editable_info_posts_update ' + str(request_json))
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


@server_bp.route('/summary/', methods=['GET'])
@login_required
def overview():
    return render_template('c_overview.html', title='Overview')


@server_bp.route('/narration/', methods=['GET', 'POST'])
@login_required
def narration():

    form = TaleForm()
    if form.validate_on_submit():

        # get the current_user
        u0 = User.query.filter_by(username=current_user.username).first_or_404()
        my_log.info(" narration {} {} ".format(u0.id, u0.username))

        p0 = Tale(body=form.narrative.data, author=u0)
        db.session.add(p0)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('c_narration.html', title='Narration', form=form)

@server_bp.route('/narration/info')
@login_required
def narration_info():
    tale_query = Tale.query

    # filter by current_user
    user_now = User.query.filter_by(username=current_user.username).first_or_404()
    tale_query = Tale.query.filter_by(user_id=user_now.id)

    # search filter
    search = request.args.get('search')
    if search:
        tale_query = tale_query.filter(db.or_(
            Tale.body.like(f'%{search}%'),
        ))
    total = tale_query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['body']:
                name = 'body'
            col = getattr(Post, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            tale_query = tale_query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = tale_query.offset(start).limit(length)

    # response
    return {
        'data': [a_post.to_dict() for a_post in tale_query],
        'total': total,
    }


@server_bp.route('/narration/info', methods=['POST'])
def narration_info_update():

    from datetime import datetime

    request_json = request.get_json()
    my_log.info(' editable_info_posts_update ' + str(request_json))
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
