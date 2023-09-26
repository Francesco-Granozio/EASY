import asyncio
import os
import random
from datetime import datetime, timedelta
from functools import partial
from typing import Any

import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Poll
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext, \
    PollAnswerHandler

from Argomenti import Argomenti
from DatabaseManager import DatabaseManager
from Domanda import Domanda
from DomandaDAO import DomandaDAO
from Player import Player
from PlayerDAO import PlayerDAO
from Powerups import Powerups
from Settings import Settings
from SettingsDAO import SettingsDAO
from filtri import filtro_privato, filtro_pubblico

bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'))
DB_PATH = r"C:\Shared\Unisa\Tesi\EASY\database.db"
database_manager = DatabaseManager(DB_PATH)

quiz_attivi = {argomento.value: False for argomento in Argomenti}
messaggi_per_lobby = {argomento.value: [] for argomento in Argomenti}
players_in_quiz = {argomento.value: [] for argomento in Argomenti}


@filtro_privato
async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # se il player non è registrato nel database, lo registro e gli invio un messaggio di benvenuto
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
    # controllo che il player abbia inserito un nickname e non solo /nickname
    if len(context.args) == 0:
        await update.message.reply_text('Devi inserire il nuovo nickname dopo il comando /nickname')
    # nickname lungo massimo 30 caratteri
    elif len("".join(context.args)) > 30:
        await update.message.reply_text('Il nickname deve essere lungo massimo 30 caratteri')
    else:
        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        nickname_inserito = " ".join(context.args)

        # contollo se il nick è uguale a quello attuale
        if player.nickname == nickname_inserito:
            await update.message.reply_text('Il nickname inserito è già il tuo nickname attuale')
            return

        other_players = await PlayerDAO(database_manager).do_retrieve_by_nickname(nickname_inserito)

        # controllo l'univocità del nickname
        if other_players is not None:
            for other_player in other_players:
                if nickname_inserito == other_player.get_nickname():
                    await update.message.reply_text('Il nickname inserito è già stato scelto da un altro player')
                    return

        player.set_nickname(nickname_inserito)
        await PlayerDAO(database_manager).do_update(player)
        await update.message.reply_text(f'Nickname aggiornato con successo!')


@filtro_privato
async def comando_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # tastiera inline che permette di scegliere la lobby (gruppo) del quiz
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
    # controllo se il player è registrato nel database
    player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
    if player is None:
        await update.message.reply_text('Devi prima registrarti con il comando /start')
        return

    await update.message.reply_text(
        f'Ecco le informazioni del tuo profilo:\nNickname: *{player.get_nickname()}*\nPunteggio ottenuto tra tutti i quiz svolti: *{player.get_punteggio_totale()}*',
        parse_mode='Markdown')


@filtro_privato
async def comando_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # mostro le informazioni per il funzionamento del bot
    text = (f"Il funzionamento del bot è molto semplice!\n"
            f"Una volta selezionato l\'argomento su cui vuoi fare il quiz dovrai rispondere correttamente alla domande per ottenere punti ed altre ricompense.\n"
            f"Potrai utilizare un sacco di potenziamenti:\n")

    for powerup in list(Powerups):
        text += f"*{powerup.nome()}*:  {powerup.descrizione()}.\n"

    await update.message.reply_text(text, parse_mode='Markdown')


