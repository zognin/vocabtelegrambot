from telegram.ext import CommandHandler, MessageHandler, Filters
from configs.telegram import DISPATCHER


class HandlerManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def add_handlers(self):
        # List handlers
        start_handler = CommandHandler('start', self.game_manager.start)
        stop_handler = CommandHandler('stop', self.game_manager.stop)
        read_guess_input_handler = MessageHandler(Filters.text, self.game_manager.process_guess_input)

        # Add handlers to the dispatcher
        handlers = [start_handler, stop_handler, read_guess_input_handler]
        for handler in handlers:
            DISPATCHER.add_handler(handler)
