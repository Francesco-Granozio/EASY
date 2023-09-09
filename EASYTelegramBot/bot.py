import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from DatabaseManager import DatabaseManager
from Player import Player
from PlayerDAO import PlayerDAO


async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Ciao *{update.effective_user.full_name}* benvenuto sul bot EASY!\n' 
                                    f'Stai avendo difficoltà nello studiare il linguaggio di programmazione C?\n' 
                                    f'Non ti preoccupare, questo bot ti aiuterà a superare le tue difficoltà e allo stesso tempo ' 
                                    f'ti divertirai con i tuoi amici.\n' 
                                    f'Ecco la lista dei dei comandi:\n' 
                                    f'/nickname *`nuovo nickname`* per modificare il tuo nickname\n'
                                    f'/profilo per visulizzare le statistiche del tuo profilo (punti, emblemi, ecc...)\n',
                                    parse_mode='Markdown')

    database_manager = DatabaseManager(r"C:\Shared\Unisa\Tesi\EASY\database.db")

    if await PlayerDAO(database_manager).do_retrieve_by_id(
            update.effective_user.id) is None:
        await PlayerDAO(database_manager).do_save(
            Player(update.effective_user.id, update.effective_user.full_name, 0))


def main():
    app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()
    app.add_handler(CommandHandler("start", comando_start))
    app.run_polling()


if __name__ == '__main__':
    main()
