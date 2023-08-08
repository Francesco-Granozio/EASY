using EasyProfessorInterface.DAO;
using EasyProfessorInterface.Domande;
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
    public partial class Form1 : Form
    {
        private DataTable table = new DataTable("tabella");
        
        public Form1()
        {
            InitializeComponent();
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

            
            using (SqliteConnection connection = new SqliteConnection(@"Data Source=C:\Shared\Unisa\Tesi\EASY\database.db"))
            {
                /*connection.Open();

                DomandaDAO dao = new DomandaDAO(connection);
                List<Domanda> domande = dao.DoRetrieveAll();

                connection.Close();*/
            }
            
       

            //table.Rows.Add(1, "Il Fra?", "IlFra", "il fra", "IL FRA", "il FRA", "ilFRAAAAA", 1, 1, 5, File.ReadAllBytes(@"C:\Shared\Unisa\Tesi\EASY\Risorse\ilFra.png"));

        }

        private void dataGridView1_CellFormatting(object sender, DataGridViewCellFormattingEventArgs e)
        {
            if (dataGridView1.Columns[e.ColumnIndex].Name == "Meme")
            {
                if (e.Value != null)
                {
                    int desiredHeight = 150; // Altezza desiderata delle celle
                    dataGridView1.Rows[e.RowIndex].Height = desiredHeight;
                }
            }
        }

        private void dataGridView1_AllowUserToAddRowsChanged(object sender, EventArgs e)
        {
            Debug.WriteLine("Chiamato");
        }
    }
}
