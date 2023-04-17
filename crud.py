from model import db, User, Post, Meetup, connect_to_db


#-----------------create_user--------------------------------------#
def create_user(username, email, password):
    
    user = User(username=username, email=email, password=password)

    return user

#-----------------get_user----------------------------------------#
def get_users():
    
    return User.query.all()


#-----------------get_user_by_id----------------------------------#
def get_user_by_id(user_id):
    
    return User.query.get(user_id)

#-----------------get_user_by_email-------------------------------#
def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

    