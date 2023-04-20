from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, User, Post, Meetup
import crud

app = Flask(__name__)
app.secret_key = "dev"
from jinja2 import StrictUndefined

#--------------------------home page--------------------------------#
@app.route("/")
def home():
    
    return render_template("index.html")


#--------------------------User Login GET-----------------------------#
@app.route("/login", methods=["GET"])
def login():


    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Incorrect email or password")
    else:
        session['user_email'] = user.email
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
        

    return redirect("/userprofile")
        

#-------------------------user profile--------------------------#
@app.route("/userprofile")
def user_profile():

    return render_template("userprofile.html")

#---------------------------meet up-----------------------------#
@app.route("/meet_up")
def meet_up():
    
    return render_template("meet_up.html")


#------------------------Post Content-------------------------#
@app.route("/post_content")
def post_content():

    return render_template("post_content.html")





if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    
