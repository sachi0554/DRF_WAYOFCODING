"""
WSGI config for DRF_WAYOFCODING project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .handler_register import register_handler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_WAYOFCODING.settings')
register_handler()
application = get_wsgi_application()

