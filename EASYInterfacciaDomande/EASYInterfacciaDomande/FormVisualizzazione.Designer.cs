namespace EasyInterfacciaDomande
{
    partial class FormVisualizzazione
    {
        /// <summary>
        /// Variabile di progettazione necessaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Pulire le risorse in uso.
        /// </summary>
        /// <param name="disposing">ha valore true se le risorse gestite devono essere eliminate, false in caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Codice generato da Progettazione Windows Form

        /// <summary>
        /// Metodo necessario per il supporto della finestra di progettazione. Non modificare
        /// il contenuto del metodo con l'editor di codice.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle6 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle7 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle8 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle9 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle10 = new System.Windows.Forms.DataGridViewCellStyle();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormVisualizzazione));
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.comboBox_ricerca = new System.Windows.Forms.ComboBox();
            this.comboBox_input = new System.Windows.Forms.ComboBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.numeroDomanda = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.testo = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.argomento = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.rispostaA = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.rispostaB = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.rispostaC = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.rispostaD = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.rispostaCorretta = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.difficolta = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.tempoRisposta = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.meme = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.immagineMeme = new System.Windows.Forms.DataGridViewImageColumn();
            this.fonte = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.elimina = new System.Windows.Forms.DataGridViewCheckBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            dataGridViewCellStyle6.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            dataGridViewCellStyle6.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dataGridView1.AlternatingRowsDefaultCellStyle = dataGridViewCellStyle6;
            this.dataGridView1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dataGridView1.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.dataGridView1.BackgroundColor = System.Drawing.SystemColors.ControlLight;
            this.dataGridView1.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.dataGridView1.CellBorderStyle = System.Windows.Forms.DataGridViewCellBorderStyle.SingleHorizontal;
            dataGridViewCellStyle7.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle7.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle7.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle7.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle7.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle7.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle7.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.dataGridView1.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle7;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.numeroDomanda,
            this.testo,
            this.argomento,
            this.rispostaA,
            this.rispostaB,
            this.rispostaC,
            this.rispostaD,
            this.rispostaCorretta,
            this.difficolta,
            this.tempoRisposta,
            this.meme,
            this.immagineMeme,
            this.fonte,
            this.elimina});
            dataGridViewCellStyle8.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle8.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle8.Font = new System.Drawing.Font("Segoe UI Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle8.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle8.SelectionBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            dataGridViewCellStyle8.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle8.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.dataGridView1.DefaultCellStyle = dataGridViewCellStyle8;
            this.dataGridView1.GridColor = System.Drawing.Color.FromArgb(((int)(((byte)(144)))), ((int)(((byte)(155)))), ((int)(((byte)(183)))));
            this.dataGridView1.Location = new System.Drawing.Point(5, 67);
            this.dataGridView1.Name = "dataGridView1";
            dataGridViewCellStyle9.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle9.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle9.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle9.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle9.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle9.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle9.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.dataGridView1.RowHeadersDefaultCellStyle = dataGridViewCellStyle9;
            dataGridViewCellStyle10.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dataGridView1.RowsDefaultCellStyle = dataGridViewCellStyle10;
            this.dataGridView1.Size = new System.Drawing.Size(1219, 496);
            this.dataGridView1.TabIndex = 0;
            this.dataGridView1.AllowUserToAddRowsChanged += new System.EventHandler(this.dataGridView1_AllowUserToAddRowsChanged);
            this.dataGridView1.CellFormatting += new System.Windows.Forms.DataGridViewCellFormattingEventHandler(this.dataGridView1_CellFormatting);
            this.dataGridView1.CellMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.dataGridView1_CellMouseClick);
            this.dataGridView1.CellMouseDoubleClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.dataGridView1_CellMouseDoubleClick);
            this.dataGridView1.CellMouseEnter += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellMouseEnter);
            this.dataGridView1.CellMouseLeave += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellMouseLeave_1);
            this.dataGridView1.MouseLeave += new System.EventHandler(this.dataGridView1_MouseLeave);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(81, 47);
            this.button1.TabIndex = 1;
            this.button1.Text = "Inserisci";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(108, 12);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(154, 47);
            this.button2.TabIndex = 3;
            this.button2.Text = "Elimina Selezionate";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // comboBox_ricerca
            // 
            this.comboBox_ricerca.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBox_ricerca.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBox_ricerca.FormattingEnabled = true;
            this.comboBox_ricerca.Items.AddRange(new object[] {
            "*",
            "Numero domanda",
            "Testo",
            "Argomento",
            "Difficoltà"});
            this.comboBox_ricerca.Location = new System.Drawing.Point(428, 22);
            this.comboBox_ricerca.Name = "comboBox_ricerca";
            this.comboBox_ricerca.Size = new System.Drawing.Size(144, 29);
            this.comboBox_ricerca.TabIndex = 10;
            this.comboBox_ricerca.SelectedIndexChanged += new System.EventHandler(this.comboBox_ricerca_SelectedIndexChanged);
            // 
            // comboBox_input
            // 
            this.comboBox_input.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBox_input.FormattingEnabled = true;
            this.comboBox_input.Location = new System.Drawing.Point(578, 22);
            this.comboBox_input.Name = "comboBox_input";
            this.comboBox_input.Size = new System.Drawing.Size(586, 29);
            this.comboBox_input.TabIndex = 13;
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox2.Image = global::EASYInterfacciaDomande.Properties.Resources._211818_search_icon32;
            this.pictureBox2.InitialImage = ((System.Drawing.Image)(resources.GetObject("pictureBox2.InitialImage")));
            this.pictureBox2.Location = new System.Drawing.Point(1170, 20);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(34, 34);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 12;
            this.pictureBox2.TabStop = false;
            this.pictureBox2.Click += new System.EventHandler(this.pictureBox2_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox1.Location = new System.Drawing.Point(406, 158);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(400, 300);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Visible = false;
            this.pictureBox1.MouseLeave += new System.EventHandler(this.pictureBox1_MouseLeave);
            // 
            // numeroDomanda
            // 
            this.numeroDomanda.FillWeight = 111.6751F;
            this.numeroDomanda.HeaderText = "#";
            this.numeroDomanda.Name = "numeroDomanda";
            this.numeroDomanda.ReadOnly = true;
            // 
            // testo
            // 
            this.testo.FillWeight = 98.83249F;
            this.testo.HeaderText = "Testo";
            this.testo.Name = "testo";
            this.testo.ReadOnly = true;
            // 
            // argomento
            // 
            this.argomento.FillWeight = 98.83249F;
            this.argomento.HeaderText = "Argomento";
            this.argomento.Name = "argomento";
            this.argomento.ReadOnly = true;
            // 
            // rispostaA
            // 
            this.rispostaA.FillWeight = 98.83249F;
            this.rispostaA.HeaderText = "Risposta A";
            this.rispostaA.Name = "rispostaA";
            this.rispostaA.ReadOnly = true;
            // 
            // rispostaB
            // 
            this.rispostaB.FillWeight = 98.83249F;
            this.rispostaB.HeaderText = "Risposta B";
            this.rispostaB.Name = "rispostaB";
            this.rispostaB.ReadOnly = true;
            // 
            // rispostaC
            // 
            this.rispostaC.FillWeight = 98.83249F;
            this.rispostaC.HeaderText = "Risposta C";
            this.rispostaC.Name = "rispostaC";
            this.rispostaC.ReadOnly = true;
            // 
            // rispostaD
            // 
            this.rispostaD.FillWeight = 98.83249F;
            this.rispostaD.HeaderText = "Risposta D";
            this.rispostaD.Name = "rispostaD";
            this.rispostaD.ReadOnly = true;
            // 
            // rispostaCorretta
            // 
            this.rispostaCorretta.FillWeight = 98.83249F;
            this.rispostaCorretta.HeaderText = "Risposta Corretta";
            this.rispostaCorretta.Name = "rispostaCorretta";
            this.rispostaCorretta.ReadOnly = true;
            // 
            // difficolta
            // 
            this.difficolta.FillWeight = 98.83249F;
            this.difficolta.HeaderText = "Difficoltà";
            this.difficolta.Name = "difficolta";
            this.difficolta.ReadOnly = true;
            // 
            // tempoRisposta
            // 
            this.tempoRisposta.FillWeight = 98.83249F;
            this.tempoRisposta.HeaderText = "Tempo Risposta";
            this.tempoRisposta.Name = "tempoRisposta";
            this.tempoRisposta.ReadOnly = true;
            // 
            // meme
            // 
            this.meme.FillWeight = 98.83249F;
            this.meme.HeaderText = "Meme";
            this.meme.Name = "meme";
            this.meme.ReadOnly = true;
            // 
            // immagineMeme
            // 
            this.immagineMeme.HeaderText = "Immagine Meme";
            this.immagineMeme.Name = "immagineMeme";
            this.immagineMeme.ReadOnly = true;
            this.immagineMeme.Resizable = System.Windows.Forms.DataGridViewTriState.True;
            this.immagineMeme.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.Automatic;
            // 
            // fonte
            // 
            this.fonte.HeaderText = "Fonte";
            this.fonte.Name = "fonte";
            this.fonte.ReadOnly = true;
            // 
            // elimina
            // 
            this.elimina.HeaderText = "Elimina";
            this.elimina.Name = "elimina";
            // 
            // FormVisualizzazione
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.DarkSeaGreen;
            this.ClientSize = new System.Drawing.Size(1232, 575);
            this.Controls.Add(this.comboBox_input);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.comboBox_ricerca);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.dataGridView1);
            this.Name = "FormVisualizzazione";
            this.Text = "EASY Interfaccia Domande";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.ComboBox comboBox_ricerca;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.ComboBox comboBox_input;
        private System.Windows.Forms.DataGridViewTextBoxColumn numeroDomanda;
        private System.Windows.Forms.DataGridViewTextBoxColumn testo;
        private System.Windows.Forms.DataGridViewTextBoxColumn argomento;
        private System.Windows.Forms.DataGridViewTextBoxColumn rispostaA;
        private System.Windows.Forms.DataGridViewTextBoxColumn rispostaB;
        private System.Windows.Forms.DataGridViewTextBoxColumn rispostaC;
        private System.Windows.Forms.DataGridViewTextBoxColumn rispostaD;
        private System.Windows.Forms.DataGridViewTextBoxColumn rispostaCorretta;
        private System.Windows.Forms.DataGridViewTextBoxColumn difficolta;
        private System.Windows.Forms.DataGridViewTextBoxColumn tempoRisposta;
        private System.Windows.Forms.DataGridViewTextBoxColumn meme;
        private System.Windows.Forms.DataGridViewImageColumn immagineMeme;
        private System.Windows.Forms.DataGridViewTextBoxColumn fonte;
        private System.Windows.Forms.DataGridViewCheckBoxColumn elimina;
    }
}

