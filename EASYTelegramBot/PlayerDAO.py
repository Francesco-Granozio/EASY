import sqlite3

from Player import Player


class PlayerDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def do_retrieve_all(self):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players")
                rows = await cursor.fetchall()
                players = []
                for row in rows:
                    players.append(Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca di tutti i giocatori: {e}")

    async def do_retrieve_by_id(self, player_id):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players WHERE id = ?", (player_id,))
                row = await cursor.fetchone()
                if row:
                    return Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                return None
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del giocatore per ID: {e}")

    async def do_retrieve_by_id_list(self, id_list):
        try:
            async with self.db_manager as conn:
                # Utilizza una stringa di interrogazione con il segnaposto IN per passare la lista di ID
                query = "SELECT * FROM Players WHERE id IN ({seq})".format(seq=','.join(['?'] * len(id_list)))
                cursor = await conn.execute(query, id_list)
                rows = await cursor.fetchall()
                players = []
                for row in rows:
                    players.append(Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca dei giocatori per ID: {e}")

    async def do_retrieve_by_nickname(self, nickname):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players WHERE nickname = ?", (nickname,))
                rows = await cursor.fetchall()
                players = []
                for row in rows:
                    players.append(Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del giocatore per nickname: {e}")

    async def do_retrieve_by_punteggio_totale(self, punteggio_totale):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players WHERE punteggio_totale = ?", (punteggio_totale,))
                rows = await cursor.fetchall()
                players = []
                for row in rows:
                    players.append(Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del giocatore per punteggio_totale: {e}")

    async def do_save(self, player):
        try:
            async with self.db_manager as conn:
                await conn.execute("INSERT INTO Players (id, nickname, punteggio_totale, domande_risposte, "
                                   "risposte_corrette, risposte_errate, quiz_completati, powerup_utilizzati, "
                                   "numero_podi) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                   (str(player.get_id()), player.get_nickname(), player.get_punteggio_totale(),
                                    player.get_domande_risposte(), player.get_risposte_corrette(),
                                    player.get_risposte_errate(), player.get_quiz_completati(),
                                    player.get_powerup_utilizzati(), player.get_numero_podi()))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'inserimento del giocatore: {e}")

    async def do_update(self, player):
        try:
            async with self.db_manager as conn:
                await conn.execute("UPDATE Players SET nickname = ?, punteggio_totale = ?, domande_risposte = ?, "
                                   "risposte_corrette = ?, risposte_errate = ?, quiz_completati = ?, "
                                   "powerup_utilizzati = ?, numero_podi = ? WHERE id = ?",
                                   (player.get_nickname(), player.get_punteggio_totale(), player.get_domande_risposte(),
                                    player.get_risposte_corrette(), player.get_risposte_errate(),
                                    player.get_quiz_completati(), player.get_powerup_utilizzati(),
                                    player.get_numero_podi(), player.get_id()))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'aggiornamento del giocatore: {e}")

    async def do_save_or_update(self, player):
        if await self.do_retrieve_by_id(player.get_id()):
            await self.do_update(player)
        else:
            await self.do_save(player)

    async def do_delete(self, player_id):
        try:
            async with self.db_manager as conn:
                await conn.execute("DELETE FROM Players WHERE id = ?", (player_id,))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'eliminazione del giocatore: {e}")
