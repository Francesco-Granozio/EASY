using EasyInterfacciaDomande;
using EasyInterfacciaDomande.Domande;
using EasyInterfacciaDomande;
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

namespace EasyInterfacciaDomande
{
    public partial class FormVisualizzazione : Form
    {
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
                AddRow(domanda, dataGridView1);
                
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Carica_Database();
        }

        public DataGridView GetDataGridView()
        {
            return dataGridView1;
        }

        public void AddRow(Domanda domanda, DataGridView dataGridView)
        {
            DataGridViewRow newRow = new DataGridViewRow();
            newRow.CreateCells(dataGridView1);
            newRow.Cells[0].Value = domanda.NumeroDomanda;
            newRow.Cells[1].Value = domanda.Testo;
            newRow.Cells[2].Value = domanda.Argomento;
            newRow.Cells[3].Value = domanda.RispostaA;
            newRow.Cells[4].Value = domanda.RispostaB;
            newRow.Cells[5].Value = domanda.RispostaC;
            newRow.Cells[6].Value = domanda.RispostaD;
            newRow.Cells[7].Value = domanda.RispostaCorretta;
            newRow.Cells[8].Value = domanda.Difficolta;
            newRow.Cells[9].Value = domanda.TempoRisposta;
            newRow.Cells[10].Value = domanda.Meme;

            byte[] memeBytes = null;

            if (!string.IsNullOrEmpty(domanda.Meme))
            {
                memeBytes = File.ReadAllBytes(domanda.Meme);
            }

            newRow.Cells[11].Value = memeBytes;
            dataGridView.Rows.Add(newRow);
        }

        private void dataGridView1_CellFormatting(object sender, DataGridViewCellFormattingEventArgs e)
        {
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
            if (e.RowIndex >= 0 && e.ColumnIndex == dataGridView1.Columns["immagineMeme"].Index)
            {
                DataGridViewRow row = dataGridView1.Rows[e.RowIndex];
                byte[] imageData = (byte[])row.Cells["immagineMeme"].Value;

                if (imageData != null && imageData.Length > 0)
                {
                    pictureBox1.Image = Image.FromStream(new MemoryStream(imageData));
                    pictureBox1.Visible = true;
                }
            }
        }


        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {

        }

        private void dataGridView1_MouseLeave(object sender, EventArgs e)
        {
        }

        private void dataGridView1_CellMouseLeave_1(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0 && e.ColumnIndex == dataGridView1.Columns["immagineMeme"].Index)
            {
                pictureBox1.Visible = false;
            }
        }

        private void dataGridView1_CellMouseDoubleClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = dataGridView1.Rows[e.RowIndex];


                FormInserimento form = new FormInserimento(this, new Domanda(
                        Convert.ToInt32(row.Cells["numeroDomanda"].Value),
                        row.Cells["testo"].Value.ToString(),
                        row.Cells["argomento"].Value.ToString(),
                        row.Cells["rispostaA"].Value.ToString(),
                        row.Cells["rispostaB"].Value.ToString(),
                        row.Cells["rispostaC"].Value.ToString(),
                        row.Cells["rispostaD"].Value.ToString(),
                        Convert.ToInt32(row.Cells["rispostaCorretta"].Value),
                        Convert.ToInt32(row.Cells["difficolta"].Value),
                        Convert.ToInt32(row.Cells["tempoRisposta"].Value),
                        row.Cells["meme"].Value.ToString()));

                form.Show();
            }
            /*if (e.RowIndex >= 0)
            {
                DataGridViewRow row = dataGridView1.Rows[e.RowIndex];

                // Chiedi all'utente se vuole eliminare o modificare
                DialogResult result = MessageBox.Show("Vuoi eliminare la domanda?", "Azione", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

                if (result == DialogResult.Yes)
                {
                    Domanda domanda = new Domanda(
                        Convert.ToInt32(row.Cells["numeroDomanda"].Value),
                        row.Cells["testo"].Value.ToString(),
                        row.Cells["argomento"].Value.ToString(),
                        row.Cells["rispostaA"].Value.ToString(),
                        row.Cells["rispostaB"].Value.ToString(),
                        row.Cells["rispostaC"].Value.ToString(),
                        row.Cells["rispostaD"].Value.ToString(),
                        Convert.ToInt32(row.Cells["rispostaCorretta"].Value),
                        Convert.ToInt32(row.Cells["difficolta"].Value),
                        Convert.ToInt32(row.Cells["tempoRisposta"].Value),
                        row.Cells["meme"].Value.ToString());

                    dataGridView1.Rows.Remove(row);

                    using (SqliteConnection connection = new SqliteConnection(@"Data Source=C:\Shared\Unisa\Tesi\EASY\database.db"))
                    {
                        connection.Open();

                        DomandaDAO dao = new DomandaDAO(connection);
                        dao.DoDelete(domanda);
                        connection.Close();
                    }
                }
            }*/
        }

        private void dataGridView1_CellMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bool success = true;

            for (int i = dataGridView1.Rows.Count - 1; i >= 0; i--)
            {
                DataGridViewRow row = dataGridView1.Rows[i];
                DataGridViewCheckBoxCell checkBoxCell = row.Cells["elimina"] as DataGridViewCheckBoxCell;

                if (checkBoxCell != null && Convert.ToBoolean(checkBoxCell.Value))
                {
                    int numeroDomanda = Convert.ToInt32(row.Cells["numeroDomanda"].Value);

                    // Rimuovi la riga dalla DataGridView
                    dataGridView1.Rows.Remove(row);

                    using (SqliteConnection connection = new SqliteConnection(@"Data Source=C:\Shared\Unisa\Tesi\EASY\database.db"))
                    {
                        connection.Open();

                        DomandaDAO dao = new DomandaDAO(connection);
                        if (dao.DoDelete(new Domanda(numeroDomanda, null, null, null,
                            null, null, null, 0, 0, 0, null)))
                        {
                            success = true;
                        }
                        else
                        {
                            success = false;
                            break;
                        }
                        connection.Close();
                    }
                }
            }

            if (success)
            {
                MessageBox.Show("Domande eliminate con successo", "Successo", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Errore durante l'eliminazione delle domande", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }     
}
