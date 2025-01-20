from CaiLinXMusic.core.bot import Hotty
from CaiLinXMusic.core.dir import dirr
from CaiLinXMusic.core.git import git
from CaiLinXMusic.core.userbot import Userbot
from CaiLinXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "sasukevipmusicbot"  # connect music api key "Dont change it"