@filtro_pubblico
async def comando_start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # comando che deve essere eseguito solo dall'admin del gruppo e permette di generare i
    # 2 bottoni per iniziare il quiz e per aggiungere/rimuovere un partecipante e fissa il primo
    keyboard = [
        [
            InlineKeyboardButton(text="Inizia il quiz 🚀", callback_data="avvia_quiz"),
        ]
    ]

    messaggio = await bot.send_message(text="Premi il bottone per iniziare il quiz 👇🏻", chat_id=update.message.chat_id,
                                       reply_markup=InlineKeyboardMarkup(keyboard))

    keyboard = [
        [
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

    # salvo l'id del messaggio fissato così sarà sempre attivo anche se il bot viene riavviato
    await SettingsDAO(database_manager).do_delete()
    await SettingsDAO(database_manager).do_save(Settings(messaggio_opzioni.message_id))

    try:
        await context.bot.pin_chat_message(chat_id=update.message.chat_id, message_id=messaggio.message_id)
    except Exception as e:
        print(f"Impossibile fissare il messaggio: {e}")


async def bottone_aggiungi_partecipante(update: Update, context: CallbackContext) -> None:
    nome_gruppo = update.effective_chat.title
    # se il player non è già stato aggiunto al quiz, lo aggiungo
    if update.effective_user.id not in players_in_quiz[nome_gruppo]:

        # se il quiz è già in corso avviso il player di aspettare
        if quiz_attivi[nome_gruppo]:
            await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                            text=f"Quiz su {nome_gruppo} già in corso, attendi ⏳", show_alert=False)
            return

        # aggiungo il player alla lista dei partecipanti
        players_in_quiz[nome_gruppo].append(update.effective_user.id)
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Aggiunto al quiz su {nome_gruppo} ✅", show_alert=False)

        # salvo alcune informazioni del player come
        # nickname, punteggio quiz corrente, streak e powerups
        # powerups è un dizionario che contiene tutti i powerups e per ogni powerup indica se è disponible o meno
        # False indica non disponible, True indica disponibile
        context.bot_data.update({
            update.effective_user.id: {
                "nickname": (
                    await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)).get_nickname(),
                "punteggio_quiz_corrente": {argomento.value: 0 for argomento in Argomenti},
                "streak": 1,
                "powerups": {powerup.nome(): False for powerup in Powerups}
            }
        })

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Sei già stato aggiunto al quiz su {nome_gruppo} ⚠", show_alert=False)
        return


async def resetta_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE, job_name) -> None:
    # ripristino alcune informazioni del player come
    # nickname, punteggio quiz corrente, streak e powerups
    # powerups è un dizionario che contiene tutti i powerups e per ogni powerup indica se è disponible o meno
    # False indica non disponible, True indica disponibile
    context.bot_data.update({
        update.effective_user.id: {
            "nickname": (
                await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)).get_nickname(),
            "punteggio_quiz_corrente": {argomento.value: 0 for argomento in Argomenti},
            "streak": 1,
            "powerups": {powerup.nome(): False for powerup in Powerups}
        }
    })

    # siccome il metodo viene chiamato ogni volta che finisce un quizz
    # svuoto la lista dei partecipanti e setto il quiz come non attivo
    players_in_quiz[update.effective_chat.title] = []
    quiz_attivi[update.effective_chat.title] = False


async def bottone_rimuovi_partecipante(update: Update, context: CallbackContext) -> None:
    # controllo se il player è stato aggiunto al quiz
    nome_gruppo = update.effective_chat.title
    if update.effective_user.id in players_in_quiz[nome_gruppo]:

        # se il quiz è già in corso avviso il player di aspettare, non posso rimuoverlo durante il quiz
        if quiz_attivi[nome_gruppo]:
            await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                            text=f"Quiz su {nome_gruppo} già in iniziato, attendi ⏳", show_alert=False)
            return

        # rimuovo il player dalla lista dei partecipanti
        players_in_quiz[nome_gruppo].remove(update.effective_user.id)
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Rimosso dal quiz su {nome_gruppo} ❌", show_alert=False)

        # rimuovo alcune innformazioni del player
        if update.effective_user.id in context.bot_data:
            del context.bot_data[update.effective_user.id]

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei attualmente nel quiz su {nome_gruppo} ⚠", show_alert=False)
    return


