import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main():
    app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()
    app.add_handler(CommandHandler("start", comando_start))
    app.run_polling()


if __name__ == '__main__':
    main()



