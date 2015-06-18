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

# in production server we have an extra settings file that overwrites devel settings.
# If we can import it then we are on production server and need to set up
# the virtualenv. Sucks that these paths are hard-coded.
try:
	# Add the site-packages of the chosen virtualenv to work with
	site.addsitedir('/home/django/.virtualenvs/blight_fight/local/lib/python2.7/site-packages')

	# Add the app's directory to the PYTHONPATH
	sys.path.append('/home/django/blight_fight')
	sys.path.append('/home/django/blight_fight/blight_fight')

	from settings_production import *


	# Activate your virtual env
	activate_env=os.path.expanduser("/home/django/.virtualenvs/blight_fight/bin/activate_this.py")
	execfile(activate_env, dict(__file__=activate_env))

except ImportError:
	pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
