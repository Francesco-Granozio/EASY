import sqlite3

from Domanda import Domanda


class DomandaDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def do_retrieve_all(self):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Domande")
                rows = await cursor.fetchall()
                domande = []
                for row in rows:
                    domande.append(
                        Domanda(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11]))
                return domande
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca di tutte le domande: {e}")

    async def do_retrieve_by_id(self, numeroDomanda):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Domande WHERE numeroDomanda = ?", (numeroDomanda,))
                row = await cursor.fetchone()
                if row:
                    return Domanda(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                   row[10], row[11])
                return None
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca della domanda per Numero: {e}")

    async def do_retrieve_by_argomento(self, argomento):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Domande WHERE argomento = ?", (argomento,))
                rows = await cursor.fetchall()
                domande = []
                for row in rows:
                    domande.append(
                        Domanda(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11]))
                return domande
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca delle domande per Argomento: {e}")

    async def do_retrieve_by_argomento_random_limit(self, argomento, limite):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Domande WHERE argomento = ? ORDER BY RANDOM() LIMIT ?", (argomento, limite))
                rows = await cursor.fetchall()
                domande = []
                for row in rows:
                    domande.append(
                        Domanda(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11]))
                return domande
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca delle domande per Argomento: {e}")

    async def do_save(self, domanda):
        try:
            async with self.db_manager as conn:
                await conn.execute(
                    "INSERT INTO Domande (testo, argomento, rispostaA, rispostaB, rispostaC, rispostaD, rispostaCorretta, difficolta, tempoRisposta, meme, fonte) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (domanda.testo, domanda.argomento, domanda.rispostaA, domanda.rispostaB, domanda.rispostaC,
                     domanda.rispostaD, domanda.rispostaCorretta, domanda.difficolta, domanda.tempoRisposta,
                     domanda.meme, domanda.fonte))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'inserimento della domanda: {e}")

    async def do_update(self, domanda):
        try:
            async with self.db_manager as conn:
                await conn.execute(
                    "UPDATE Domande SET testo = ?, argomento = ?, rispostaA = ?, rispostaB = ?, rispostaC = ?, rispostaD = ?, rispostaCorretta = ?, difficolta = ?, tempoRisposta = ?, meme = ?, fonte = ? WHERE numeroDomanda = ?",
                    (domanda.testo, domanda.argomento, domanda.rispostaA, domanda.rispostaB, domanda.rispostaC,
                     domanda.rispostaD, domanda.rispostaCorretta, domanda.difficolta, domanda.tempoRisposta,
                     domanda.meme, domanda.fonte, domanda.numeroDomanda))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'aggiornamento della domanda: {e}")

    async def do_save_or_update(self, domanda):
        if await self.do_retrieve_by_id(domanda.numeroDomanda):
            await self.do_update(domanda)
        else:
            await self.do_save(domanda)

    async def do_delete(self, numeroDomanda):
        try:
            async with self.db_manager as conn:
                await conn.execute("DELETE FROM Domande WHERE numeroDomanda = ?", (numeroDomanda,))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'eliminazione della domanda: {e}")
