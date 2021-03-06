# django-girls-blog-makkaronis4e
[![Build Status](https://travis-ci.org/kpi-web-guild/django-girls-blog-makkaronis4e.svg?branch=master)](https://travis-ci.org/kpi-web-guild/django-girls-blog-makkaronis4e)


##### How to run this site from your own computer locally and deploy it on heroku?

###### To run locally:
1. Clone this repository to your local folder
2. Run in terminal
```
$ pip install -r requirements/dev.txt
```
3. Add `.env` in `mysite` folder, like in `.env.example`

4. Run your local server
```
(myvenv) ~/djangogirls$ python manage.py runserver
```
5. [Open it in browser](http://127.0.0.1:8000/)


###### To deploy on heroku:

1. Register account on Heroku
2. Install Heroku CLI locally
3. Login to Heroku
```
$ login heroku
$ heroku git:remote
```
4. Create name of your site
```
$ heroku create your-name
```
5. Push your local repository to heroku
```
$ git push heroku master
```
6. Tell heroku to start web process
```
$ heroku ps:scale web=1
```
7. Run migrate and create superuser
```
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
```
