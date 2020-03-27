# Hackathon!

This is our project created in one day for the SEI35 cohort at General Assembly. 

To get this project running on your computer:
1. Clone this repo.
1. In the project directory, run the following commands:
   ```
   pipenv install
   pipenv shell
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser # Create a superuser
   python manage.py runserver
   ```
1. Open tab to `http://127.0.0.1:8000` to see the main site, where you can click on a sign-up link.
1. If you sign-up with a valid email, you will get a confirmation from smithsonian.zoo.entertainment@gmail.com.
1. "As the business, to be able to see the data being collected from newsletter sign-ups on an account dashboard", open a browser to `http://127.0.0.1:8000/admin/zoo/zoouser/`

With more time, here is what we'd like to do next:
1. Change re-direct page when user enters incorrect data
1. Create newsletter model in our database and have the information posted to our website
1. CSS and UI in general

### Authors

Colleen O'Brien and Sara Laffin

#### Inspiration

Tiger King, for the email addresss idea :)


Project requirements are listed below, as provided by GA:

## Project Overview
Your team's assignment is to create a way for users to sign up to recieve your client's newsletter via email.

### Constraints
  - Mobile-first, responsive, browser-based site
  - Must work in top 3 browsesr: Chrome, Safari and Firefox
  - Must be accessible: https://a11yproject.com/checklist/

## User Stories

### General
  - As a user, I am interested in signing up to receive email newsletters from the client
  - As a user, I might want to know more information about their newsletters

### Personal Information
  - As the user, I want to enter my personal information as quickly and easily as possible
  - As the business, I want the user to provide their first and last name
    - A first and last name is required
    - A name cannot contain a number
    - A name cannot contain a special character
    - A name must be at least two letters
  - As the business, I want the user to provide their email address
    - An email address is required
    - An email address must contain exactly one @
    - An email address must contain at least one period (.)

### Integration
  - As the business, I want to be able to see the data being collected from newsletter sign-ups on an account dashboard

### Confirmation
  - As a user, I want confirmation from the client that I am now subscribed to the newsletter

### Stretch Goals: Customizability
  - As a user, I want to determine exactly which newsletter topics I receive.
    - I want to be able to select one or more topics
  - As a user, I want to determine how frequently I receive these email newsletters
    - Frequencies to be determined by the team
