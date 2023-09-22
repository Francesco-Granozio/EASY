import os
from typing import Any
import asyncio
import random
from datetime import datetime, timedelta
from functools import partial

import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext, \
    PollAnswerHandler

from Argomenti import Argomenti
from filtri import filtro_privato, filtro_pubblico
from DatabaseManager import DatabaseManager
from Player import Player
from Powerups import Powerups
from Domanda import Domanda
from Settings import Settings
from PlayerDAO import PlayerDAO
from DomandaDAO import DomandaDAO
from SettingsDAO import SettingsDAO

bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'))
DB_PATH = r"C:\Shared\Unisa\Tesi\EASY\database.db"
database_manager = DatabaseManager(DB_PATH)

quiz_attivi = {argomento.value: False for argomento in Argomenti}
messaggi_per_lobby = {argomento.value: [] for argomento in Argomenti}
players_in_quiz = {argomento.value: [] for argomento in Argomenti}


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
                                    f'/profilo per visulizzare le statistiche del tuo profilo (punti, emblemi, ecc...)\n'
                                    f'/info per visulizzare le informazioni sul funzionamento del bot\n',
                                    parse_mode='Markdown')


@filtro_privato
async def comando_nickname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 0:
        await update.message.reply_text('Devi inserire il nuovo nickname dopo il comando /nickname')
    elif len("".join(context.args)) > 30:
        await update.message.reply_text('Il nickname deve essere lungo massimo 30 caratteri')
    else:
        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        nickname_inserito = " ".join(context.args)

        if player.nickname == nickname_inserito:
            await update.message.reply_text('Il nickname inserito è già il tuo nickname attuale')
            return

        other_players = await PlayerDAO(database_manager).do_retrieve_by_nickname(nickname_inserito)

        if other_players is not None:
            for other_player in other_players:
                if nickname_inserito == other_player.get_nickname():
                    await update.message.reply_text('Il nickname inserito è già stato scelto da un altro utente')
                    return

        player.set_nickname(" ".join(context.args))
        await PlayerDAO(database_manager).do_update(player)
        await update.message.reply_text(f'Nickname aggiornato con successo!')


@filtro_privato
async def comando_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    opzioni = [
        [
            InlineKeyboardButton(text=Argomenti.CONCETTI_BASE.value, url='https://t.me/+5dJJ2GLVTCBhOTNk'),
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
        f'Ecco le informazioni del tuo profilo:\nNickname: *{player.get_nickname()}*\nPunteggio ottenuto tra tutti i quiz svolti: *{player.get_punteggio_totale()}*',
        parse_mode='Markdown')


@filtro_privato
async def comando_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (f"Il funzionamento del bot è molto semplice!\n"
            f"Una volta selezionato l\'argomento su cui vuoi fare il quiz dovrai rispondere correttamente alla domande per ottenere punti ed altre ricompense.\n"
            f"Potrai utilizare un sacco di potenziamenti:\n")

    for powerup in list(Powerups):
        text += f"*{powerup.nome()}*:  {powerup.descrizione()}.\n"

    await update.message.reply_text(text, parse_mode='Markdown')


@filtro_pubblico
async def comando_start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(text="Inizia il quiz 🚀", callback_data="avvia_quiz"),
        ]
    ]

    messaggio = await bot.send_message(text="Premi il bottone per iniziare il quiz 👇🏻", chat_id=update.message.chat_id,
                                       reply_markup=InlineKeyboardMarkup(keyboard))

    keyboard = [
        [
            # InlineKeyboardButton(
            #     text=f"Partecipo al quiz ✅\n({len(players_in_quiz[update.effective_chat.title])} partecipanti)",
            #     callback_data="aggiungi_partecipante"),
            InlineKeyboardButton(text=f"Partecipo al quiz ✅", callback_data="aggiungi_partecipante"),
        ],
        [
            InlineKeyboardButton(text="Non partecipo al quiz ❌", callback_data="rimuovi_partecipante"),
        ]
    ]

    messaggio_opzioni = await bot.send_message(
        text=f"Seleziona l'opzione 👇🏻",
        chat_id=update.message.chat_id,
        reply_markup=InlineKeyboardMarkup(keyboard))

    await SettingsDAO(database_manager).do_delete()
    await SettingsDAO(database_manager).do_save(Settings(messaggio_opzioni.message_id))

    try:
        await context.bot.pin_chat_message(chat_id=update.message.chat_id, message_id=messaggio.message_id)
    except Exception as e:
        print(f"Impossibile fissare il messaggio: {e}")


