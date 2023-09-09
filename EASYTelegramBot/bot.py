import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from DatabaseManager import DatabaseManager
from Player import Player
from PlayerDAO import PlayerDAO

db_path = r"C:\Shared\Unisa\Tesi\EASY\database.db"
database_manager = DatabaseManager(db_path)


async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
                                    f'/profilo per visulizzare le statistiche del tuo profilo (punti, emblemi, ecc...)\n',
                                    parse_mode='Markdown')


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


def main():
    app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()
    app.add_handler(CommandHandler("start", comando_start))
    app.add_handler(CommandHandler("nickname", comando_nickname))
    app.run_polling()


if __name__ == '__main__':
    main()
