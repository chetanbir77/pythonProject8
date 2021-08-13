"""
WSGI config for homelane project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homelane.settings')

application = get_wsgi_application()
path = '/home/chetanbir77/pythonProject8'
if path not in sys.path:
    sys.path.insert(0, path)