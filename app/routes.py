from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gino'}



    posts = [
        {
            'author': {'username': 'Michelle'},
            'body': 'Have a wonderful day!'
        },
        {
            'author': {'username': 'Gerardo'},
            'body': 'Nice to meet you!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
