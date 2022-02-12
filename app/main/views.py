from unicodedata import category
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from app.auth.forms import UpdateProfile
from .. import db,photos
from flask_login import login_required
from ..models import Pitches
from .forms import PitchForm


@main.route('/', methods = ['GET','POST'])
def index():
    # form = ReviewForm()
    # movie = get_movie(id)

    title = 'Welcome'
    return render_template('index.html',title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        pitch = form.pitch.data
        new_pitch = Pitches(title,category,pitch)
        new_pitch.save_pitch()
        return redirect(url_for('index'))

    title = 'Add Pitch'
    return render_template('new_pitch.html',title = title, pitch_form=form)    