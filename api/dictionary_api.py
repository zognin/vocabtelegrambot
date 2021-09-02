import json
import os

import requests
from dotenv import load_dotenv

from exceptions.dictionary_api_exception import DictionaryApiException


class DictionaryApi:
    def __init__(self, no_definition_message):
        load_dotenv()
        self.base_url = os.getenv('FREE_DICTIONARY_API_URL')
        self.no_definition_message = no_definition_message

    def get_word_definition(self, word):
        url = f"{self.base_url}/{word}"
        try:
            response = requests.get(url)
            json_response = json.loads(json.dumps(response.json()))
            if 'title' in json_response:
                return self.no_definition_message
            json_dict = json_response[0]
            return json_dict['meanings'][0]['definitions'][0]
        except requests.exceptions.RequestException:
            raise DictionaryApiException
