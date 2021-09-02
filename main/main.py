from components.game_manager import GameManager
from configs.telegram import UPDATER
from handlers.handler_manager import HandlerManager

game_manager = GameManager()
command_manager = HandlerManager(game_manager)
command_manager.add_handlers()

# Start receiving messages
UPDATER.start_polling()
