using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Domande;
using Microsoft.Data.Sqlite;

namespace Domande
{
    public class DomandaDAO : Storage.SQLDAO
    {
        public DomandaDAO(SqliteConnection connection) : base(connection)
        {
        }

        public List<Domanda> DoRetrieveAll()
        {
            Debug.WriteLine("DoRetrieveAll");
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande", connection);
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10), reader.IsDBNull(11) ? null : reader.GetString(11)));
            }
            return domande;
        }

        public Domanda DoRetrieveById(int id)
        {
            Debug.WriteLine("DoRetrieveById");
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE NumeroDomanda = @id", connection);
            command.Parameters.AddWithValue("@id", id);
            SqliteDataReader reader = command.ExecuteReader();
            if (reader.Read())
            {
                return new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10), reader.IsDBNull(11) ? null : reader.GetString(11));
            }
            return null;
        }

        public List<Domanda> DoRetrieveByArgomento(string argomento)
        {
            Debug.WriteLine("DoRetrieveByArgomento");
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE Argomento = @argomento", connection);
            command.Parameters.AddWithValue("@argomento", argomento);
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10), reader.IsDBNull(11) ? null : reader.GetString(11)));
            }
            return domande;
        }

        public List<Domanda> DoRetrieveByTesto(string testo)
        {
            Debug.WriteLine("DoRetrieveByTesto");
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE Testo LIKE @testo", connection);
            command.Parameters.AddWithValue("@testo", "%" + testo + "%"); // Aggiunge % al testo per cercare tutte le sottostringhe
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10), reader.IsDBNull(11) ? null : reader.GetString(11)));
            }
            // Restituisci l'elenco delle domande trovate
            return domande;
        }



        public List<Domanda> DoRetrieveByDifficolta(int difficolta)
        {
            Debug.WriteLine("DoRetrieveByDifficolta");
            List<Domanda> domande = new List<Domanda>();
            SqliteCommand command = new SqliteCommand("SELECT * FROM Domande WHERE Difficolta = @difficolta", connection);
            command.Parameters.AddWithValue("@difficolta", difficolta);
            SqliteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                domande.Add(new Domanda(reader.GetInt32(0), reader.GetString(1), reader.GetString(2), reader.GetString(3), reader.GetString(4), reader.GetString(5), reader.GetString(6), reader.GetInt32(7), reader.GetInt32(8), reader.GetInt32(9), reader.IsDBNull(10) ? null : reader.GetString(10), reader.IsDBNull(11) ? null : reader.GetString(11)));
            }
            return domande;
        }

        public bool DoSave(Domanda domanda)
        {
            Debug.WriteLine("DoSave");
            SqliteCommand command = new SqliteCommand(
                @"INSERT INTO Domande (testo, argomento, RispostaA, RispostaB, RispostaC, RispostaD, 
                RispostaCorretta, difficolta, tempoRisposta, meme, fonte) 
                VALUES (@testo, @argomento, @RispostaA, @RispostaB, @RispostaC, @RispostaD, 
                @RispostaCorretta, @difficolta, @tempoRisposta, @meme, @fonte)", connection);

            command.Parameters.AddWithValue("@testo", domanda.Testo);
            command.Parameters.AddWithValue("@argomento", domanda.Argomento);
            command.Parameters.AddWithValue("@RispostaA", domanda.RispostaA);
            command.Parameters.AddWithValue("@RispostaB", domanda.RispostaB);
            command.Parameters.AddWithValue("@RispostaC", domanda.RispostaC);
            command.Parameters.AddWithValue("@RispostaD", domanda.RispostaD);
            command.Parameters.AddWithValue("@RispostaCorretta", domanda.RispostaCorretta);
            command.Parameters.AddWithValue("@difficolta", domanda.Difficolta);
            command.Parameters.AddWithValue("@tempoRisposta", domanda.TempoRisposta);
            command.Parameters.AddWithValue("@meme", domanda.Meme is null ? DBNull.Value : (object)domanda.Meme);
            command.Parameters.AddWithValue("@fonte", domanda.Fonte is null ? DBNull.Value : (object)domanda.Fonte);

            return command.ExecuteNonQuery() == 1;
        }

        public bool DoUpdate(Domanda domanda)
        {
            Debug.WriteLine("DoUpdate");
            SqliteCommand command = new SqliteCommand(
                @"UPDATE Domande SET testo = @testo, argomento = @argomento, RispostaA = @RispostaA, 
                RispostaB = @RispostaB, RispostaC = @RispostaC, RispostaD = @RispostaD, 
                RispostaCorretta = @RispostaCorretta, difficolta = @difficolta, 
                tempoRisposta = @tempoRisposta, meme = @meme, fonte = @fonte WHERE NumeroDomanda = @id", connection);

            command.Parameters.AddWithValue("@testo", domanda.Testo);
            command.Parameters.AddWithValue("@argomento", domanda.Argomento);
            command.Parameters.AddWithValue("@RispostaA", domanda.RispostaA);
            command.Parameters.AddWithValue("@RispostaB", domanda.RispostaB);
            command.Parameters.AddWithValue("@RispostaC", domanda.RispostaC);
            command.Parameters.AddWithValue("@RispostaD", domanda.RispostaD);
            command.Parameters.AddWithValue("@RispostaCorretta", domanda.RispostaCorretta);
            command.Parameters.AddWithValue("@difficolta", domanda.Difficolta);
            command.Parameters.AddWithValue("@tempoRisposta", domanda.TempoRisposta);
            command.Parameters.AddWithValue("@meme", domanda.Meme is null ? DBNull.Value : (object)domanda.Meme);
            command.Parameters.AddWithValue("@id", domanda.NumeroDomanda);
            command.Parameters.AddWithValue("@fonte", domanda.Fonte is null ? DBNull.Value : (object)domanda.Fonte);
            
            return command.ExecuteNonQuery() == 1;
        }

        public bool DoSaveOrUpdate(Domanda domanda)
        {
            Debug.WriteLine("DoSaveOrUpdate");
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
            Debug.WriteLine("DoDelete");
            SqliteCommand command = new SqliteCommand("DELETE FROM Domande WHERE NumeroDomanda = @id", connection);
            command.Parameters.AddWithValue("@id", domanda.NumeroDomanda);
            return command.ExecuteNonQuery() == 1;
        }
    }
}
