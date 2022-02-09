from flask_login import login_required
from flask import render_template
from . import main


@main.route('/', methods = ['GET','POST'])
def index():
    # form = ReviewForm()
    # movie = get_movie(id)

    title = 'Welcome'
    return render_template('index.html',title = title)

@main.route('/login', methods = ['GET','POST'])
@login_required
def login():
    # form = ReviewForm()
    # movie = get_movie(id)

    title = 'Welcome'
    return render_template('login.html',title = title)    
