"""
WSGI config for blight_fight project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

os.environ['DJANGO_SETTINGS_MODULE'] = 'blight_fight.settings'

try:
	from settings_production import *

	# Add the site-packages of the chosen virtualenv to work with
	site.addsitedir('/home/django/.virtualenvs/blight_fight/local/lib/python2.7/site-packages')

	# Add the app's directory to the PYTHONPATH
	sys.path.append('/home/django/blight_fight')
	sys.path.append('/home/django/blight_fight/blight_fight')


	# Activate your virtual env
	activate_env=os.path.expanduser("/home/django/.virtualenvs/blight_fight/bin/activate_this.py")
	execfile(activate_env, dict(__file__=activate_env))

except ImportError:
	pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

