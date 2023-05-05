from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from model import connect_to_db, db, User, Meetup, Post
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
        flash("Login Successful!")
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
        

#-------------------------user profile, events--------------------------#
@app.route("/userprofile")
def user_profile():

    
    email = session['user_email']
    user = crud.get_user_by_email(email)

    
    user_id = session["user_id"]
    events = crud.get_events(user_id)
    
    return render_template("userprofile.html", user=user, events=events)


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
   


#---------------------------search meet up-----------------------------#
@app.route("/meet_up")
def meet_up():
    
    state = request.args.get("state")
    city = request.args.get("city")

    meetups = Meetup.query.filter(Meetup.state == state, Meetup.city == city).all()

    return render_template("meet_up.html", meetups=meetups, city=city, state=state)


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

    if user_id is None:
        flash("You have to logged in to create event")
    else:
        meets = crud.meet_up(title, datetime, address, city, state, zipcode, user_id)
        db.session.add(meets)
        db.session.commit()
        flash("Post is successful")
    
    return redirect("/userprofile")

 

@app.route("/update_event", methods=["POST"])
def update_event():

    # Getting meet up id input from form
    meet_up_id = request.form.get("meet_up_id")  

    title = request.form.get("title")
    datetime = request.form.get("datetime")
    address = request.form.get("address")
    city = request.form.get("city")
    state = request.form.get("state")
    zipcode = request.form.get("zipcode")

    user_id = session.get('user_id')
    
    meetup = crud.get_meet_up_by_id(meet_up_id)
    
    if user_id is None:
        flash("You have to log in to update event")

    if title:
         meetup.title = title

    if datetime:
        meetup.datetime = datetime

    if address:
        meetup.address = address

    if city:
        meetup.city = city

    if state:
        meetup.state = state

    if zipcode:
        meetup.zipcode = zipcode
  
    db.session.commit()
    flash("Event update successful")

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

    if username:
        user.username = username
      
    if first_name:
        user.first_name = first_name
      
    if last_name:
        user.last_name = last_name
       
    if city:
        user.city = city
        
    if state:
        user.state = state
       

    db.session.commit()
    flash("Profile update successful")

    return redirect("/userprofile")

#----------------------------Post Content Page----------------------------#
@app.route("/post_content",methods=["GET", "POST"])
def post_content():

    # date_time = request.form.get("datetime")
    # posts = request.form.get("posts")

    # user_id = session['user_id']
    # user = crud.get_user_by_id(user_id)

    # if len(posts) < 1:
    #     flash("Post cannot be empty!")
    # else:
    #     new_post = Post(post_content=posts, user=user)
    #     db.session.add(new_post)
    #     db.session.commit()
    #     flash("Post successful!")


    return render_template("post_content.html")

#-----------------------Delete Events-----------------#
@app.route("/delete_meetup/<meet_id>", methods=["POST"])
def delete(meet_id):

    user = session.get("user_id")
    if user is None:
        flash("You must logged in to delete a post")
    else:
        meetup = Meetup.query.filter(Meetup.meet_up_id == meet_id).first()
        db.session.delete(meetup)
        db.session.commit()
        flash("Event has been deleted")

    
    return redirect("/userprofile")
    

#------------------------Log Out-----------------------------#
@app.route("/logout")
def logout():

    session.clear()
    flash("Logged out successful")
   
    return redirect("/login")

#-----------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    
