# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1948607264:AAHnS5Bq487wogPFKEB_4zgmVnHzFwUQk9U"
    OWNER_ID = "1370004762"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Ali1313_Ha"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://alihashemi1313:Ali.1313@hostname:port/alihashemi1313'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation', 'rss', 'weather', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1370004762
    ]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [
    ]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [
    ]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # ban sticker
    START_STICKER = False  #add a START_STICKER_ID = 'stickerid' in your config.py if you use this as true
    START_STICKER_ID = 'CAADAgAD0QMAAjq5FQKizo2AiTQCBQI'  #putin hand sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    API_OPENWEATHER = None  # OpenWeather API


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
