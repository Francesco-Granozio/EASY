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
                    players.append(Player(row[0], row[1], row[2]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca di tutti i giocatori: {e}")

    async def do_retrieve_by_id(self, player_id):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players WHERE id = ?", (player_id,))
                row = await cursor.fetchone()
                if row:
                    return Player(row[0], row[1], row[2])
                return None
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del giocatore per ID: {e}")

    async def do_retrieve_by_nickname(self, nickname):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players WHERE nickname = ?", (nickname,))
                rows = await cursor.fetchall()
                players = []
                for row in rows:
                    players.append(Player(row[0], row[1], row[2]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del giocatore per nickname: {e}")

    async def do_retrieve_by_punteggio(self, punteggio):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Players WHERE punteggio = ?", (punteggio,))
                rows = await cursor.fetchall()
                players = []
                for row in rows:
                    players.append(Player(row[0], row[1], row[2]))
                return players
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del giocatore per punteggio: {e}")

    async def do_save(self, player):
        try:
            async with self.db_manager as conn:
                await conn.execute("INSERT INTO Players (id, nickname, punteggio) VALUES (?, ?, ?)",
                                   (str(player.get_id()), player.get_nickname(), player.get_punteggio()))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'inserimento del giocatore: {e}")

    async def do_update(self, player):
        try:
            async with self.db_manager as conn:
                await conn.execute("UPDATE Players SET nickname = ?, punteggio = ? WHERE id = ?",
                                   (player.get_nickname(), player.get_punteggio(), player.get_id()))
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
