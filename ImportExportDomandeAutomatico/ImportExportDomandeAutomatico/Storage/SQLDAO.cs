using Microsoft.Data.Sqlite;

namespace Storage
{
    public abstract class SQLDAO
    {
        protected readonly SqliteConnection connection;

        public SQLDAO(SqliteConnection connection)
        {
            this.connection = connection;
        }
    }
}
