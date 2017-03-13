import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
from forms import RegistrationForm
from models import UserProfile
from hashlib import pbkdf2_hmac
from binascii import hexlify
from werkzeug import secure_filename
import time


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


# check if filetype is allowed
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_PROFILE_PIC_EXTENSIONS']


@app.route('/')
def home():
    return profile()


@app.route('/profile', methods=["GET","POST"])
def profile():
    form = RegistrationForm()

    if request.method == "POST" and form.validate_on_submit():

        username = form.username.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        age = form.age.data
        gender = form.gender.data
        biography = form.biography.data

        existing = UserProfile.query.filter_by(username=username).all()
       
        # check if user exists
        if len(existing) > 0:
            flash("That username is already taken, please choose another", "danger")
            return render_template('register.html', active="profile", form=form)
        else:
            # check if picture uploaded
            if 'profilepic' not in request.files:
                flash("Please upload a profile picture")
                return render_template('register.html', active="profile", form=form)
            f = request.files['profilepic']
            # browser may have submitted empty file without name
            if f.filename == '':
                flash("Please upload a profile picture")
                return render_template('register.html', active="profile", form=form)
            if f and allowed_file(f.filename):
                filename = "%s.%s" % (username, "png")
                f.save(os.path.join(app.config['PROFILE_PIC_FOLDER'], filename))

            # create user object to add
            # current time in milliseconds, guaranteed unique
            uid = str(int(round(time.time() * 1000)))
            new_user = UserProfile(uid, firstname, lastname, username, age, gender, biography, time.strftime("%Y-%m-%d"))
            #flash(new_user)
            db.session.add(new_user)
            db.session.commit()
            flash("Successfully registered new user", "success")

            return render_template('register.html', active="profile", form=form)

    flash_errors(form)
    return render_template('register.html', active="profile", form=form)


@app.route('/profiles', methods=["GET", "POST"])
def profiles():

    # get profiles
    users = UserProfile.query.all()
    _users = []

    if request.method == "POST" and 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        for user in users:
            _users.append({ "username": user.username, "userid": user.userid })
        return jsonify({ "users": _users})

    return render_template('profiles.html', users=users)


@app.route('/profile/<userid>', methods=["GET", "POST"])
def user_profile(userid):

    # get profile
    user = UserProfile.query.filter_by(userid=userid).first()

    if request.method == "POST" and 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        _user = { "userid": user.userid,
                "username": user.username,
                "image": user.username+".png",
                "gender": user.gender,
                "age": user.age,
                "profile_created_on": user.created_on }
        return jsonify(_user)

    return render_template('profile.html', user=user)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="localhost",port="8080")