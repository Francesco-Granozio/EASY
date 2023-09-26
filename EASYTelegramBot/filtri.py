from functools import wraps
from telegram import Update, Chat
from telegram.ext import ContextTypes


# il comando è visibile soltanto se viene scritto nella chat con il bot
def filtro_privato(func):
    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.type == Chat.PRIVATE:
            return await func(update, context)

    return wrapped


# il comando è visibile soltanto se viene scritto nel gruppo dei quiz
def filtro_pubblico(func):
    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.type != Chat.PRIVATE:
            return await func(update, context)

    return wrapped
