#Using email for auth instead of username

## start new project:
1. Create new directory
2. `pipenv install django`
3. `pipenv shell`
4. `django-admin startproject whatsonme_auth .`
5. `python manage.py startapp auth_email`
6. settings -> add created app to the installed app
7. settings -> `AUTH_USER_MODEL = 'auth_email.Auth'`
8. create custom auth class based on AbstractUser in models.py
9. create forms.py file to include the custom form for signup
10. update the admin.py to that create a new custom admin user based on the built-in adminuser that will use email also, and list the models in the admin page
11. connect to postgres database
    install psycopg2 and update the settings file to configure the database
11. `python manage.py makemigrations`
12. `python manage.py migrate`
13. `python manage.py createsuperuser`
14. `python manage.py runserver`
15. signout from the admin account

## using django-allauth
1. `pipenv install django-allauth`
2. update the settings.py to include it and also add .sites
3. create and link templates folder to override the built-in templates (the name should be templates/'account' to override the original one)
4. create home page to redirect to after login/out and set that in the settings
    ''' 
        LOGIN_REDIRECT_URL = 'home'
        ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
    '''
5. create template for the home page in the template
6. create view and url for the app
7. to override each default page of the allauth create new template for it and it will be changed

