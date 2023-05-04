from app import apps
from flask import render_template

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
