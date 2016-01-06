"""
Django settings for blight_fight project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n!ri)qh6@-3&qgzj(&#6a#1-lsbb!j!vh^41ds5&d-f09nv=4*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CRISPY_FAIL_SILENTLY = not DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #required by allauth
    'django.contrib.gis', # added 20150225
	'crispy_forms', # added 20150225
	'django_tables2', # added 20150225
	'django_tables2_reports', # added 20150225
	'django_filters', # added 20150225
	'allauth',	# added 20150526
	'allauth.account', # added 20150526
	'endless_pagination', # added 20150610 for old style map search.
    'django.contrib.humanize', # added 20150708 to format prices in template
    'formtools',    # added 20151028 to use form wizard for application form
    'ajaxuploader',
	'property_inventory',
	'annual_report_form',
	'property_inquiry',
	'neighborhood_associations',
	'property_condition',
    'applications',
	'applicants',
    'accella_records'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django_tables2_reports.middleware.TableReportMiddleware',
)

ROOT_URLCONF = 'blight_fight.urls'

WSGI_APPLICATION = 'blight_fight.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'blight_fight', # change this to a new db to prevent problems on dev server
        'USER': 'chris',
        'PASSWORD': 'chris',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Indiana/Indianapolis'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/chris/Projects/geodjango/blight_fight/static/',
)

# custom things added by Chris
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# django-allauth required added 20150526
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            	BASE_DIR + '/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
				"django.core.context_processors.request",
				'allauth.account.context_processors.account',
#				'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]

# django all-auth related
AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)


LOGIN_URL = '/map/accounts/login'
LOGIN_REDIRECT_URL = '/map/accounts/profile'
LOGOUT_URL = '/map/accounts/logout'
#AUTH_USER_MODEL = 'applicants.ApplicantUser'
AUTH_PROFILE_MODULE = 'applicants.ApplicantProfile'

#django all-auth related
SITE_ID = 2

# set all-auth to use email as username
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_DISPLAY = lambda user: user.email
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_FORM_CLASS = 'applicants.forms.SignupForm'

# Email settings - for development. Typically over-written by production settings for production use
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# used by django-passwords
PASSWORD_COMPLEXITY = { # You can omit any or all of these for no limit for that particular set
    "UPPER": 1,        # Uppercase
    "LOWER": 1,        # Lowercase
    "LETTERS": 0,       # Either uppercase or lowercase letters
    "DIGITS": 1,       # Digits
    "PUNCTUATION": 0,  # Punctuation (string.punctuation)
    "SPECIAL": 0,      # Not alphanumeric, space or punctuation character
    "WORDS": 0         # Words (alphanumeric sequences separated by a whitespace or punctuation character)
}


# media settings
MEDIA_ROOT = '/home/chris/Projects/geodjango/blight_fight/media/'
MEDIA_URL = '/media/'

# for django-tables2-reports
EXCEL_SUPPORT = 'xlwt'

# Production settings are kept in a separate file, settings_production.py which overrides db, email, secret key, etc with production values
try:
	from settings_production import *
except ImportError:	#
	pass
