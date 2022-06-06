#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv
import pathlib

def main():
    """Run administrative tasks."""
    DJANGO_ENV = os.environ.get('DJANGO_ENV')
    if DJANGO_ENV:
        DOT_ENV_FILE = pathlib.Path() / f'{DJANGO_ENV}.env'
    dotenv.read_dotenv(str(DOT_ENV_FILE))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_WAYOFCODING.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