async def bottone_aggiungi_partecipante(update: Update, context: CallbackContext) -> None:
    # aggiungere controllo quiz attivo
    nome_gruppo = update.effective_chat.title
    if update.effective_user.id not in players_in_quiz[nome_gruppo]:

        if quiz_attivi[nome_gruppo]:
            await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                            text=f"Quiz su {nome_gruppo} già in corso, attendi ⏳", show_alert=False)
            return

        players_in_quiz[nome_gruppo].append(update.effective_user.id)
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Aggiunto al quiz su {nome_gruppo} ✅", show_alert=False)

        # Aggiorna il contatore dei partecipanti
        # stringa_partecipanti = f"Partecipo al quiz ✅\n({len(players_in_quiz[nome_gruppo])} partecipanti)"
        # numero_membri = await ottieni_numero_membri(update, context)
        # print(f"Numero membri: {numero_membri}")
        # if numero_membri is not None:
        #     stringa_partecipanti = f"Partecipo al quiz ✅\n{len(players_in_quiz[nome_gruppo])}/{numero_membri-1}"

        # stringa_partecipanti = f"Partecipo al quiz ✅"
        #
        # keyboard = [
        #     [
        #         InlineKeyboardButton(
        #             text=stringa_partecipanti,
        #             callback_data="aggiungi_partecipante"),
        #     ],
        #     [
        #         InlineKeyboardButton(text="Non partecipo al quiz ❌", callback_data="rimuovi_partecipante"),
        #     ]
        # ]
        # messaggio_opzioni = (await SettingsDAO(database_manager).do_retrieve()).get_messaggio_opzioni()
        #
        # await bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
        #                                     message_id=messaggio_opzioni,
        #                                     reply_markup=InlineKeyboardMarkup(keyboard))

        context.bot_data.update({
            update.effective_user.id: {
                "nickname": (
                    await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)).get_nickname(),
                "punteggio_quiz_corrente": {argomento.value: 0 for argomento in Argomenti},
                "streak": 1,
                "powerups": {powerup.nome(): False for powerup in Powerups},
            }
        })

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Sei già stato aggiunto al quiz su {nome_gruppo} ⚠", show_alert=False)
        return


async def resetta_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE, job_name) -> None:

    context.bot_data.update({
        update.effective_user.id: {
            "nickname": (
                await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)).get_nickname(),
            "punteggio_quiz_corrente": {argomento.value: 0 for argomento in Argomenti},
            "streak": 1,
            "powerups": {powerup.nome(): False for powerup in Powerups},
        }
    })
    players_in_quiz[update.effective_chat.title] = []
    quiz_attivi[update.effective_chat.title] = False


async def bottone_rimuovi_partecipante(update: Update, context: CallbackContext) -> None:
    # aggiungere controllo quiz attivo
    nome_gruppo = update.effective_chat.title
    if update.effective_user.id in players_in_quiz[nome_gruppo]:

        if quiz_attivi[nome_gruppo]:
            await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                            text=f"Quiz su {nome_gruppo} già in iniziato, attendi ⏳", show_alert=False)
            return

        players_in_quiz[nome_gruppo].remove(update.effective_user.id)
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Rimosso dal quiz su {nome_gruppo} ❌", show_alert=False)

        # Aggiorna il contatore dei partecipanti
        # stringa_partecipanti = f"Partecipo al quiz ✅\n({len(players_in_quiz[nome_gruppo])} partecipanti)"
        # numero_membri = await ottieni_numero_membri(update, context)
        # if numero_membri is not None:
        #     print(f"Numero membri: {numero_membri}")
        #     stringa_partecipanti = f"Partecipo al quiz ✅\n{len(players_in_quiz[nome_gruppo])}/{numero_membri-1}"

        # stringa_partecipanti = f"Partecipo al quiz ✅"
        # keyboard = [
        #     [
        #         InlineKeyboardButton(
        #             text=stringa_partecipanti,
        #             callback_data="aggiungi_partecipante"),
        #     ],
        #     [
        #         InlineKeyboardButton(text="Non partecipo al quiz ❌", callback_data="rimuovi_partecipante"),
        #     ]
        # ]
        #
        # messaggio_opzioni = (await SettingsDAO(database_manager).do_retrieve()).get_messaggio_opzioni()
        #
        # await bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
        #                                     message_id=messaggio_opzioni,
        #                                     reply_markup=InlineKeyboardMarkup(keyboard))

        if update.effective_user.id in context.bot_data:
            del context.bot_data[update.effective_user.id]

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei attualmente nel quiz su {nome_gruppo} ⚠", show_alert=False)
    return