async def bottone_avvia_quiz_jobs(update: Update, context: CallbackContext) -> None:
    # questa funzione avvia il quiz e manda le domande una dopo l'altra
    # manda anche i meme se presenti, mostra la classifica, cancella i messaggi e resetta il quiz
    # mostra i bottoni per l'invio dei riferimenti

    nome_gruppo = update.effective_chat.title

    # se il quiz è già in corso avviso il player di aspettare altrimenti lo avvio

    if not quiz_attivi[nome_gruppo]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Avvio quiz su {nome_gruppo} in corso 🚀", show_alert=False)

        quiz_attivi[nome_gruppo] = True
    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Quiz su {nome_gruppo} già in corso, attendi ⏳", show_alert=False)
        return

    domande = await DomandaDAO(database_manager).do_retrieve_by_argomento(nome_gruppo)
    random.shuffle(domande)

    # Calcola il tempo per la prossima domanda come 2 secondi nel futuro dall'istante corrente
    tempo_prossima_domanda = datetime.now() + timedelta(seconds=2)
    # Imposta un intervallo iniziale tra le domande a 2 secondi
    intervallo_domande = 2
    # Itera attraverso le domande e assegna loro un'azione da eseguire come job in un orario specifico
    for numero_domanda, domanda in enumerate(domande):
        function = partial(invia_domanda, update, context, domanda, numero_domanda + 1, len(domande),
                           tempo_prossima_domanda)

        # Programma l'esecuzione della funzione dopo un certo intervallo di tempo
        context.job_queue.run_once(function, when=intervallo_domande, name="invia_domanda")

        function = partial(manda_meme, update, context, domanda)
        context.job_queue.run_once(function, when=intervallo_domande + domanda.get_tempoRisposta(), name="manda_meme")

        # Aggiorna il tempo per la prossima domanda, considerando il tempo per rispondere e 5 secondi di intervallo
        tempo_prossima_domanda = tempo_prossima_domanda + timedelta(seconds=domanda.get_tempoRisposta()) + timedelta(
            seconds=5)

        # Aggiorna l'intervallo tra le domande considerando il tempo per rispondere e 5 secondi di intervallo
        intervallo_domande = intervallo_domande + domanda.get_tempoRisposta() + 5

    # Mostra la classifica dopo che tutte le domande sono state inviate
    function = partial(mostra_classifica, update, context)
    context.job_queue.run_once(function, when=intervallo_domande + 2, name="mostra_classifica")

    # Mostra pulsante per la visualizzazione dei riferimenti
    function = partial(invia_bottone_riferimenti, update, context, domande)
    context.job_queue.run_once(function, when=intervallo_domande + 3, name="mostra _bottone_riferimenti")

    # Cancella i messaggi dopo che tutte le domande sono state inviate
    function = partial(cancella_messaggi, update, context)
    context.job_queue.run_once(function, when=intervallo_domande + 4, name="cancella_messaggi")

    # Resetta il quiz dopo che tutte le domande sono state inviate
    function = partial(resetta_quiz, update, context)
    context.job_queue.run_once(function, when=intervallo_domande + 4, name="resetta_quiz")

    # Mostra i bottoni per l'invio dei riferimenti dopo che tutte le domande sono state inviate


async def invia_bottone_riferimenti(update: Update, context: ContextTypes.DEFAULT_TYPE, domande, job_name) -> None:
    # Questa funzione invia un pulsante per visualizzare i riferimenti alle domande del quiz.

    keyboard = [
        [
            InlineKeyboardButton(text=f"Visualizza riferimenti alle domande 🔍", callback_data="mostra_riferimenti"),
        ]
    ]

    # Salva le domande nel chat_data per poterle utilizzare nella funzione di callback.
    context.chat_data["domande"] = domande


    messaggio = await bot.send_message(
        text=f"👇🏻",
        chat_id=update.effective_chat.id,
        reply_markup=InlineKeyboardMarkup(keyboard))

    messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)


async def bottone_mostra_riferimenti(update: Update, context: CallbackContext) -> None:
    # Questa funzione mostra i riferimenti alle domande del quiz.

    if "domande" not in context.chat_data:
        return

    private_chat_id = update.effective_user.id
    domande = context.chat_data["domande"]

    text = f"Riferimenti alle domande:\n\n"

    # Aggiungi i riferimenti alle domande nel testo.
    for numero_domanda, domanda in enumerate(domande, start=1):
        if domanda.has_fonte():
            text += f"Domanda *{numero_domanda}*:\n"
            text += f"*{domanda.get_testo()}*\n\n"
            text += f"Argomento: *{domanda.get_argomento()}*\n"
            text += f"Difficoltà: *{domanda.get_difficoltaString()}*\n\n"
            text += f"Risposta A: *{domanda.get_rispostaA()}*\n"
            text += f"Risposta B: *{domanda.get_rispostaB()}*\n"
            text += f"Risposta C: *{domanda.get_rispostaC()}*\n"
            text += f"Risposta D: *{domanda.get_rispostaD()}*\n\n"
            text += f"Risposta corretta: *{domanda.get_rispostaCorretta_string()}*\n\n"
            text += f"Riferimenti: *{domanda.get_fonte()}*\n\n\n"

    # Invia i riferimenti al giocatore nella chat privata.
    await context.bot.send_message(chat_id=private_chat_id, text=text, parse_mode="Markdown")


