# Login/Signup form
Written in Python with:
 - flask for the backend
 - wtforms for form validation
 - sqlite with sqlalchemy for the database
 - werkzeug for password hashing
 - dotenv for environment variables

HTML/CSS for the frontend

Checklist:
 - [x] Sort checkbox value acceptance
 - [x] encrypt password
 - [x] setup DB (sqlite)
    - [x] create model
    - [x] initialise database
    - [x] check for user in db
    - [x] user doesnt exist signup / add to db
    - [x] else return user already exists
 - [x] logins
 - [x] csrf token?
 - [x] dotenv
 - [x] sessions