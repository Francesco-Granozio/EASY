import sqlite3

from Settings import Settings


class SettingsDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def do_retrieve(self):
        try:
            async with self.db_manager as conn:
                cursor = await conn.execute("SELECT * FROM Settings")
                row = await cursor.fetchone()
                if row:
                    return Settings(row[0])
                return None  # Restituisci None se non ci sono impostazioni
        except sqlite3.Error as e:
            print(f"Errore durante la ricerca delle impostazioni: {e}")

    async def do_save(self, settings):
        try:
            async with self.db_manager as conn:
                await conn.execute(
                    "INSERT INTO settings (messaggio_opzioni) VALUES (?)",
                    (settings.messaggio_opzioni,))
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'inserimento delle impostazioni: {e}")

    async def do_delete(self):
        try:
            async with self.db_manager as conn:
                await conn.execute("DELETE FROM Settings WHERE TRUE")
                await conn.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'eliminazione delle impostazioni: {e}")