async def cancella_messaggi(update: Update, context: ContextTypes.DEFAULT_TYPE, job_name) -> None:
    messaggio = await bot.send_message(text="Sto per cancellare la chat 👇🏻", chat_id=update.effective_chat.id)
    messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    await asyncio.sleep(5)

    # Cancella tutti i messaggi inviati dal bot, tranne i primi 2 pulsanti che non sono stati salvati
    for messaggio_per_lobby in messaggi_per_lobby[update.effective_chat.title]:
        try:
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=messaggio_per_lobby)
        except Exception as e:
            print(f"Impossibile cancellare il messaggio: {e}")

    # Una volta cancellati i messaggi, svuota la lista dei messaggi per questo gruppo/lobby.
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
    # Questa funzione invia una domanda sotto forma di sondaggio (poll) in una chat e configura le opzioni per i powerup.

    risposte = [domanda.rispostaA, domanda.rispostaB, domanda.rispostaC, domanda.rispostaD]

    # Configura la tastiera per i powerup.
    righe_tastiera_powerups = []
    riga = []

    for powerup in list(Powerups):

        bottone = InlineKeyboardButton(text=powerup.nome(), callback_data=f"{powerup.nome()}")
        riga.append(bottone)

        if len(riga) == 2:
            righe_tastiera_powerups.append(riga)
            riga = []

    # Se rimane una riga incompleta, aggiungila comunque.
    if riga:
        righe_tastiera_powerups.append(riga)

    tastiera_powerups = InlineKeyboardMarkup(righe_tastiera_powerups)

    messaggio = await bot.send_poll(chat_id=update.effective_chat.id,
                                    question=f"Domanda: {numero_domanda}/{totale_domande}\nDifficoltà: {domanda.get_difficoltaString()}\n{domanda.get_testo()}",
                                    options=risposte,
                                    type=Poll.QUIZ, correct_option_id=int(domanda.get_rispostaCorretta()) - 1,
                                    is_anonymous=False, open_period=domanda.get_tempoRisposta(),
                                    reply_markup=tastiera_powerups)

    messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    # Aggiorna il bot_data con i dettagli del sondaggio corrente.
    context.bot_data.update({
        messaggio.poll.id: {
            "chat_id": update.effective_chat.id,
            "chat_title": update.effective_chat.title,
            "message_id": messaggio.message_id,
            "risposta_corretta": int(domanda.get_rispostaCorretta()),
            "tempo_inizio": tempo_inizio,
            "durata_risposta": domanda.get_tempoRisposta(),
            "difficolta": int(domanda.get_difficolta()),
            "risposte": [domanda.get_rispostaA(), domanda.get_rispostaB(), domanda.get_rispostaC(),
                         domanda.get_rispostaD()],
            "id_player_gioco_di_potere": None
        }
    })


async def handle_powerup_streak(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Streak" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Streak".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.STREAK.nome()]:

        # Imposta il powerup "Streak" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.STREAK.nome()] = False

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.STREAK.nome()} utilizato!", show_alert=False)

        # Ottieni il nickname del player e mostra che ha usato il powerup.
        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.STREAK.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.STREAK.nome()} non disponibile! ⚠", show_alert=False)


async def handle_powerup_regalo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Regalo" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Regalo".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.REGALO.nome()]:

        # Imposta il powerup "Regalo" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.REGALO.nome()] = False

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.REGALO.nome()} utilizato!", show_alert=False)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.REGALO.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.REGALO.nome()} non disponibile! ⚠", show_alert=False)


async def handle_powerup_doppio_rischio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Doppio Rischio" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Doppio Rischio".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO_RISCHIO.nome()]:

        # Imposta il powerup "Doppio Rischio" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO_RISCHIO.nome()] = False

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.DOPPIO_RISCHIO.nome()} utilizato!", show_alert=False)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.DOPPIO_RISCHIO.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.DOPPIO_RISCHIO.nome()} non disponibile! ⚠",
                                        show_alert=False)


