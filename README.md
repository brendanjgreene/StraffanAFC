# WebSite or WebApp for my local Football club

The Aim of this app is to create a website for my local Football Club which allows the management to Manage the 
information that it needs to run the Club and for other members and visitors to get the necessary information that they 
need while maintaining the Privacy of our members especially the underage ones. The Management  should be able to update
information and have it displayed on the website without having to ask the developer to make changes but rather be able 
to do it themselves using the UI that has been set up in advance.

## Secondary Aim is to make an App that can be easily adapted to be used by other clubs and therefore increase my exposure as a Full Stack Web Developer

## KEY COMPONENTS

A Club administrator (i.e. club secretary who has been setup with superuser privileges) is able to manage the website 
using the methods and forms provided by the app without having technological "coding skills" to accomplish the following:
* Create Edit and Delete Teams and in creating a Team set up a news feed for them
* Create Edit and Delete Managers (and other staff) and assign them to a team and assign them username and password which they can use for Logon privileges
* Create Edit and Delete Players and assign (or reassign) them to a Team
* View the Databases containing sensitive information and control who else can see it.
* Post relevant Club News for everyone to see


Managers and other staff can:
* Update their own profile information to insure details available to the public are up to date
* Update their password
* Share news about their prospective teams
* View the relevant information about the players on their team in the database

Visitors and Members of the club without logon privileges:
* See and view News about the club
* Use links to access Registration forms etc.
* See information about upcoming games

### Not Yet implemented
Superuser will be able to 
* Edit Club Name, Colors and Logo as well as other information and those changes will be reflected in the website

## Tech used

* Python using the  Django Framework
* HTML5
* CSS
* javascript an jQuery
* Bootstrap for ease of styling and ensuring a mobile first design

## Deployment
When this repository is ready for deployment you will be able to :

1. Fork this repository
2. Navigate to the local directory where you forked this repository on your Terminal or command line and Run the following commands:
* `python manage.py createsuperuser` in order to create an initial user with administration privileges
* `python manage.py makemigrations` to ensure the database is ready to be setup
* `python manage.py migrate` to run migrations and setup database
* `python manage.py runserver` to run locally and begin using the user interface to get it ready to Deploy using Heroku or other deployment method
