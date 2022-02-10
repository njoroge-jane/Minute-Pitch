from flask import render_template,redirect,url_for
from . import auth
from .forms import ReviewForm,RegistrationForm
from ..models import User
from .. import db


# @auth.route('/login',  methods = ['GET','POST'])
# def login():
#     review_form = ReviewForm()
#     title = 'welcome'

#     if review_form.validate_on_submit():
#         username = review_form.username.data
#         email = review_form.email.data
#         password = review_form.password.data
#         confirm = review_form.confirm.data
#         new_profile = Review(username,email,password,confirm)
#         return redirect(url_for('index',new_profile=new_profile))




#     return render_template('auth/login.html',title=title, review_form=review_form)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',registration_form = form,title=title)