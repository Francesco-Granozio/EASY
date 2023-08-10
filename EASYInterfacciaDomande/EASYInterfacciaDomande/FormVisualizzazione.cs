using EasyInterfacciaDomande;
using EasyInterfacciaDomande.Domande;
using EasyInterfacciaDomande.Utils;
using EASYInterfacciaDomande.Utils;
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

        public void Refresh_Database()
        {
            dataGridView1.Rows.Clear();
            List<Domanda> domande = null;

            DatabaseManager.Instance.Execute(connection =>
            {
                DomandaDAO dao = new DomandaDAO(connection);
                domande = dao.DoRetrieveAll();
            });


            if (domande != null)
            {
                foreach (Domanda domanda in domande)
                {
                    AddRow(domanda, dataGridView1);

                }
            }
        }

        public void Refresh_Database(Func<DomandaDAO, List<Domanda>> retrieveMethod)
        {
            dataGridView1.Rows.Clear();
            List<Domanda> domande = null;

            DatabaseManager.Instance.Execute(connection =>
            {
                DomandaDAO dao = new DomandaDAO(connection);
                domande = retrieveMethod(dao);
            });

            if (domande != null)
            {
                foreach (Domanda domanda in domande)
                {
                    if (domanda != null)
                    {
                        AddRow(domanda, dataGridView1);
                    }
                }
            }
        }

        public void Carica_Database()
        {
            List<Domanda> domande = null;

            DatabaseManager.Instance.Execute(connection =>
            {
                DomandaDAO dao = new DomandaDAO(connection);
                domande = dao.DoRetrieveAll();
            });

            if (domande != null)
            {
                foreach (Domanda domanda in domande)
                {
                    if (domanda != null)
                    {
                        AddRow(domanda, dataGridView1);
                    }
                }
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Carica_Database();
            comboBox_ricerca.SelectedItem = "Numero domanda";
        }

        public DataGridView GetDataGridView()
        {
            return dataGridView1;
        }

        public void UpdateRow(Domanda domanda, DataGridView dataGridView)
        {
            foreach (DataGridViewRow row in dataGridView.Rows)
            {
                if (Convert.ToInt32(row.Cells[0].Value) == domanda.NumeroDomanda)
                {
                    row.Cells[1].Value = domanda.Testo;
                    row.Cells[2].Value = domanda.Argomento;
                    row.Cells[3].Value = domanda.RispostaA;
                    row.Cells[4].Value = domanda.RispostaB;
                    row.Cells[5].Value = domanda.RispostaC;
                    row.Cells[6].Value = domanda.RispostaD;
                    row.Cells[7].Value = domanda.RispostaCorretta;
                    row.Cells[8].Value = domanda.Difficolta;
                    row.Cells[9].Value = domanda.TempoRisposta;
                    row.Cells[10].Value = domanda.Meme;

                    byte[] memeBytes = null;

                    if (!string.IsNullOrEmpty(domanda.Meme))
                    {
                        memeBytes = File.ReadAllBytes(domanda.Meme);
                    }

                    row.Cells[11].Value = memeBytes;

                    break; // Esci dal ciclo dopo aver trovato e aggiornato la riga
                }
            }
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form f = new FormInserimento(this, true);
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
                        row.Cells["meme"].Value.ToString()),
                        false);

                form.Show();
            }
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


                    DatabaseManager.Instance.Execute(connection =>
                    {
                        DomandaDAO dao = new DomandaDAO(connection);
                        if (dao.DoDelete(new Domanda(numeroDomanda)))
                        {
                            success = true;
                        }
                        else
                        {
                            success = false;
                        }
                    });
                    if (!success)
                    {
                        break;
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

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            if (comboBox_ricerca.SelectedItem.Equals("Numero domanda"))
            {
                if (int.TryParse(comboBox_input.Text, out int numeroDomanda))
                {
                    
                    //Refresh_Database(dao => dao.DoRetrieveAll());
                    Refresh_Database(dao =>
                    {
                        Domanda domanda = dao.DoRetrieveById(numeroDomanda);
                        return new List<Domanda> { domanda };
                    });
                }
                else
                {
                    MessageBox.Show("Inserisci un numero valido.", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }

            if (comboBox_ricerca.SelectedItem.Equals("Testo"))
            {
                Refresh_Database(dao =>
                {
                    return dao.DoRetrieveByTesto(comboBox_input.Text);
                });
            }

            if (comboBox_ricerca.SelectedItem.Equals("Argomento"))
            {
                Refresh_Database(dao =>
                {
                    return dao.DoRetrieveByArgomento(comboBox_input.Text);
                });
            }

            if (comboBox_ricerca.SelectedItem.Equals("Difficoltà"))
            {
                Refresh_Database(dao =>
                {
                    return dao.DoRetrieveByDifficolta(Convert.ToInt32(comboBox_input.Text));
                });
            }
        }

        private void comboBox_ricerca_SelectedIndexChanged(object sender, EventArgs e)
        {
            comboBox_input.Items.Clear();
            comboBox_input.SelectedItem = "";
            comboBox_input.Text = "";
            if (comboBox_ricerca.SelectedItem.Equals("Argomento"))
            {

                comboBox_input.Items.AddRange(Argomenti.argomenti);
                comboBox_input.SelectedItem = Argomenti.CONCETTI_BASE;
                comboBox_input.DropDownStyle = ComboBoxStyle.DropDownList;
            }

            if (comboBox_ricerca.SelectedItem.Equals("Difficoltà"))
            {

                comboBox_input.Items.AddRange(new object[] { 1, 2, 3 });
                comboBox_input.SelectedItem = 1;
                comboBox_input.DropDownStyle = ComboBoxStyle.DropDownList;
            }
            if (comboBox_ricerca.SelectedItem.Equals("Testo") || comboBox_ricerca.SelectedItem.Equals("Numero domanda"))
            {
                comboBox_input.DropDownStyle = ComboBoxStyle.DropDown;
            }
        }
    }     
}
