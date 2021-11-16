#Final Project

CS50 Web Programming with Python and JavaScript



#Distinctiveness and Complexity

I believe this project satisfies the distinctiveness and complexity requirements as I have used chat system,javascript geolocation and match concept is distinct from previous projects.this project is not based on old CS50W Pizza project because this project is not online order system and this project is not include Menu, Adding Items, Shopping Cart and others.

This project is completely distinct from social network project because this project is an online dating application.Users anonymously to like or dislike other users' profiles, which include their photo, a short bio, and a list of their interests and they can exchange messages when user like eachother.

finally this project is absolutely distinct from an e-commerce site project2 because Ecommerce site cannot be equated to online dating.In ecommerce site users can post products and other users bid those products.In this project two people, complete strangers, meet on the internet, and then interact online for some time, before deciding to have that first date.

This project was built using Django as a backend framework and JavaScript as a frontend programming language.this project including three models.All generated information are saved in database (SQLite by default).

All webpages of the project are mobile-responsive.

Furthermore, the general concept and UI has not been based on any previous projects and thus is unique.


#Introduction

My final project is  Dating app. Users are able to create account,uploading photo, "like" other users' or "unlike other users'.if users like each other,it becomes match and then users can message each other.If users access their locations,users can see near 50miles other users on their newfeed.users can also edit and delete their accounts.    


#Tools and Languages

HTML
CSS
Bootstrap
Python Django
Javascript
Bootstrap Icon


#Installation

pip install requirements.txt.

python manage.py makemigrations 

python manage.py migrate

And You can run this command to run your server.

python manage.py runserver

Create superuser with python manage.py createsuperuser. This step is optional.


#Files and directories

pinner - main application directory.
templates/pinner/layout.html contains all static content.

Login.html - 
you need to first login for application.

Register.html - 
If you don't have login account you can register with username, email and password.

Create.html - 
when you are register,you can create account with birthday date,profile picture,gender,interest,like_gender,height,passions.if you don't have account,you can't use this application and if you are not register or login.you can't create account.

index.html - 
when you created account,redirect to index page.first you can see alert box for locations.You need to access your locations and then you can see near 50miles other users on your newfeed.you will see other users detail and then you can like or unlike other users in index page.Index page is singlepage.It contains matches and your profile.

if you click people icon,you will see other users matches with you and you can messages them.In private message chat,you can see dropdown icon and two options "view other profile detail" or "unmatch that user".
if you click view profile,you can see other user profile detail and if you click unmatch, you can never  see to this user. 

if you click your profile,you will see your profile detail and you can edit your profile detail and upload new profile picture and you can delete or logout.

profile.html - 
For other users profile page.

admin.py - here I added some admin register sites Passion, Profile, SendMessage, User.

decorators.py - I added one function for permission.

tests.py - I added three functions for testing

models.py contains three models I used in the project. Profile model is for user account profile, 
Passions. model is for Profile, and SendMessage model represents users messages.

urls.py - all application URLs.

views.py respectively, contains all application views.

media - this directory contains all users profile photos.

SuperUser
The super user can manipulate all data in the backend management dashboard.Super user can also have a view of all users, sendmessage, profile and added, edit or delete for those things.

My FinalProject is aiming for people to get lifepartner.


Finally
Thanks for all people make CS50's Web Programming with Python and JavaScript possible. Especially, thanks for Instructor Brain Yu.

November 11, 2021
