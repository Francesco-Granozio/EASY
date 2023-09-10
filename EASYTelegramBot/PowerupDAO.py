import sqlite3
from Powerup import Powerup


class PowerupDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def do_retrieve_all(self):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Powerups")
                rows = await cursor.fetchall()
                powerups = []
                for row in rows:
                    powerups.append(Powerup(row[0], row[1], row[2]))
                return powerups
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca di tutti i powerup: {e}")

    async def do_retrieve_by_id(self, id_powerup):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Powerups WHERE id = ?", (id_powerup,))
                row = await cursor.fetchone()
                if row:
                    return Powerup(row[0], row[1], row[2])
                return None
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del powerup per ID: {e}")

    async def do_retrieve_by_nome(self, nome):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Powerups WHERE nome = ?", (nome,))
                rows = await cursor.fetchall()
                powerups = []
                for row in rows:
                    powerups.append(Powerup(row[0], row[1], row[2]))
                return powerups
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del powerup per nome: {e}")

    async def do_retrieve_by_descrizione(self, descrizione):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Powerups WHERE descrizione = ?", (descrizione,))
                rows = await cursor.fetchall()
                powerups = []
                for row in rows:
                    powerups.append(Powerup(row[0], row[1], row[2]))
                return powerups
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca del powerup per descrizione: {e}")

    async def do_save(self, powerup):
        try:
            async with self.db_manager as conn:
                await conn.execute("INSERT INTO Powerups (id, nome, descrizione) VALUES (?, ?, ?)",
                                   (powerup.get_id(), powerup.get_nome(), powerup.get_descrizione()))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'inserimento del powerup: {e}")

    async def do_update(self, powerup):
        try:
            async with self.db_manager as conn:
                await conn.execute("UPDATE Powerups SET nome = ?, descrizione = ? WHERE id = ?",
                                   (powerup.get_nome(), powerup.get_descrizione(), powerup.get_id()))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'aggiornamento del powerup: {e}")

    async def do_save_or_update(self, powerup):
        if await self.do_retrieve_by_id(powerup.get_id()):
            await self.do_update(powerup)
        else:
            await self.do_save(powerup)

    async def do_delete(self, id_powerup):
        try:
            async with self.db_manager as conn:
                await conn.execute("DELETE FROM Powerups WHERE id = ?", (id_powerup,))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'eliminazione del powerup: {e}")
