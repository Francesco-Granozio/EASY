using Microsoft.Data.Sqlite;
using System;

namespace Utils
{
    public class DatabaseManager
    {
        private static DatabaseManager instance;
        private string connectionString;

        private DatabaseManager(string connectionString)
        {
            this.connectionString = connectionString;
        }

        public static DatabaseManager Instance
        {
            get
            {
                if (instance == null)
                {
                    // Imposta la stringa di connessione qui
                    string connectionString = @"Data Source=C:\Shared\Unisa\Tesi\EASY\database.db";
                    instance = new DatabaseManager(connectionString);
                }
                return instance;
            }
        }

        public void Execute(Action<SqliteConnection> action)
        {
            using (SqliteConnection connection = new SqliteConnection(connectionString))
            {
                try
                {
                    connection.Open();
                    action.Invoke(connection);
                }
                catch (Exception ex)
                {
                    // Gestione delle eccezioni
                    Console.WriteLine(ex.Message);
                }
            }
        }
    }

}
