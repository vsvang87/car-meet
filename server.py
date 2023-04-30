from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from model import connect_to_db, db, User, Meetup
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

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():
    
    # username = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Incorrect username, email or password")
        return redirect("/login")
    else:
        session['user_email'] = user.email
        session['user_id'] = user.user_id
        # flash(f"Welcome {user.email}")
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
    city = request.form.get('city')
    state = request.form.get('state')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_password(password)
    if user:
        flash("That email already existed")
        return redirect("/create_user")
    else:
        user = crud.create_user(first_name, last_name, username, city , state, email, password)
        db.session.add(user)
        db.session.commit()
        session['user_email'] = user.email
        session['user_id'] = user.user_id

    return redirect("/userprofile")
        

#-------------------------user profile--------------------------#
@app.route("/userprofile")
def user_profile():

    email = session['user_email']
    user = crud.get_user_by_email(email)
    print(email) 
    print(user)
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
    # city = request.form.get("city")
    # state = request.form.get("state")

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


#-------------------------Create Meet Up Form-------------------#
@app.route("/create_meet_up_form")
def create_meet_up_form():
   
    return render_template("create_meet_up.html")



@app.route("/create_meet_up_form", methods=["POST"])
def meetup():
  
    title = request.form.get("title")
    datetime = request.form.get("datetime")
    address = request.form.get("address")
    city = request.form.get("city")
    state = request.form.get("state")
    zipcode = request.form.get("zipcode")

    user_id = session['user_id']
    
    meets = crud.meet_up(title, datetime, address, city, state, zipcode, user_id)
    db.session.add(meets)
    db.session.commit()
    
    return redirect("/userprofile")

#------------------------Edit User Profile-------------------------#
@app.route("/profile_update")
def profile_update():

    email = session['user_email']
    user = crud.get_user_by_email(email)
    
    return render_template("profile_update.html", user=user)



@app.route("/profile_update", methods=["POST"])
def user_profile_update():

    username = request.form.get("username")
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    city = request.form.get("city")
    state = request.form.get("state")

    email = session['user_email']
    user = crud.get_user_by_email(email)

    if user.username:
        user.username = username
    elif user.first_name:
        user.first_name = first_name
    elif user.last_name:
        user.last_name = last_name
    elif user.city:
        user.city = city
    elif user.state:
        user.state = state
    

    db.session.commit()

    return redirect("/userprofile")
#------------------------Log Out-----------------------------#
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


#-----------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    
