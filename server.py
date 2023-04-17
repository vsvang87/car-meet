from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, User, Post, Meetup

app = Flask(__name__)
app.secret_key = "dev"

#--------------------------home--------------------------------#
@app.route("/")
def home():
    
    username = request.form.get('username')
    email = request.form.get("email")
    password = request.form.get("password")
    
    return render_template("index.html")


#---------------------------meet up-----------------------------#
@app.route("/meetup")
def meet_up():
    
    return render_template("meetup.html")



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    connect_to_db(app)