# async def ottieni_numero_membri(update: Update, context: CallbackContext) -> int:
#     print(f"Ottengo il numero dei membri")
#     chat_id = update.effective_chat.id
#     try:
#         chat = await context.bot.get_chat(chat_id)
#         if chat and chat.type in ("group", "supergroup"):
#             return chat.get_members_count()
#     except Exception as e:
#         print(f"Errore durante il recupero del conteggio dei membri: {str(e)}")
#
#     return None


async def bottone_avvia_quiz_jobs(update: Update, context: CallbackContext) -> None:
    nome_gruppo = update.effective_chat.title

    if not quiz_attivi[nome_gruppo]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Avvio quiz su {nome_gruppo} in corso 🚀", show_alert=False)

        quiz_attivi[nome_gruppo] = True
    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Quiz su {nome_gruppo} già in corso, attendi ⏳", show_alert=False)
        return


    domande = await DomandaDAO(database_manager).do_retrieve_by_argomento(nome_gruppo)

    tempo_prossima_domanda = datetime.now() + timedelta(seconds=2)
    intervallo_domande = 2
    for numero_domanda, domanda in enumerate(domande):
        function = partial(invia_domanda, update, context, domanda, numero_domanda + 1, len(domande),
                           tempo_prossima_domanda)

        context.job_queue.run_once(function, when=intervallo_domande, name="invia_domanda")

        function = partial(manda_meme, update, context, domanda)

        context.job_queue.run_once(function, when=intervallo_domande + domanda.get_tempoRisposta(), name="manda_meme")
        tempo_prossima_domanda = tempo_prossima_domanda + timedelta(seconds=domanda.get_tempoRisposta()) + timedelta(
            seconds=5)

        intervallo_domande = intervallo_domande + domanda.get_tempoRisposta() + 5

    function = partial(mostra_classifica, update, context)
    context.job_queue.run_once(function, when=intervallo_domande + 2, name="mostra_classifica")

    function = partial(cancella_messaggi, update, context)
    context.job_queue.run_once(function, when=intervallo_domande + 3, name="cancella_messaggi")

    function = partial(resetta_quiz, update, context)
    context.job_queue.run_once(function, when=intervallo_domande + 3, name="resetta_quiz")


async def cancella_messaggi(update: Update, context: ContextTypes.DEFAULT_TYPE, job_name) -> None:
    messaggio = await bot.send_message(text="Sto per cancellare la chat 👇🏻", chat_id=update.effective_chat.id)
    messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    await asyncio.sleep(5)

    for messaggio_per_lobby in messaggi_per_lobby[update.effective_chat.title]:
        try:
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=messaggio_per_lobby)
        except Exception as e:
            print(f"Impossibile cancellare il messaggio: {e}")

    messaggi_per_lobby[update.effective_chat.title] = []


async def manda_meme(update: Update, context: ContextTypes.DEFAULT_TYPE, domanda: Domanda, job_name) -> None:
    if domanda.has_meme():
        try:
            with open(domanda.get_meme(), "rb") as meme:
                messaggio = await bot.send_photo(chat_id=update.effective_chat.id, photo=meme)
                messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)
        except Exception as e:
            print(f"Impossibile inviare il meme: {e}")


async def invia_domanda(update: Update, context: ContextTypes.DEFAULT_TYPE, domanda: Domanda, numero_domanda: int,
                        totale_domande: int, tempo_inizio: datetime, job_name) -> None:
    risposte = [domanda.rispostaA, domanda.rispostaB, domanda.rispostaC, domanda.rispostaD]

    righe_tastiera_powerups = []
    riga = []

    for powerup in list(Powerups):
        bottone = InlineKeyboardButton(text=powerup.nome(), callback_data=f"{powerup.nome()}")
        riga.append(bottone)

        if len(riga) == 2:
            righe_tastiera_powerups.append(riga)
            riga = []

    if riga:
        righe_tastiera_powerups.append(riga)

    tastiera_powerups = InlineKeyboardMarkup(righe_tastiera_powerups)
    messaggio = await bot.send_poll(chat_id=update.effective_chat.id,
                                    question=f"Domanda: {numero_domanda}/{totale_domande}\nDifficoltà: {domanda.get_difficoltaString()}\n{domanda.get_testo()}",
                                    options=risposte,
                                    type=Poll.QUIZ, correct_option_id=int(domanda.get_rispostaCorretta()) - 1,
                                    is_anonymous=False, open_period=domanda.tempoRisposta,
                                    reply_markup=tastiera_powerups)

    messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    context.bot_data.update({
        messaggio.poll.id: {
            "chat_id": update.effective_chat.id,
            "chat_title": update.effective_chat.title,
            "message_id": messaggio.message_id,
            "risposta_corretta": int(domanda.get_rispostaCorretta()),
            "tempo_inizio": tempo_inizio,
            "durata_risposta": domanda.get_tempoRisposta(),
            "difficolta": int(domanda.get_difficolta())
        }
    })


