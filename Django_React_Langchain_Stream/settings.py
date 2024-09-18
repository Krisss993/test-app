import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from the .env file
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ml-chat.onrender.com','test-app-y0lp.onrender.com']

CSRF_TRUSTED_ORIGINS = [
    'https://test-app-y0lp.onrender.com',
]
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ALLOW_ALL_ORIGINS = True

LANGUAGE_CODE = 'en-us'  # or another default language
USE_I18N = True
USE_L10N = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'langchain_stream',
    'langchain_chat',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
    'crispy_forms',
    'crispy_bootstrap4',
    'core',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'Django_React_Langchain_Stream.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# WSGI_APPLICATION = 'Django_React_Langchain_Stream.wsgi.application'
ASGI_APPLICATION = "Django_React_Langchain_Stream.asgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
# }
print(f"postgresql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_NAME')}")

DATABASES = {
    'default': dj_database_url.config(default=f"postgresql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST')}:{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_NAME')}")
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
# Directory where static files are collected from apps and other locations
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # The folder in your project for static files
]
# Directory where static files are collected by `collectstatic` during production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'  # The base URL to serve media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/profile/'

# if DEBUG is False:
#    SESSION_COOKIE_SECURE = True
#    SECURE_BROWSER_XSS_FILTER = True
#    SECURE_CONTENT_TYPE_NOSNIFF = True
#    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#    SECURE_HSTS_SECONDS = 31536000
#    SECURE_REDIRECT_EXEMPT = []
#    SECURE_SSL_REDIRECT = True
#    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDER_PROTO', 'https')
#    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'