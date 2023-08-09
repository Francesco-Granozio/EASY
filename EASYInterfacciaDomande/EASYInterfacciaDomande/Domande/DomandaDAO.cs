using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using EasyInterfacciaDomande;
using EasyInterfacciaDomande.Storage;
using Microsoft.Data.Sqlite;

namespace EasyInterfacciaDomande.Domande
{
    internal class DomandaDAO : SQLDAO
    {
        public DomandaDAO(SqliteConnection connection) : base(connection)
        {
        }

        public List<Domanda> DoRetrieveAll()
        {
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande", connection);
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10)));
            }
            return domande;
        }

        public Domanda DoRetrieveById(int id)
        {
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE NumeroDomanda = @id", connection);
            command.Parameters.AddWithValue("@id", id);
            SqliteDataReader reader = command.ExecuteReader();
            if (reader.Read())
            {
                return new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10));
            }
            return null;
        }

        public List<Domanda> DoRetrieveByArgomento(string argomento)
        {
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE Argomento = @argomento", connection);
            command.Parameters.AddWithValue("@argomento", argomento);
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10)));
            }
            return domande;
        }

        public List<Domanda> DoRetrieveByDifficolta(int difficolta)
        {
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE Difficolta = @difficolta", connection);
            command.Parameters.AddWithValue("@difficolta", difficolta);
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10)));
            }
            return domande;
        }

        public bool DoSave(Domanda domanda)
        {
            SqliteCommand command = new SqliteCommand(
                @"INSERT INTO Domande (testo, argomento, RispostaA, RispostaB, RispostaC, RispostaD, 
                RispostaCorretta, difficolta, tempoRisposta, meme) 
                VALUES (@testo, @argomento, @RispostaA, @RispostaB, @RispostaC, @RispostaD, 
                @RispostaCorretta, @difficolta, @tempoRisposta, @meme)", connection);

            command.Parameters.AddWithValue("@testo", domanda.Testo);
            command.Parameters.AddWithValue("@argomento", domanda.Argomento);
            command.Parameters.AddWithValue("@RispostaA", domanda.RispostaA);
            command.Parameters.AddWithValue("@RispostaB", domanda.RispostaB);
            command.Parameters.AddWithValue("@RispostaC", domanda.RispostaC);
            command.Parameters.AddWithValue("@RispostaD", domanda.RispostaD);
            command.Parameters.AddWithValue("@RispostaCorretta", domanda.RispostaCorretta);
            command.Parameters.AddWithValue("@difficolta", domanda.Difficolta);
            command.Parameters.AddWithValue("@tempoRisposta", domanda.TempoRisposta);
            command.Parameters.AddWithValue("@meme", domanda.Meme);

            return command.ExecuteNonQuery() == 1;
        }

        public bool DoUpdate(Domanda domanda)
        {
            SqliteCommand command = new SqliteCommand(
                @"UPDATE Domande SET testo = @testo, argomento = @argomento, RispostaA = @RispostaA, 
                RispostaB = @RispostaB, RispostaC = @RispostaC, RispostaD = @RispostaD, 
                RispostaCorretta = @RispostaCorretta, difficolta = @difficolta, 
                tempoRisposta = @tempoRisposta, meme = @meme WHERE NumeroDomanda = @id", connection);

            command.Parameters.AddWithValue("@testo", domanda.Testo);
            command.Parameters.AddWithValue("@argomento", domanda.Argomento);
            command.Parameters.AddWithValue("@RispostaA", domanda.RispostaA);
            command.Parameters.AddWithValue("@RispostaB", domanda.RispostaB);
            command.Parameters.AddWithValue("@RispostaC", domanda.RispostaC);
            command.Parameters.AddWithValue("@RispostaD", domanda.RispostaD);
            command.Parameters.AddWithValue("@RispostaCorretta", domanda.RispostaCorretta);
            command.Parameters.AddWithValue("@difficolta", domanda.Difficolta);
            command.Parameters.AddWithValue("@tempoRisposta", domanda.TempoRisposta);
            command.Parameters.AddWithValue("@meme", domanda.Meme);
            command.Parameters.AddWithValue("@id", domanda.NumeroDomanda);

            return command.ExecuteNonQuery() == 1;
        }

        public bool DoSaveOrUpdate(Domanda domanda)
        {
            if (DoRetrieveById(domanda.NumeroDomanda) == null)
            {
                return DoSave(domanda);
            }
            else
            {
                return DoUpdate(domanda);
            }
        }

        public bool DoDelete(Domanda domanda)
        {
            SqliteCommand command = new SqliteCommand("DELETE FROM Domande WHERE NumeroDomanda = @id", connection);
            command.Parameters.AddWithValue("@id", domanda.NumeroDomanda);
            return command.ExecuteNonQuery() == 1;
        }
    }
}
