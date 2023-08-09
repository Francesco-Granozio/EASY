import os
import telebot
import utils

from comandi import *
from databaseManager import DatabaseManager

db = DatabaseManager("database.db")
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

current_topic = None


def registra_nickname(message):
    if message.text.replace(" ", "").isalnum() and len(message.text) <= 30:
        db.modifica_utente(message.from_user.id, message.text)
        bot.send_message(message.chat.id, f"Ciao {message.text} ti sei registrato con successo!")
    else:
        bot.send_message(message.chat.id, "Nome utente non valido. Riprova.")
        bot.register_next_step_handler(message, registra_nickname)


@bot.message_handler(commands=['start'])
def visualizza_comandi(message):
    global current_topic

    current_topic = None
    db.crea_tabella_utenti()

    nickname = db.cerca_utente(message.from_user.id)

    if nickname is None:
        nickname = utils.get_nickname(message)
        db.inserisci_utente(message.from_user.id, utils.get_nickname(message))
    else:
        nickname = nickname[1]

    messaggio = f"Ciao {nickname}! Benvenuto sul bot!\n"

    keyboard = utils.crea_tastiera(*[topic for topic in opzioni])

    for option_name, option_description in opzioni.items():
        messaggio += f"-{option_name}\n    {option_description}\n"

    bot.send_message(message.chat.id, messaggio, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == OPZIONI_NICKNAME)
def handle_nickname_command(message):
    if current_topic is not None:
        bot.send_message(message.chat.id, "Non puoi cambiare il nickname mentre stai facendo un quiz!")
        return

    bot.send_message(message.chat.id, 'Inserisci il tuo nickname:')
    bot.register_next_step_handler(message, registra_nickname)


@bot.message_handler(func=lambda message: message.text == OPZIONI_QUIZ)
def handle_quiz_command(message):
    global current_topic
    current_topic = OPZIONI_QUIZ
    messaggio = "Ecco la lista completa degli argomenti:\n"

    for topic_name, topic_description in quiz_topics.items():
        messaggio += f"-{topic_name}\n    {topic_description}\n"

    keyboard = utils.crea_tastiera(*[topic for topic in quiz_topics])

    bot.send_message(message.chat.id, messaggio, reply_markup=keyboard)


def handle_quiz_topic(topic, message):
    global current_topic

    if current_topic != OPZIONI_QUIZ:
        bot.send_message(message.chat.id, "Comando non valido!")
        return

    current_topic = topic

    selected_topic = quiz_topics.get(topic)
    if selected_topic:
        topic_description = selected_topic
        bot.send_message(message.chat.id, f"Quiz su: {topic_description}")
    else:
        bot.send_message(message.chat.id, "Argomento non trovato.")


@bot.message_handler(func=lambda message: message.text == QUIZ_CONCETTI_BASE)
def handle_quiz_topic_concetti_base(message):
    handle_quiz_topic(QUIZ_CONCETTI_BASE, message)




# @bot.message_handler(func=lambda message: message.text == QUIZ_ESPRESSIONI_CICLI)
# def handle_quiz_topic_espressioni_cicli(message):
#     handle_quiz_topic(QUIZ_ESPRESSIONI_CICLI, message)
#
#
# @bot.message_handler(func=lambda message: message.text == TORNA_INDIETRO)
# def handle_quiz_torna_indietro(message):
#     global current_topic
#
#     if current_topic != OPZIONI_QUIZ:
#         bot.send_message(message.chat.id, "Comando non valido!")
#         return
#
#     visualizza_comandi(message)


bot.infinity_polling()