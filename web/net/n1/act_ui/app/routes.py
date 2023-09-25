
import os # import json

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for # from flask import abort
from flask import flash
from flask import session  # flask-login timeout
from flask import send_from_directory  # static directory to favicon.ico
from flask_cors import cross_origin

from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse


from app.forms import LoginForm, TaleForm, AnalysisForm
from app.models import User, Tale, Analysis
from app.extensions import db
from my_cfg import my_log, MyConfigObject

from app.forms import TXT_CHOICES, KEYWORD_CHOICES

#
#
#
import nltk
import pandas as pd

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
@cross_origin()
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

    return render_template('c_login.html', title='Login', form=form)


@server_bp.route('/logout/')
@login_required
def logout():
    my_log.info('logging_out ')
    logout_user()
    return redirect(url_for('main.index'))


@server_bp.route('/exploration/')
@login_required
def exploration():
    return render_template('c_dash.html', dash_url='/board30/')


@server_bp.route('/feedback4/', methods=['GET', 'POST'])
@login_required
def feedback4a():
    form = TaleForm()
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

    # filter by current_user
    user_now = User.query.filter_by(username=current_user.username).first_or_404()
    tale_query = Tale.query.filter_by(user_id=user_now.id)

    return {'data': [ a_tale.to_dict() for a_tale in tale_query]}


@server_bp.route('/overview', methods=['GET'])
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
        u0 = User.query.filter_by(username=current_user.username).first()
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
    user_now = User.query.filter_by(username=current_user.username).first()
    tale_query = Tale.query.filter_by(user_id=user_now.id)

    total = tale_query.count()

    # response
    return {
        'data': [a_post.to_dict() for a_post in tale_query],
        'total': total,
    }


@server_bp.route('/narration/info', methods=['POST'])
@login_required
def narration_info_update():

    from datetime import datetime

    request_json = request.get_json()
    my_log.info(' narration_info_update ' + str(request_json))
    if 'tale_id' not in request_json:
        request_json['tale_id'] = len(Tale.query.all()) #abort(400)

    response_code=404
    if int(request_json['tale_id']) < len(Tale.query.all()):

        request_post = Tale.query.get(request_json['tale_id'])
        my_log.info('narration_info_posts_update > request_post:' + str(request_post))
        # body
        setattr(request_post, 'timestamp', datetime.utcnow())
        for field in ['tale_narrative', 'tale_narrative_id', 'tale_narrative_submission_date', 'tale_narrative_correctness']:

            if field in request_json:
                my_log.info('narration_info_posts_update > field > updating' + str(field) + ' with ' + request_json[field] + 'timestamp' + str(datetime.utcnow) )
                setattr(request_post, field, request_json[field])


        db.session.commit()
        response_code=204
    else:  # new tale
        # get the current_user
        u0 = User.query.filter_by(username=current_user.username).first()
        my_log.info(" narration user_id: {} and username: {} ".format(u0.id, u0.username))

        p0 = Tale(user_id=u0.id,
                  tale_narrative=request_json['tale_narrative'],
                  tale_narrative_id=request_json['tale_narrative_id'],
                  tale_narrative_correctness=request_json['tale_narrative_correctness'],
                  tale_narrative_submission_date=datetime.utcnow(),
                  author=u0)
        db.session.add(p0)

        db.session.commit()
        response_code=200

    return '', response_code

