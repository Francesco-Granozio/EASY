import os
from typing import Any

import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext

from Argomenti import Argomenti
from filtri import filtro_privato, filtro_pubblico
from DatabaseManager import DatabaseManager
from Player import Player
from PlayerDAO import PlayerDAO
from PowerupDAO import PowerupDAO

bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'))
DB_PATH = r"C:\Shared\Unisa\Tesi\EASY\database.db"
database_manager = DatabaseManager(DB_PATH)

lobbies = {argomento: False for argomento in Argomenti}


@filtro_privato
async def comando_start(update: Update, context: Any) -> None:
    player = (await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id))
    if player is None:
        player = Player(update.effective_user.id, update.effective_user.full_name, 0)
        await PlayerDAO(database_manager).do_save(player)

    await update.message.reply_text(f'Ciao *{player.get_nickname()}* benvenuto sul bot EASY!\n'
                                    f'Stai avendo difficoltà nello studiare il linguaggio di programmazione C?\n'
                                    f'Non ti preoccupare, questo bot ti aiuterà a superare le tue difficoltà e allo stesso tempo '
                                    f'ti divertirai con i tuoi amici.\n'
                                    f'Ecco la lista dei dei comandi:\n'
                                    f'/nickname *`nuovo nickname`* per modificare il tuo nickname\n'
                                    f'/quiz per visulizzare gli argomenti si cui iniziare un quiz\n'
                                    f'/profilo per visulizzare le statistiche del tuo profilo (punti, emblemi, ecc...)\n',
                                    parse_mode='Markdown')


@filtro_privato
async def comando_nickname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 0:
        await update.message.reply_text('Devi inserire il nuovo nickname dopo il comando /nickname')
    elif len("".join(context.args)) > 30:
        await update.message.reply_text('Il nickname deve essere lungo massimo 30 caratteri')
    else:
        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)

        if player.nickname == " ".join(context.args):
            await update.message.reply_text('Il nickname inserito è già il tuo nickname attuale')
            return

        player.set_nickname(" ".join(context.args))
        await PlayerDAO(database_manager).do_update(player)
        await update.message.reply_text(f'Nickname aggiornato con successo!')


@filtro_privato
async def comando_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    opzioni = [
        [
            InlineKeyboardButton(text=Argomenti.CONCETTI_BASE.value, url='https://t.me/+kV0M0bH98k5iYjNk'),
            InlineKeyboardButton(text=Argomenti.ESPRESSIONI_CONDIZIONALI.value, url='https://t.me/+Yge7RsgLTsE4Mjg0'),
        ],
        [
            InlineKeyboardButton(text=Argomenti.FUNZIONI.value, url='https://t.me/+VLOanReXCyFhOWNk'),
            InlineKeyboardButton(text=Argomenti.ARRAY_PUNTATORI.value, url='https://t.me/+lOz9oEaCvvs0YzBk'),
        ],
        [
            InlineKeyboardButton(text=Argomenti.STRINGHE.value, url='https://t.me/+Uve6o8bowFg1M2Y0'),
            InlineKeyboardButton(text=Argomenti.STRUTTURE_DATI.value, url='https://t.me/+pB1kqZKl9iZiYWY0'),
        ],
        [
            InlineKeyboardButton(text=Argomenti.GESTIONE_MEMORIA.value, url='https://t.me/+StdzIqaaMQBkOTQ8'),
            InlineKeyboardButton(text=Argomenti.FILES.value, url='https://t.me/+F33xkrlIjywzOWU0'),
        ],
        [
            InlineKeyboardButton(text=Argomenti.ISTRUZIONI_PREPROCESSORE.value, url='https://t.me/+wDQAXpAJpEZiYTlk'),
        ],
    ]

    await update.message.reply_text(text="Ecco gli argomenti su cui fare quiz:",
                                    reply_markup=InlineKeyboardMarkup(opzioni))


@filtro_privato
async def comando_profilo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
    if player is None:
        await update.message.reply_text('Devi prima registrarti con il comando /start')
        return

    await update.message.reply_text(
        f'Ecco le informazioni del tuo profilo:\nNickname: *{player.get_nickname()}*\nPunteggio: *{player.get_punteggio()}*',
        parse_mode='MarkdownV2')


@filtro_privato
async def comando_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (f"Il funzionamento del bot è molto semplice!\n"
            f"Una volta selezionato l\'argomento su cui vuoi fare il quiz dovrai rispondere correttamente alla domande per ottenere punti ed altre ricompense.\n"
            f"Potrai utilizare un sacco di potenziamenti:\n")

    powerups = await PowerupDAO(database_manager).do_retrieve_all()
    for powerup in powerups:
        text += f"*{powerup.get_nome()}*:  {powerup.get_descrizione()}.\n"

    await update.message.reply_text(text, parse_mode='Markdown')


@filtro_pubblico
async def comando_start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(text="Inizia il quiz 🚀", callback_data="start_quiz"),
        ]
    ]

    messaggio = await bot.send_message(text="Premi il bottone per iniziare il quiz 👇🏻", chat_id=update.message.chat_id,
                                       reply_markup=InlineKeyboardMarkup(keyboard))
    try:
        await context.bot.pin_chat_message(chat_id=update.message.chat_id, message_id=messaggio.message_id)
    except Exception as e:
        print(f"Impossibile fissare il messaggio: {e}")


async def bottone_avvia_quiz(update: Update, context: CallbackContext) -> None:
    await bot.send_message(text="Quiz avviato fraaaatm", chat_id=update.callback_query.message.chat_id)


def main():
    app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()
    app.add_handler(CommandHandler("start", comando_start))
    app.add_handler(CommandHandler("nickname", comando_nickname))
    app.add_handler(CommandHandler("quiz", comando_quiz))
    app.add_handler(CommandHandler("profilo", comando_profilo))
    app.add_handler(CommandHandler("info", comando_info))
    app.add_handler(CommandHandler("start_quiz", comando_start_quiz))

    app.add_handler(CallbackQueryHandler(bottone_avvia_quiz, pattern="start_quiz"))

    app.run_polling()


if __name__ == '__main__':
    main()
