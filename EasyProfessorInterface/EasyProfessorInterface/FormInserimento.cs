using EasyProfessorInterface;
using EasyProfessorInterface.Domande;
using EASYProfessorInterface.Utils;
using Microsoft.Data.Sqlite;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EASYProfessorInterface
{
    public partial class FormInserimento : Form
    {
        private Domanda domanda;
        private FormVisualizzazione formVisualizzazione;
        public FormInserimento()
        {
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            InitializeComponent();
        }

        public FormInserimento(FormVisualizzazione formVisualizzazione)
        {
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.formVisualizzazione = formVisualizzazione;
            
            InitializeComponent();
        }
        

        private void FormInserimento_Load(object sender, EventArgs e)
        {
            domainUpDown_difficolta.SelectedItem = "1";
            comboBox_argomento.Items.AddRange(Argomenti.argomenti);
            comboBox_argomento.SelectedItem = Argomenti.CONCETTI_BASE;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Filter = "Image Files(*.jpg; *.jpeg; *.png)|*.jpg; *.jpeg; *.png";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                label_meme_path.Text = dialog.FileName;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button_conferma_Click(object sender, EventArgs e)
        {
            
            if (string.IsNullOrEmpty(richTextBox_testo.Text) || comboBox_argomento.SelectedItem == null
                || string.IsNullOrEmpty(richTextBox_rispostaA.Text) || string.IsNullOrEmpty(richTextBox_rispostaB.Text)
                || string.IsNullOrEmpty(richTextBox_rispostaC.Text) || string.IsNullOrEmpty(richTextBox_rispostaD.Text)
                || comboBox_risposta_corretta.SelectedItem == null)
            {
                MessageBox.Show("Compilare tutti i campi", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            try
            {
                domanda = new Domanda(richTextBox_testo.Text, comboBox_argomento.SelectedItem.ToString(),
                richTextBox_rispostaA.Text, richTextBox_rispostaB.Text, richTextBox_rispostaC.Text,
                richTextBox_rispostaD.Text,
                comboBox_risposta_corretta.SelectedIndex + 1, domainUpDown_difficolta.SelectedIndex + 1,
                Convert.ToInt32(trackBar_tempo_risposta.Value * 5 + 10), label_meme_path.Text);
            }
            catch
            {
                MessageBox.Show("Inserire tutti i campi", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            
            using (SqliteConnection connection = new SqliteConnection(@"Data Source=C:\Shared\Unisa\Tesi\EASY\database.db"))
            {
                try
                {
                    connection.Open();

                    DomandaDAO dao = new DomandaDAO(connection);

                    if (dao.DoSave(domanda))
                    {
                        MessageBox.Show("Domanda inserita con successo", "Successo", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        formVisualizzazione.Carica_Database();
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show("Errore durante l'inserimento della domanda", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
                finally
                {
                    connection.Close();
                }

                
            }
            
        }

        private void richTextBox_rispostaA_TextChanged(object sender, EventArgs e)
        {
        }

        private void richTextBox_rispostaB_TextChanged(object sender, EventArgs e)
        {
        }

        private void richTextBox_rispostaC_TextChanged(object sender, EventArgs e)
        {
        }

        private void richTextBox_rispostaD_TextChanged(object sender, EventArgs e)
        {
           
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
