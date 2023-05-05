from model import db, User, Meetup, Post, connect_to_db


#-----------------create_user--------------------------------------#
def create_user(first_name, last_name, username, city, state, email, password):
    
    user = User(first_name=first_name, last_name=last_name, username=username, city=city, state=state, email=email, password=password)

    return user

#-----------------get_user----------------------------------------#
def get_users(user_id):
    
    return User.query.filter(User.user_id == user_id).all()


#-----------------get user by username----------------------------#
def get_user_by_username(username):

    return User.query.filter(User.username == username).first()


#-----------------get_user_by_email-------------------------------#
def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

#----------------get_user_by_password-----------------------------#
def get_user_by_password(password):

    return User.query.filter(User.password == password).first()

#----------------create post--------------------------------------#
# def create_post(datetime, post_content, user_id):

#     post = Post(datetime=datetime, post_content=post_content, user_id=user_id)
    
#     return post

#-----------------get_user_by_id----------------------------------#
def get_user_by_id(user_id):
    
    return Meetup.query.filter(Meetup.user_id == user_id).all()


#------------------Meet up Page-----------------------------------------#
def meet_up(title, date_time, address, city, state, zipcode, user_id):

    meetup = Meetup(title=title, date_time=date_time, address=address, city=city, state=state, zipcode=zipcode, user_id=user_id)

    return meetup



def get_events(user_id):
    
    return Meetup.query.filter(Meetup.user_id == user_id).all()



#------------------------------------------------------------------------#
def create_city_and_state(city, state, user):

    user.city = city
    user.state = state

    return user

   
#-----------------Update user image---------------------------------#
def update_img_url(image_url, user):

    user.image_url = image_url

    return image_url

#-------------------Update User Profile-----------------------------#
# def update_user_profile(city, state, username, user):
#     user.city = city
#     user.state = state
#     user.username = username

#     return user
