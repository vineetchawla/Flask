
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname' : 'Vineet'}
    posts = [
            {
                'name': 'Vineet Chawla',
                'body': 'Beautiful Day'
            },

            {
                'name': 'chawla Vineet',
                'body': 'Bad day'
            }
        ]
    return render_template('index.html', title = "Nice Guy", user=user, posts = posts)
