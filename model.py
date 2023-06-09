from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#-------------------------------------------------------------------------
class User(db.Model):
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),nullable=False, unique=True)
    password = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    image_url = db.Column(db.String, nullable=True)

    meet_ups = db.relationship("Meetup", back_populates="user")

    def __repr__(self):
        return f"<User username={self.username} user_id={self.user_id}>"


#------------------------------------------------------------------
class Meetup(db.Model):
    
    __tablename__ = 'meets'

    meet_up_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
    date_time = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    description = db.Column(db.String(1500), nullable=True)

    user = db.relationship("User", back_populates="meet_ups")

    def __repr__(self):
        return f"<Meetup city={self.city} state={self.state}>"
    

# class Post(db.Model):
    
#     __tablename__ = 'posts'

#     post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     post_content = db.Column(db.String(5000), nullable=True)
#     date_time = db.Column(db.DateTime, nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

#     user = db.relationship("User", back_populates="posts")

#     def __repr__(self):
#         return f"<Post post_id={self.post_id} user_id={self.user_id}>"


#------------------------------------------------------------------
def connect_to_db(flask_app, db_uri="postgresql:///car_meet", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()