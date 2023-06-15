
#
#
#
from app import app

from flask import render_template

from app.forms import LoginForm


class IndexCommon():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

index_common = IndexCommon()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=index_common.user, posts=index_common.posts)

@app.route('/index_a')
def index_a():
    return render_template('index_a.html', title='Home', user=index_common.user, posts=index_common.posts)

    
@app.route('/index_b')
def index_b():
    return render_template('index_b.html', title='Home', user=index_common.user, posts=index_common.posts)




   
@app.route('/login_a')
def login_a():
    form = LoginForm()
    return render_template('login_a.html', title='Sign In', form=form)



from flask import render_template, flash, redirect

@app.route('/login_b', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index_b')
    return render_template('login_b.html', title='Sign In', form=form)