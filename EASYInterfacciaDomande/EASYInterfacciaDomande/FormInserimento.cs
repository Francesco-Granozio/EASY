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
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EasyInterfacciaDomande
{
    public partial class FormInserimento : Form
    {
        private Domanda domanda;
        private FormVisualizzazione formVisualizzazione;
        private bool mode = true; //false aggiornamento, true inserimento
        private int id;

        public FormInserimento()
        {
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            InitializeComponent();
        }

        public FormInserimento(FormVisualizzazione formVisualizzazione, bool mode)
        {
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.formVisualizzazione = formVisualizzazione;
            this.mode = mode;

            InitializeComponent();

            domainUpDown_difficolta.SelectedItem = "1";
            comboBox_argomento.Items.AddRange(Argomenti.argomenti);
            comboBox_argomento.SelectedItem = Argomenti.CONCETTI_BASE;
        }

        public FormInserimento(FormVisualizzazione formVisualizzazione, Domanda domanda, bool mode)
        {
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.formVisualizzazione = formVisualizzazione;
            this.mode = mode;

            InitializeComponent();

            comboBox_argomento.Items.AddRange(Argomenti.argomenti);
            domainUpDown_difficolta.SelectedItem = domanda.Difficolta.ToString();

            Debug.WriteLine(domanda.Argomento);
            this.id = domanda.NumeroDomanda;
            richTextBox_testo.Text = domanda.Testo;
            comboBox_argomento.Text = domanda.Argomento;
            comboBox_argomento.SelectedItem = domanda.Argomento;
            Debug.WriteLine(comboBox_argomento.SelectedItem.ToString());
            richTextBox_rispostaA.Text = domanda.RispostaA;
            richTextBox_rispostaB.Text = domanda.RispostaB;
            richTextBox_rispostaC.Text = domanda.RispostaC;
            richTextBox_rispostaD.Text = domanda.RispostaD;
            comboBox_risposta_corretta.Text = domanda.RispostaCorrettaToSting();
            domainUpDown_difficolta.Text = domanda.Difficolta.ToString();
            trackBar_tempo_risposta.Value = domanda.TempoRisposta;
            label_meme_path.Text = domanda.Meme;
            richTextBox_fonte.Text = domanda.Fonte;
        }



        private void FormInserimento_Load(object sender, EventArgs e)
        {
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

                domanda = new Domanda(id, richTextBox_testo.Text, comboBox_argomento.SelectedItem.ToString(),
                richTextBox_rispostaA.Text, richTextBox_rispostaB.Text, richTextBox_rispostaC.Text,
                richTextBox_rispostaD.Text,
                comboBox_risposta_corretta.SelectedIndex + 1, domainUpDown_difficolta.SelectedIndex + 1,
                Convert.ToInt32(trackBar_tempo_risposta.Value), label_meme_path.Text == "" ? null : label_meme_path.Text,
                richTextBox_fonte.Text == "" ? null : richTextBox_fonte.Text);


            }
            catch
            {
                MessageBox.Show("Inserire tutti i campi", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            DatabaseManager.Instance.Execute(connection =>
            {
                DomandaDAO dao = new DomandaDAO(connection);

                if (dao.DoSaveOrUpdate(domanda))
                {
                    this.Close();
                }
                else
                {
                    MessageBox.Show("Errore durante l'inserimento della domanda", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }

                if (mode)
                {
                    MessageBox.Show("Domanda inserita con successo", "Successo", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    //formVisualizzazione.AddRow(domanda, formVisualizzazione.GetDataGridView());
                    formVisualizzazione.Refresh_Database();
                }
                else
                {
                    MessageBox.Show("Domanda aggiornata con successo", "Successo", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    //formVisualizzazione.UpdateRow(domanda, formVisualizzazione.GetDataGridView());
                    formVisualizzazione.Refresh_Database();

                }
            });
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

        private void button1_Click_1(object sender, EventArgs e)
        {
            label_meme_path.Text = "";
        }
    }
}
