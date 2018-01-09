"""Django settings for mysite project."""

import environ

# ініціалізується об'єкт, через який читати щось із енва зручно + дефолт для дебага
env = environ.Env(DEBUG=(bool, False),)
# оце шукає шлях папки на 2 рівні вище, ніж поточний файл (по-новому, замість того, що чуть нижче)
BASE_DIR = environ.Path(__file__) - 2
environ.Env.read_env()  # А оце читає файл із назвою .env, потім про це
# os імпортити більше не треба, ми тільки шляхи ним склеювали

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# читаємо змінну середовища з назвою SECRET_KEY, якщо нема - дефолт
SECRET_KEY = env('SECRET_KEY', default='na*iqh-5=($8u+3pt3(lkthu6*9jm!l6!a7!o@(qw4d%&8v+ri')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')  # те ж саме для дебага, дефолт на рядку 5

ALLOWED_HOSTS = ['127.0.0.1', 'lolis4e1.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite3'),  # а це вже хелпер для парсингу змінної DATABASE_URL в словник,
                                                        # який був тут перед цим. дефолтне значення - sqlite база
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT_DIR = env.path('STATIC_ROOT', BASE_DIR('static'))  # заміняємо на гарніший спосіб працювати зі шляхами
STATIC_ROOT = STATIC_ROOT_DIR()
