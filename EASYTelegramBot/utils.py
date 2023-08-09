import telebot


def get_nickname(message):
    username = message.from_user.username
    if username is None:
        username = message.from_user.first_name
        if message.from_user.last_name is not None and username is not None:
            username += " " + message.from_user.last_name

    else:
        username = message.from_user.id

    return username


def crea_tastiera(*buttons):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    for button_text in buttons:
        button = telebot.types.KeyboardButton(button_text)
        keyboard.add(button)
    return keyboard


