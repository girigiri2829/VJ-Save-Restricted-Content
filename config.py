import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7076384608:AAGskQfUrcJlLSb0yu6L5HSIY9xalNOErE8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23049826"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4a4216f089ce68a3ce2c8b9b9a6fa79a")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "2135601715"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "hdhub4net")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
