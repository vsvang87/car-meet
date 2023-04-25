from flask import Flask, render_template, request, flash, session, redirect, url_for
from model import connect_to_db, db, User, Post, Meetup
import crud

import cloudinary.uploader
import os

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dha9labk1"

app = Flask(__name__)
app.secret_key = "DEV"
from jinja2 import StrictUndefined

#--------------------------Home page--------------------------------#
@app.route("/")
def home():
    
    return render_template("index.html")


#--------------------------User Login-----------------------------#
@app.route("/login")
def login():

    # email = request.args.get("email")
    # password = request.args.get("password")

    # user = crud.get_user_by_email(email)
    # if not user or user.password != password:
    #     flash("Incorrect email or password")

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():
    
    username = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Incorrect email or password")
        return redirect("/login")
    else:
        session['user_email'] = user.email
        session['user_name'] = user.username
        flash(f"Welcome {user.email}")
        return redirect("/userprofile")
    

#-------------------------create new user----------------------#
@app.route("/create_user", methods=["GET"])
def create_new_user():

    
    return render_template("create_user.html")


@app.route("/create_user", methods=["POST"])
def create_new_users():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_password(password)
    if user:
        flash("That email already existed")
    else:
        user = crud.create_user(first_name, last_name, username, email, password)
        db.session.add(user)
        db.session.commit()
        session['user_email'] = user.email

    return redirect("/userprofile")
        

#-------------------------user profile--------------------------#
@app.route("/userprofile")
def user_profile():

    email = session['user_email']
    user = crud.get_user_by_email(email)

    return render_template("userprofile.html", user=user)


@app.route("/post-form-data", methods=["POST"])
def userprofile_username():

    my_file = request.files['my-file']
    result = cloudinary.uploader.upload(my_file, api_key = CLOUDINARY_KEY, api_secret = CLOUDINARY_SECRET, cloud_name = CLOUD_NAME)
    image_url = result['secure_url']
    #getting user session
    email = session['user_email']
    # getting the email function from crud
    user = crud.get_user_by_email(email)
    # updating user image from crud
    crud.update_img_url(image_url, user)
    db.session.add(user)
    db.session.commit()

    return redirect("/userprofile")
    
    
@app.route("/userprofile", methods=["POST"])
def add_city_and_state():

    #getting city and state from form
    city = request.form.get("city")
    state = request.form.get("state")

    email = session['user_email']
    user = crud.get_user_by_email(email)
    user = crud.create_city_and_state(city, state, user)
    db.session.add(user)
    db.session.commit()

    return redirect("/userprofile")
#---------------------------search meet up-----------------------------#
@app.route("/meet_up")
def meet_up():
    
    state = request.args.get("state")
    city = request.args.get("city")

    meetups = Meetup.query.filter(Meetup.state == state, Meetup.city == city).all()

    return render_template("meet_up.html", meetups=meetups)


@app.route("/create_meet_up_form")
def create_meet_up_form():
    #this route is to display the form
    return render_template("create_meet_up.html")



@app.route("/create_meet_up")
def meetup():

    date_time = request.form.get("datetime")
    city = request.form.get("city")
    state = request.form.get("state")
    zipcode = request.form.get("zipcode")
    # crud.meet_up(datetime, city, state, zipcode, user_id)
    #this data need to comes from the form in the create_meet-up.html


    return render_template("create_meet_up.html")




#------------------------Post Content-------------------------#
@app.route("/post_content")
def post_content():

    return render_template("post_content.html")


#------------------------Log Out-----------------------------#
@app.route("/logout")
def logout():

    session.pop('username')

    return redirect("/")

#--------------------------Host Event-----------------------#
@app.route("/host-event")
def host_event():

    return render_template("host_event.html")


#-----------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    
