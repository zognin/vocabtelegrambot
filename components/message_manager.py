class MessageManager:
    def __init__(self, update, context):
        self.update = update
        self.context = context

    def greet(self):
        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text="Welcome to Vocab Buddy! Let's learn some new words!"
        )

    def send_new_word(self, word_entity):
        question = "What is a word that means \"{definition}\"?" \
                   "\n\nIt has {length} letters" \
                   "\n{blank_word}" \
            .format(definition=word_entity.definition,
                    length=word_entity.get_word_length(),
                    blank_word=word_entity.blank_word
                    )

        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=question
        )

    def send_start_reminder(self):
        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text="Send /start to start a game first!"
        )

    def send_hint(self, hint_word):
        response = "That's not quite right, here's a hint" \
                   f"\n{hint_word}"

        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=response)

    def send_ans_when_unsuccessful(self, word):
        message = f"The word is actually {word}, let's try another word!"

        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=message
        )

    def send_ans_when_successful(self, word):
        message = f"You got it! The word is {word}, let's try another word!"

        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=message
        )

    def send_goodbye(self):
        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text="See you next time ^^, send /start to start another round"
        )

    def send_error_message(self, message):
        self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=message
        )
