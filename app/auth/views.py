from flask import render_template,redirect,url_for
from . import auth
from .forms import ReviewForm


@auth.route('/login',  methods = ['GET','POST'])
def login():
    review_form = ReviewForm()
    title = 'welcome'

    if review_form.validate_on_submit():
        username = review_form.username.data
        email = review_form.email.data
        password = review_form.password.data
        confirm = review_form.confirm.data
        new_profile = Review()
        return redirect(url_for('index',new_profile=new_profile))




    return render_template('auth/login.html',title=title, review_form=review_form)

