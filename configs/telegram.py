from telegram.ext import Updater

from configs.config import BOT_API_TOKEN

UPDATER = Updater(token=BOT_API_TOKEN)
DISPATCHER = UPDATER.dispatcher