# https://www.nltk.org/howto/chunk.html
# https://stackoverflow.com/questions/10929941/make-drag-and-drop-uploader-in-flask
@server_bp.route('/analysis', methods=['GET','POST'])
@login_required
def analysis():

    # filter by current_user
    u0 = User.query.filter_by(username=current_user.username).first_or_404()
    my_log.info(" feedback {} {} ".format(u0.id, u0.username))

    #

    form_default_page = 'c_analysis_a2.html'

    #
    #
    #
    if request.method == 'GET':
        form = AnalysisForm()
        return render_template(form_default_page, title='Analysis', form=form, user=current_user)
    elif 'analyze_btn' in request.form.keys():

        #if form.is_submitted(): #validate_on_submit():

        #form.analysis_txt.data = dict(TXT_CHOICES).get(form.txt_slct.data)
        #form.keyword_slct.data = dict(KEYWORD_CHOICES).get(form.txt_slct.data)

        now_lst = []
        now_txt = request.form['analysis_txt']
        now_sent = nltk.sent_tokenize(now_txt)
        for a_sentence_id in range(0,len(now_sent)):
            a_sentence = now_sent[a_sentence_id]
            a_snt_token = nltk.word_tokenize(a_sentence)
            a_snt_tag   = nltk.pos_tag(a_snt_token)
            a_snt_tag_df = pd.DataFrame(a_snt_tag)
            a_snt_tag_df_dict = a_snt_tag_df.to_dict()
            a_snt_tag0=a_snt_tag_df_dict[0].keys()
            a_snt_tag1= list(a_snt_tag_df_dict[0].values())
            a_snt_tag2= list(a_snt_tag_df_dict[1].values())
            now_lst.append({'snt': a_sentence,
                            'snt_id': a_sentence_id,
                            'tkn': a_snt_token,
                            'tag': a_snt_tag,
                            'tag0': a_snt_tag0,
                            'tag1': a_snt_tag1,
                            'tag2': a_snt_tag2,
                            }
                           )
        now_df = pd.DataFrame(now_lst)
        my_log.info(now_df.to_json())

        a0 = Analysis(author=u0,
                      analysis_txt=now_txt,
                      analysis_jsn=now_df.to_json()
                    )
        db.session.add(a0)
        db.session.commit()

        return render_template('c_analysis_snt.html',
                               title='AnalysisReport',
                               user=current_user,
                               items=now_lst)
    elif 'clear_btn' in request.form.keys():
        form = AnalysisForm()
        form.analysis_txt.data = ''
        return render_template(form_default_page, title='Analysis', form=form, user=current_user)
    elif 'txt_slct' in request.form.keys():
        form = AnalysisForm()
        form.analysis_txt.data = dict(TXT_CHOICES).get(form.txt_slct.data)
        form.keyword_slct.data = form.txt_slct.data
        form.keyword_str.data = dict(KEYWORD_CHOICES).get(form.txt_slct.data)
        return render_template(form_default_page, title='Analysis2', form=form, user=current_user)

    return render_template(form_default_page, title='Analysis', form = AnalysisForm(), user=current_user)




@server_bp.route('/analysis/config', methods=['POST'])
@login_required
def analysis_config():

    #
    form = AnalysisForm()
    form_default_page = 'c_analysis_a2.html'

    if 'txt_slct' in request.form.keys():
        form.analysis_txt.data = 'two'
        return render_template(form_default_page, title='AnalysisConfig', form=form, user=current_user)

    return render_template(form_default_page,
                           title='AnalysisConfig',
                           form=form,
                           user=current_user)



@server_bp.route('/analysis/info', methods=['GET'])
@login_required
def analysis_info():
    # filtering using the current_user
    now_user = User.query.filter_by(username=current_user.username).first()
    now_query = Analysis.query.filter_by(user_id=now_user.id)
    now_query_last = Analysis.query.order_by(Analysis.analysis_id.desc()).first()

    df = pd.read_json(now_query_last.analysis_jsn)
    df = df.reset_index()  # make sure indexes pair with number of rows
    df_dict = {
        'snt': str(df['snt']),
        'tag': str(df['tag']),
        'tkn': str(df['tkn']),
        'index': str(df.index),
        'columns': str(df.columns),
        'shape': str(df.shape),
    }

    out_lst = []
    for row_idx, row in df.iterrows():

        a_snt_token  = row['tkn']
        a_snt_tag    = row['tag']
        a_snt_tag_df = pd.DataFrame(row['tag'])
        a_snt_tag_df_dict = a_snt_tag_df.to_dict()
        a_snt_tag0 = list(a_snt_tag_df_dict[0].keys())
        a_snt_tag1 = list(a_snt_tag_df_dict[0].values())
        a_snt_tag2 = list(a_snt_tag_df_dict[1].values())
        out_lst.append({'snt': row['snt'],
                        'snt_id': row_idx,
                        'tkn': row['tkn'],
                        'tag': row['tag'],
                        'tag0': a_snt_tag0,
                        'tag1': a_snt_tag1,
                        'tag2': a_snt_tag2,
                        }
                       )

    # response
    return out_lst


@server_bp.route('/analysis_report', methods=['GET','POST'])
@login_required
def analysis_report():

    # filtering using the current_user
    now_user = User.query.filter_by(username=current_user.username).first()
    now_query = Analysis.query.filter_by(user_id=now_user.id)
    now_query_last = Analysis.query.order_by(Analysis.analysis_id.desc()).first()
    pd.read_json(now_query_last.analysis_jsn)
    # my_log.info(
    # now_query_last.analysis_jsn.
    # now_df = pd.read_json(

    out_lst = []
    for an_entry in now_query:
        out_lst.append(an_entry.to_dict)

    return render_template('c_analysis_report.html',
                           title='AnalysisReport',
                           user=current_user,
                           items=out_lst)






