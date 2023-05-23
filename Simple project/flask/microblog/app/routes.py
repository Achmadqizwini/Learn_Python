from app import apps
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@apps.route('/')
@apps.route('/index')

def index():

    user = {'username': {"Achamd"}}

    posts = [
        {
            'author': {'username':'Jonathan'},
            'body': 'Ore no namae wa Jonathan Jotaro, ore wa yume ga aru'
        },
        {
            'author': {'username': 'Dio'},
            'body': 'ZZAWARUDO'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@apps.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('login requested for user{}, remember_me= {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)