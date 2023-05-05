class Message:
    def __init__(self, id, user_id, text):
        self.id = id
        self.user_id = user_id
        self.text = self.__validate_message(140)(text)
        # self.text = self.validate_message(140, text)

    def __validate_message(self, max_length):
        def validator(text):
            if len(text) > max_length or len(text) == 0:
                raise ValueError(f"Le message ne doit pas être vide "
                                 f"ou dépasser la longueur de {max_length} caractères.")
            return text

        return validator


if __name__ == "__main__":
    try:
        message = Message(1, 1, "Un message valide.")
    except ValueError as e:
        print(e)
    else:
        print(message.text)
