## This project demonstrates creating a note taking/ todo app using django 2.1.

- Django uses a MVC framework
- Database: SQLite

Here is a screenshot of what the application looks like:
![Screenshot](https://i.imgur.com/vuG86hi.png)

Some notes:
1. I used pip3 to install pipenv and django 2.1
2. To create the notes app/module of the note taking application, create views.py file and add the connecting URL to the note_taking_app urls.py file
3. Django uses templates to display their views
4. Create a templates folder in the same directory as notes
5. Within templates, create notes.html file
6. Route template folding by editing settings.py in note_taking_app directory. Specifically add templates route in DIR
7. Edit models.py file
8. Run python manage.py makemigrations to create migrations file so migration can communicate with database
9. Make migration by running python manage.py migrate