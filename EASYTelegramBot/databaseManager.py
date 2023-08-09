import sqlite3

from singleton import singleton


@singleton
class DatabaseManager:

    def __init__(self, name):
        self.connection = sqlite3.connect("database.db", isolation_level="DEFERRED", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def crea_tabella_utenti(self):
        with self.connection:
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS Utenti (
                                "id"	INTEGER NOT NULL,
                                "nome"	TEXT NOT NULL,
                                PRIMARY KEY("id")
                            );''')

    def cerca_utente(self, id_utente):
        with self.connection:
            self.cursor.execute(f"SELECT * FROM Utenti WHERE id = {id_utente}")
            return self.cursor.fetchone()

    def inserisci_utente(self, id_utente, nome_utente):
        with self.connection:
            self.cursor.execute(f"INSERT INTO Utenti VALUES ({id_utente}, '{nome_utente}')")

    def modifica_utente(self, id_utente, nome_utente):
        with self.connection:
            self.cursor.execute(f"UPDATE Utenti SET nome = '{nome_utente}' WHERE id = {id_utente}")

    def __del__(self):
        self.cursor.close()
        self.connection.close()