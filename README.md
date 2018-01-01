# django-girls-blog-makkaronis4e
[![Build Status](https://travis-ci.org/kpi-web-guild/django-girls-blog-makkaronis4e.svg?branch=master)](https://travis-ci.org/kpi-web-guild/django-girls-blog-makkaronis4e)

How to run this site from your own computer locally and deploy it on heroku:

1. Clone this repository to your local folder
2. Register account on Heroku
3. Install Heroku CLI locally
4. Login to Heroku
```$ login heroku```
username : blank
password : heroku auth token
``` $ heroku auth:token```
5. Create name of your site
```$ heroku create your-name```
6. Push your local repository to heroku
```$ git push heroku master```
7. Tell heroku to start web process
```$ heroku ps:scale web=1```
8. Run migrate and create superuser
```$ heroku run python manage.py migrate```
```$ heroku run python manage.py createsuperuser```
