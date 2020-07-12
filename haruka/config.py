


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "" #that you got from botfather
    OWNER_ID = "" #If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "" #@urusername

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = False
    WORKERS = 4  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAACAgUAAxkBAAEEJ4pefNAoMiGn6cLZdoy0sJQpHxcy-AACTQEAAupFXico2ds1vUzopRgE'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    GBAN_LOGS = ""
    SPAMMERS = ""
    DEV_USERS = []
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
