import random


class WordEntity:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition[:-1]
        self.blank_word = WordEntity.make_blank_word(word)
        self.num_filled_char_in_blank_word = 0

    def get_word(self):
        return self.word

    def get_word_length(self):
        return len(self.word)

    @staticmethod
    def make_blank_word(word):
        blank_word = ""

        for char in word:
            blank_word += "_ "

        return blank_word

    def is_equal(self, word):
        return self.word == word.strip().lower()

    def fill_char_in_blank_word(self):
        index = 0
        char_in_blank_word = ''

        while char_in_blank_word != '_':
            index = random.randint(0, self.get_word_length() * 2 - 1)
            char_in_blank_word = self.blank_word[index]

        index_in_word = int(index / 2)
        word_as_list = list(self.blank_word)
        word_as_list[index] = self.word[index_in_word]
        self.blank_word = ''.join(word_as_list)
        self.num_filled_char_in_blank_word += 1
        return self.blank_word

    def is_hintable(self):
        return 3 * self.num_filled_char_in_blank_word < 2 * self.get_word_length()