async def handle_powerup_doppio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Doppio" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Doppio".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO.nome()]:

        # Imposta il powerup "Doppio" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO.nome()] = False

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.DOPPIO.nome()} utilizato!", show_alert=False)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.DOPPIO.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.DOPPIO.nome()} non disponibile! ⚠",
                                        show_alert=False)


async def handle_powerup_50_e_50(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "50 e 50" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "50 e 50".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.CINQUANTA_CINQUANTA.nome()]:

        # Imposta il powerup "50 e 50" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.CINQUANTA_CINQUANTA.nome()] = False

        risposte = context.bot_data[update.callback_query.message.poll.id]["risposte"]
        indice_risposta_corretta = context.bot_data[update.callback_query.message.poll.id]["risposta_corretta"] - 1

        # Ottieni la risposta corretta
        risposta_corretta = risposte[indice_risposta_corretta]

        # Ottieni una copia delle risposte errate (tutte tranne quella corretta)
        risposte_errate = [risposta for i, risposta in enumerate(risposte) if i != indice_risposta_corretta]

        # Seleziona casualmente una risposta errata
        risposta_errata = random.choice(risposte_errate)

        # Crea una nuova lista contenente una risposta corretta e una errata
        risposte_50_e_50 = [risposta_corretta, risposta_errata]

        # Mescola gli elementi nella nuova lista
        random.shuffle(risposte_50_e_50)

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.CINQUANTA_CINQUANTA.nome()} utilizzato!\n"
                                             f"1️⃣ {risposte_50_e_50[0]}\n"
                                             f"2️⃣ {risposte_50_e_50[1]}",
                                        show_alert=True)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.CINQUANTA_CINQUANTA.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

        # Imposta il powerup "50 e 50" come disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.CINQUANTA_CINQUANTA.nome()] = True

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.CINQUANTA_CINQUANTA.nome()} non disponibile! ⚠",
                                        show_alert=False)


async def handle_powerup_gomma(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Gomma" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Gomma".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.GOMMA.nome()]:

        # Imposta il powerup "Gomma" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.GOMMA.nome()] = False

        risposte = context.bot_data[update.callback_query.message.poll.id]["risposte"]
        indice_risposta_corretta = context.bot_data[update.callback_query.message.poll.id]["risposta_corretta"] - 1

        # Ottieni una copia delle risposte errate (tutte tranne quella corretta)
        risposte_errate = [risposta for i, risposta in enumerate(risposte) if i != indice_risposta_corretta]

        # Seleziona casualmente una risposta errata da eliminare
        risposta_da_eliminare = random.choice(risposte_errate)

        # Rimuovi la risposta dalla lista originale
        risposte.remove(risposta_da_eliminare)

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.GOMMA.nome()} utilizzato!\n"
                                             f"Una risposta sbagliata è stata rimossa.\n"
                                             f"1️⃣ {risposte[0]}\n"
                                             f"2️⃣ {risposte[1]}\n"
                                             f"3️⃣ {risposte[2]}",
                                        show_alert=True)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.GOMMA.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

        # Imposta il powerup "Gomma" come disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.GOMMA.nome()] = True

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.GOMMA.nome()} non disponibile! ⚠",
                                        show_alert=False)


async def handle_powerup_immunita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Immunità" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Immunità".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.IMMUNITA.nome()]:

        # Imposta il powerup "Immunità" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.IMMUNITA.nome()] = False

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.IMMUNITA.nome()} utilizato!", show_alert=False)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.IMMUNITA.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.IMMUNITA.nome()} non disponibile! ⚠", show_alert=False)


