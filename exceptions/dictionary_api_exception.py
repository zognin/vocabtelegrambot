class DictionaryApiException(Exception):
    def __init__(self):
        message = "There was a problem in getting the word definition, please try again later"
        super().__init__(message)
