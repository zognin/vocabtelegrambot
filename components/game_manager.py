from random_word import RandomWords

from api.dictionary_api import DictionaryApi
from components.message_manager import MessageManager
from components.word_entity import WordEntity
from exceptions.dictionary_api_exception import DictionaryApiException


class GameManager:
    no_definition_message = 'No Definitions Found'
    dictionary_api = DictionaryApi(no_definition_message)

    def __init__(self):
        self.word_entity = None

    def start(self, update, context):
        message_manager = MessageManager(update, context)
        message_manager.greet()
        self.__start_new_game_round(message_manager)

    def process_guess_input(self, update, context):
        guess = update.message.text
        message_manager = MessageManager(update, context)

        if self.__is_not_playing():
            message_manager.send_start_reminder()
            return

        if self.__is_incorrect_guess(guess) and self.word_entity.is_hintable():
            hint_word = self.word_entity.fill_char_in_blank_word()
            message_manager.send_hint(hint_word)
            return

        if self.__is_incorrect_guess(guess) and not self.word_entity.is_hintable():
            message_manager.send_ans_when_unsuccessful(self.word_entity.get_word())
            self.__start_new_game_round(message_manager)
            return

        message_manager.send_ans_when_successful(self.word_entity.get_word())
        self.__start_new_game_round(message_manager)

    def stop(self, update, context):
        self.word_entity = None
        message_manager = MessageManager(update, context)
        message_manager.send_goodbye()

    # ================================ PRIVATE METHODS ================================

    def __start_new_game_round(self, message_manager):
        try:
            word_entity = self.__get_random_word_entity()
            message_manager.send_new_word(word_entity)
        except DictionaryApiException as e:
            message_manager.send_error_message(str(e))

    def __get_random_word_entity(self):
        random_word_generator = RandomWords()
        random_word = None
        while random_word is None:
            random_word = random_word_generator.get_random_word(hasDictionaryDef='true')

        try:
            random_word_information = self.dictionary_api.get_word_definition(random_word)
        except DictionaryApiException as e:
            raise e

        # If there is a definition, return the word
        if random_word_information != self.no_definition_message:
            self.word_entity = WordEntity(random_word, random_word_information['definition'])
            return self.word_entity

        # Get another random word
        return self.__get_random_word_entity()

    def __is_not_playing(self):
        return self.word_entity is None

    def __is_incorrect_guess(self, guess):
        return not self.word_entity.is_equal(guess)
