using Microsoft.Data.Sqlite;

namespace EasyProfessorInterface.Storage
{
    internal abstract class SQLDAO
    {
        protected readonly SqliteConnection connection;

        public SQLDAO(SqliteConnection connection)
        {
            this.connection = connection;
        }
    }
}
