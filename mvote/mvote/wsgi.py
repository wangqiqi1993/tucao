"""
WSGI config for ch08www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

#++++++DJANGO+++++++
import os
import sys

path = '/home/tucao/mvote'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mvote.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()