async def handle_powerup_gioco_di_potere(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Questa funzione gestisce l'uso del powerup "Gioco di Potere" da parte di un player durante il quiz.

    # Controlla se il player è un partecipante del quiz.
    if update.effective_user.id not in players_in_quiz[update.effective_chat.title]:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Non sei un partecipante del quiz su {update.effective_chat.title} ⚠",
                                        show_alert=False)
        return

    # Verifica se il player ha già utilizzato il powerup "Gioco di Potere".
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.GIOCO_DI_POTERE.nome()]:

        # Imposta il powerup "Gioco di Potere" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.GIOCO_DI_POTERE.nome()] = False

        # Salvo l'id del player che ha usato il powerup "Gioco di Potere", mi servirà per il calcolo dei punti.
        context.bot_data[update.callback_query.message.poll.id]["id_player_gioco_di_potere"] = update.effective_user.id

        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.GIOCO_DI_POTERE.nome()} utilizato!", show_alert=False)

        player = await PlayerDAO(database_manager).do_retrieve_by_id(update.effective_user.id)
        messaggio = await bot.send_message(
            text=f"Powerup *{Powerups.GIOCO_DI_POTERE.nome()}* utilizzato da *{player.get_nickname()}*!",
            chat_id=update.effective_chat.id, parse_mode='Markdown')

        messaggi_per_lobby[update.effective_chat.title].append(messaggio.message_id)

    else:
        await bot.answer_callback_query(callback_query_id=update.callback_query.id,
                                        text=f"Powerup {Powerups.GIOCO_DI_POTERE.nome()} non disponibile! ⚠",
                                        show_alert=False)


