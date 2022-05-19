from pathlib import Path
from split_settings.tools import include
from dotenv import load_dotenv

import os


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', False) == 'True'

include(
    'components/database.py',
    'components/templates.py',
    'components/internationalization.py',
    'components/application_definition.py',
    'components/password_validation.py',
    'components/static_url.py',
    'components/default_pk_field_type.py',
    'components/allowed_hosts.py'
)
