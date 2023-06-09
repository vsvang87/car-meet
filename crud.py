from model import db, User, Meetup, connect_to_db


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
def create_post(date_time, post_content, user_id):

    create_post_content = Post(date_time=date_time, post_content=post_content, user_id=user_id)
    
    return create_post_content

#-----------------get_user_by_id----------------------------------#
def get_user_by_id(user_id):
    
    return Meetup.query.filter(Meetup.user_id == user_id).all()


#------------------Meet up Page-----------------------------------------#
def meet_up(title, date_time, address, city, state, zipcode, description, user_id):

    meetup = Meetup(title=title, date_time=date_time, address=address, city=city, state=state, zipcode=zipcode, description=description, user_id=user_id)

    return meetup



def get_events(user_id):
    
    return Meetup.query.filter(Meetup.user_id == user_id).all()


def get_meet_up_by_id(meet_up_id):

    return Meetup.query.filter(Meetup.meet_up_id == meet_up_id).first()
#------------------------------------------------------------------------#
def create_city_and_state(city, state, user):

    user.city = city
    user.state = state

    return user

   
#-----------------Update user image---------------------------------#
def update_img_url(image_url, user):

    user.image_url = image_url

    return image_url

