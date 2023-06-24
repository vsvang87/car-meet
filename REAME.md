A car meet up web application for car enthusiasts to find or host their own meet up. Has user login authentication with CRUD operations. It allow users to create their own car events or search events in their area using google maps to fetch and display markers on the location. Users can update their first name, last name, city and state in their user profile. I've also implemented the Cloundianry API to upload pictures of their car.

Tech Stack: PostgreSQL, SQL Alchemy, Python, Flask, Jinja, HTML, CSS, JavaScript(ajax), Cloudinary API, Google Maps

Data Model:

Users:     |   Events:        
-----------|---------------
user_id    |   event_id      
firstname  |   start_date      
lastname   |   end_date       
email      |   event_description       
password   |   user_id(fk)          
city       |   
zipcode    |       
image      | 