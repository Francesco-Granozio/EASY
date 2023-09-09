import sqlite3
from sqlite3 import Connection
from singleton import singleton
import aiosqlite


@singleton
class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    async def __aenter__(self):
        if self.connection is None:
            self.connection = await aiosqlite.connect(self.db_file)
        return self.connection

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.connection:
            await self.connection.close()
            self.connection = None

    async def __connect(self):
        if self.connection is None:
            self.connection = await aiosqlite.connect(self.db_file)
        return self.connection

    async def __close(self):
        if self.connection:
            await self.connection.close()
            self.connection = None