async def handle_powerup_streak(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    print(context.bot_data[update.effective_user.id]["powerups"])

    if not context.bot_data[update.effective_user.id]["powerups"][Powerups.STREAK.nome()]:
        context.bot_data[update.effective_user.id]["powerups"][Powerups.STREAK.nome()] = True

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.STREAK.nome()} utilizato!", show_alert=False)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.STREAK.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.STREAK.nome()} già utilizzato! ⚠", show_alert=False)


async def processa_risposta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = await PlayerDAO(database_manager).do_retrieve_by_id(update.poll_answer.user.id)

    if int(player.get_id()) not in context.bot_data.keys():
        return

    quiz = context.bot_data[update.poll_answer.poll_id]
    player_in_quiz = context.bot_data[int(player.get_id())]

    if update.poll_answer.option_ids[0] == int(quiz["risposta_corretta"]) - 1:

        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] += quiz["difficolta"] * 10 * player_in_quiz[
            "streak"] + await calcola_punteggio_tempo_risposta(update, context, quiz["tempo_inizio"],
                                                               quiz["durata_risposta"])

        if player_in_quiz["streak"] <= 1.5:
            player_in_quiz["streak"] += 0.1

    else:
        player_in_quiz["streak"] = 1
        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] -= float(quiz["difficolta"]) * 1.5

    if player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] < 0:
        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] = 0


async def calcola_punteggio_tempo_risposta(update: Update, context: ContextTypes.DEFAULT_TYPE, tempo_inizio,
                                           durata_risposta) -> None:
    return round(
        float(timedelta(seconds=durata_risposta).total_seconds() - (datetime.now() - tempo_inizio).total_seconds()),
        2) * 10


async def mostra_classifica(update: Update, context: ContextTypes.DEFAULT_TYPE, job_name) -> None:
    player_ids = players_in_quiz[update.effective_chat.title]
    classifica = []
    for id in player_ids:
        classifica.append(context.bot_data[id])

    classifica.sort(key=lambda x: x["punteggio_quiz_corrente"][update.effective_chat.title], reverse=True)

    text = f"Ecco la classifica del quiz su *{update.effective_chat.title}*\n"
    for posizione, player in enumerate(classifica, start=1):
        text += f"*{posizione}°* - *{player['nickname']}* - *{round(player['punteggio_quiz_corrente'][update.effective_chat.title], 2)}* punti\n"

    if len(classifica) > 0:
        messaggio = await bot.send_message(text=text, chat_id=update.effective_chat.id, parse_mode='Markdown')
    else:
        messaggio = await bot.send_message(text="Nessun partecipante al quiz - classifica vuota",
                                           chat_id=update.effective_chat.id)

    messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)


@filtro_pubblico
async def comando_stop_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome_gruppo = update.effective_chat.title

    if quiz_attivi[nome_gruppo]:
        quiz_attivi[nome_gruppo] = False
        print(f"Quiz su {nome_gruppo} terminato")
    else:
        print(f"Non c'è nessun quiz su {nome_gruppo}")


def main():
    app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()
    app.add_handler(CommandHandler("start", comando_start))
    app.add_handler(CommandHandler("nickname", comando_nickname))
    app.add_handler(CommandHandler("quiz", comando_quiz))
    app.add_handler(CommandHandler("profilo", comando_profilo))
    app.add_handler(CommandHandler("info", comando_info))
    app.add_handler(CommandHandler("avvia_quiz", comando_start_quiz))
    app.add_handler(CommandHandler("stop_quiz", comando_stop_quiz))

    app.add_handler(CallbackQueryHandler(bottone_avvia_quiz_jobs, pattern="avvia_quiz"))
    app.add_handler(CallbackQueryHandler(bottone_aggiungi_partecipante, pattern="aggiungi_partecipante"))
    app.add_handler(CallbackQueryHandler(bottone_rimuovi_partecipante, pattern="rimuovi_partecipante"))

    app.add_handler(CallbackQueryHandler(handle_powerup_streak, pattern=Powerups.STREAK.nome()))

    app.add_handler(PollAnswerHandler(processa_risposta))

    app.run_polling()


if __name__ == '__main__':
    main()
