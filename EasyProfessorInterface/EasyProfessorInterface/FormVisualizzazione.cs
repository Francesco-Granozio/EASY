using EasyProfessorInterface;
using EasyProfessorInterface.Domande;
using EASYProfessorInterface;
using Microsoft.Data.Sqlite;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EasyProfessorInterface
{
    public partial class FormVisualizzazione : Form
    {
        private DataTable table = new DataTable("tabella");

        public FormVisualizzazione()
        {
            InitializeComponent();
        }

        public void Carica_Database()
        {
            List<Domanda> domande;

            using (SqliteConnection connection = new SqliteConnection(@"Data Source=C:\Shared\Unisa\Tesi\EASY\database.db"))
            {
                connection.Open();

                DomandaDAO dao = new DomandaDAO(connection);
                domande = dao.DoRetrieveAll();
                connection.Close();
            }

            foreach (Domanda domanda in domande)
            {
                byte[] memeBytes = null;

                if (!string.IsNullOrEmpty(domanda.Meme))
                {
                    memeBytes = File.ReadAllBytes(domanda.Meme);
                }

                table.Rows.Add(domanda.NumeroDomanda, domanda.Testo, domanda.Argomento, domanda.RispostaA,
                               domanda.RispostaB, domanda.RispostaC, domanda.RispostaD, domanda.RispostaCorretta,
                               domanda.Difficolta, domanda.TempoRisposta, memeBytes);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            table.Columns.Add("Numero Domanda", typeof(int));
            table.Columns.Add("Testo", typeof(string));
            table.Columns.Add("Argomento", typeof(string));
            table.Columns.Add("Risposta A", typeof(string));
            table.Columns.Add("Risposta B", typeof(string));
            table.Columns.Add("Risposta C", typeof(string));
            table.Columns.Add("Risposta D", typeof(string));
            table.Columns.Add("Risposta Corretta", typeof(int));
            table.Columns.Add("Difficoltà", typeof(int));
            table.Columns.Add("Tempo risposta", typeof(int));
            table.Columns.Add("Meme", typeof(Byte[]));

            dataGridView1.DataSource = table;

            Carica_Database();

        }

        private void dataGridView1_CellFormatting(object sender, DataGridViewCellFormattingEventArgs e)
        {
            if (dataGridView1.Columns[e.ColumnIndex].Name == "Meme")
            {
                if (e.Value != null)
                {
                    int desiredHeight = 100; // Altezza desiderata delle celle
                    dataGridView1.Rows[e.RowIndex].Height = desiredHeight;
                }
            }
        }

        private void dataGridView1_AllowUserToAddRowsChanged(object sender, EventArgs e)
        {
            Debug.WriteLine("Chiamato");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form f = new FormInserimento(this);
            f.Show();
        }


        private void dataGridView1_CellMouseEnter(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0 && e.ColumnIndex == 10) // Cambia 10 con l'indice della colonna del meme
            {
                DataGridViewCell cell = dataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex];
                if (cell.Value != null && cell.Value != DBNull.Value)
                {
                    string memePath = cell.Value.ToString(); // Supponendo che il valore sia il percorso dell'immagine
                    pictureBox_ingrandimento.ImageLocation = memePath; // pictureBoxIngrandimento è il nome del PictureBox in cui mostrerai l'immagine ingrandita
                    pictureBox_ingrandimento.Visible = true; // Mostra il PictureBox
                }
            }
        }

        private void dataGridView1_CellMouseLeave(object sender, DataGridViewCellEventArgs e)
        {
            pictureBox_ingrandimento.Visible = false; // Nascondi il PictureBox quando il mouse lascia la cella

        }


    }
}