async def processa_risposta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Questa funzione è responsabile di gestire le risposte dei players alle domande del quiz e
    di calcolare il punteggio e gli effetti delle risposte corrette o errate. Ecco come funziona:

    Ottiene i dettagli del player che ha inviato la risposta.
    Verifica se il player è coinvolto in un quiz attivo. Se non lo è, la funzione si interrompe.
    Ottiene i dettagli del quiz attivo e del player nel quiz.
    Calcola il punteggio e gli effetti della risposta corretta o errata, tra cui powerup e bonus.

    Se la risposta del player è corretta, calcola il punteggio basato su vari fattori, come il tempo di risposta,
    i powerup e il gioco di potere attivo.
    Aggiunge il punteggio alla classifica del player e aggiorna lo "streak" se è inferiore a 1.5.

    Se la risposta del player è errata, calcola il punteggio per il powerup "Doppio Rischio" e il gioco di potere attivo.
    Sottrae il punteggio per la risposta errata dalla classifica del player.

    Assicura che il punteggio del player non sia inferiore a 0."""

    player = await PlayerDAO(database_manager).do_retrieve_by_id(update.poll_answer.user.id)

    # Verifica se il player è coinvolto in un quiz attivo.
    if int(player.get_id()) not in context.bot_data.keys():
        return

    # Ottieni i dettagli del quiz attivo e del player nel quiz.
    quiz = context.bot_data[update.poll_answer.poll_id]
    player_in_quiz = context.bot_data[int(player.get_id())]

    # Se l'utente risponde correttamente alla domanda, gli vengono dati anche i punti del powerup "regalo", se attivo
    await calcola_punteggio_powerup_regalo(update, context, quiz, player_in_quiz)

    # Verifica se la risposta del giocatore è corretta.
    if update.poll_answer.option_ids[0] == int(quiz["risposta_corretta"]) - 1:

        # Calcola il punteggio per il powerup "Streak".
        await calcola_punteggio_powerup_streak(update, context, player_in_quiz)

        # Calcola il punteggio basato sul tempo di risposta del giocatore.
        punti_tempo_risposta = await calcola_punteggio_tempo_risposta(update, context, quiz["tempo_inizio"],
                                                                      quiz["durata_risposta"])

        # Calcola il punteggio per il powerup "Doppio Rischio" restituisce 2 se è attivo, 1 altrimenti.
        punti_doppio_rischio = await calcola_punteggio_powerup_doppio_rischio(update, context, True)

        # Calcola il punteggio per il powerup "Doppio" restituisce 2 se è attivo, 1 altrimenti.
        punti_doppi = await calcola_punteggio_powerup_doppio(update, context)

        # Calcola il punteggio per il gioco di potere attivo.
        punti_gioco_di_potere = await calcola_punteggio_gioco_di_potere(update, context, quiz, player_in_quiz, player,
                                                                        True)

        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] += ((quiz["difficolta"] * 10 * player_in_quiz[
            "streak"] + punti_tempo_risposta)) * punti_doppio_rischio * punti_doppi * punti_gioco_di_potere

        if player_in_quiz["streak"] <= 1.5:
            player_in_quiz["streak"] += 0.1

        # regala un powerup con probabilità 1/3 se la risposta è corretta
        await regala_powerup(update, context, player_in_quiz, quiz)

    else:

        # Se la risposta del giocatore è errata, esegui il controllo dell'immunità.
        if await calcola_punteggio_immunita(update, context):
            return

        # Calcola il punteggio per il powerup "Doppio Rischio" restituisce 2 se è attivo, 1 altrimenti.
        punti_doppio_rischio = await calcola_punteggio_powerup_doppio_rischio(update, context, False)
        # Calcola il punteggio per il gioco di potere attivo.
        punti_gioco_di_potere = await calcola_punteggio_gioco_di_potere(update, context, quiz, player_in_quiz, player,
                                                                        False)

        player_in_quiz["streak"] = 1
        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] -= (
                (float(quiz["difficolta"]) * 5) * punti_doppio_rischio * punti_gioco_di_potere)

    if player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] < 0:
        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] = 0

    # Aggiorna il punteggio totale del giocatore nel database.
    player.set_punteggio_totale(
        player.get_punteggio_totale() + player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]])
    await PlayerDAO(database_manager).do_update(player)


async def regala_powerup(update: Update, context: ContextTypes.DEFAULT_TYPE, player_in_quiz, quiz) -> None:
    # regala un powerup con probabilità 1/3 se la risposta è corretta

    probabilita = random.randint(0, 2)

    if probabilita == 0:
        powerup_disponibili = [powerup for powerup in list(Powerups) if
                               not context.bot_data[update.effective_user.id]["powerups"][powerup.nome()]]

        if len(powerup_disponibili) == 0:
            return

        powerup_scelto = random.choice(powerup_disponibili)

        # Attiva il powerup scelto per il giocatore corrente.
        context.bot_data[update.effective_user.id]["powerups"][powerup_scelto.nome()] = True

        messaggio = await bot.send_message(chat_id=quiz["chat_id"],
                                           text=f"*{player_in_quiz['nickname']}* ha ricevuto il powerup *{powerup_scelto.nome()}*!",
                                           parse_mode="Markdown")
        messaggi_per_lobby[quiz["chat_title"]].append(messaggio.message_id)


async def calcola_punteggio_powerup_streak(update: Update, context: ContextTypes.DEFAULT_TYPE, player_in_quiz) -> None:
    # la streak con il powerup attivato può superare il 1.5

    # Verifica se il powerup "Streak" è attivo per il giocatore.
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.STREAK.nome()]:
        # Imposta il powerup "Streak" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.STREAK.nome()] = True
        player_in_quiz["streak"] += 0.3


async def calcola_punteggio_powerup_regalo(update: Update, context: ContextTypes.DEFAULT_TYPE, quiz,
                                           player_in_quiz) -> None:
    # Verifica se il powerup "Regalo" è attivo per il giocatore.
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.REGALO.nome()]:
        # Imposta il powerup "Regalo" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.REGALO.nome()] = True

        # Aggiungi un bonus di punteggio al giocatore. Il bonus è casuale tra 10 e 30 punti * la difficoltà (1, 3).
        player_in_quiz["punteggio_quiz_corrente"][quiz["chat_title"]] += random.randint(10, 30) * quiz["difficolta"]


async def calcola_punteggio_powerup_doppio_rischio(update: Update, context: ContextTypes.DEFAULT_TYPE,
                                                   isCorrect) -> None:
    # Verifica se il powerup "Doppio Rischio" è attivo per il giocatore.
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO_RISCHIO.nome()]:
        # Imposta il powerup "Doppio Rischio" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO_RISCHIO.nome()] = True
        return 2

    return 1


async def calcola_punteggio_powerup_doppio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Verifica se il powerup "Doppio" è attivo per il giocatore.
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO.nome()]:
        # Imposta il powerup "Doppio" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.DOPPIO.nome()] = True
        return 2

    return 1


async def calcola_punteggio_immunita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Verifica se il powerup "Immunità" è attivo per il giocatore.
    if context.bot_data[update.effective_user.id]["powerups"][Powerups.IMMUNITA.nome()]:
        # Imposta il powerup "Immunità" come non disponibile.
        context.bot_data[update.effective_user.id]["powerups"][Powerups.IMMUNITA.nome()] = True
        return True

    return False


async def calcola_punteggio_gioco_di_potere(update: Update, context: ContextTypes.DEFAULT_TYPE, quiz,
                                            player_in_quiz, player, isCorrect) -> None:
    # Verifica se c'è un gioco di potere attivo nella domanda corrente.
    if quiz["id_player_gioco_di_potere"] is not None:

        # Verifica se il giocatore attuale è il possessore del gioco di potere.
        if quiz["id_player_gioco_di_potere"] == int(player.get_id()):

            # Attiva il powerup "Gioco di Potere" per il giocatore.
            context.bot_data[update.effective_user.id]["powerups"][Powerups.GIOCO_DI_POTERE.nome()] = True

            # Se la risposta è corretta, restituisci un bonus di punteggio (2x).
            if isCorrect:
                return 2

        else:
            context.bot_data[update.effective_user.id]["powerups"][Powerups.GIOCO_DI_POTERE.nome()] = True

            # Se la risposta è errata, restituisci un malus di punteggio (2x).
            if not isCorrect:
                return 2

    # Se non c'è gioco di potere attivo, restituisci un punteggio standard (1x).
    return 1


async def calcola_punteggio_tempo_risposta(update: Update, context: ContextTypes.DEFAULT_TYPE, tempo_inizio,
                                           durata_risposta) -> None:
    """
    Calcola la differenza tra il tempo corrente e il tempo_inizio,
    che rappresenta il momento in cui è stata inviata la domanda.

    Sottrae il tempo di risposta calcolato dal tempo massimo consentito per rispondere alla domanda (durata_risposta).

    Moltiplica il tempo di risposta rimanente per 10 per ottenere il punteggio bonus.
    Questo è basato sul principio che più il giocatore risponde rapidamente, maggiore sarà il punteggio bonus.

    """
    return round(
        float(timedelta(seconds=durata_risposta).total_seconds() - (datetime.now() - tempo_inizio).total_seconds()),
        2) * 10


async def mostra_classifica(update: Update, context: ContextTypes.DEFAULT_TYPE, job_name) -> None:
    # Ottieni l'elenco dei giocatori che hanno partecipato al quiz.
    player_ids = players_in_quiz[update.effective_chat.title]
    classifica = []

    # Ottieni i dettagli del giocatore e aggiungili alla classifica.
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


def main():
    app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()

    # Handler comandi
    app.add_handler(CommandHandler("start", comando_start))
    app.add_handler(CommandHandler("nickname", comando_nickname))
    app.add_handler(CommandHandler("quiz", comando_quiz))
    app.add_handler(CommandHandler("profilo", comando_profilo))
    app.add_handler(CommandHandler("info", comando_info))
    app.add_handler(CommandHandler("avvia_quiz", comando_start_quiz))

    # Handler callback pulsanti
    app.add_handler(CallbackQueryHandler(bottone_avvia_quiz_jobs, pattern="avvia_quiz"))
    app.add_handler(CallbackQueryHandler(bottone_aggiungi_partecipante, pattern="aggiungi_partecipante"))
    app.add_handler(CallbackQueryHandler(bottone_rimuovi_partecipante, pattern="rimuovi_partecipante"))
    app.add_handler(CallbackQueryHandler(bottone_mostra_riferimenti, pattern="mostra_riferimenti"))

    # Handler callback pulsanti powerup
    app.add_handler(CallbackQueryHandler(handle_powerup_streak, pattern=Powerups.STREAK.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_regalo, pattern=Powerups.REGALO.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_doppio_rischio, pattern=Powerups.DOPPIO_RISCHIO.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_doppio, pattern=Powerups.DOPPIO.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_50_e_50, pattern=Powerups.CINQUANTA_CINQUANTA.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_gomma, pattern=Powerups.GOMMA.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_immunita, pattern=Powerups.IMMUNITA.nome()))
    app.add_handler(CallbackQueryHandler(handle_powerup_gioco_di_potere, pattern=Powerups.GIOCO_DI_POTERE.nome()))

    app.add_handler(PollAnswerHandler(processa_risposta))

    app.run_polling()


if __name__ == '__main__':
    main()
