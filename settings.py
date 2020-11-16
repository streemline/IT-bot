import os

from dotenv import load_dotenv

load_dotenv()

BOT_PROXY = {'https': os.environ.get('BOT_PROXY')}
BOT_TOKEN = os.environ.get('BOT_TOKEN')

INVENTARIZATION_SPREADSHEET_ID = os.environ.get('INVENTARIZATION_SPREADSHEET_ID')
CREDENTIAL_FILE = os.environ.get('CREDENTIAL_FILE')

DB_FILE_PATH = os.environ.get('DB_FILE_PATH')

USER_SECRET = os.environ.get('USER_SECRET')

LOG_FILE = os.environ.get('LOG_FILE')

CHANNEL_ID = os.environ.get('CHANNEL_ID')
