namespace EasyInterfacciaDomande
{
    partial class FormInserimento
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.richTextBox_testo = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.richTextBox_rispostaA = new System.Windows.Forms.RichTextBox();
            this.richTextBox_rispostaB = new System.Windows.Forms.RichTextBox();
            this.richTextBox_rispostaC = new System.Windows.Forms.RichTextBox();
            this.richTextBox_rispostaD = new System.Windows.Forms.RichTextBox();
            this.comboBox_risposta_corretta = new System.Windows.Forms.ComboBox();
            this.panel2 = new System.Windows.Forms.Panel();
            this.comboBox_argomento = new System.Windows.Forms.ComboBox();
            this.domainUpDown_difficolta = new System.Windows.Forms.DomainUpDown();
            this.trackBar_tempo_risposta = new System.Windows.Forms.TrackBar();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.label17 = new System.Windows.Forms.Label();
            this.label18 = new System.Windows.Forms.Label();
            this.label19 = new System.Windows.Forms.Label();
            this.label20 = new System.Windows.Forms.Label();
            this.label21 = new System.Windows.Forms.Label();
            this.button_meme = new System.Windows.Forms.Button();
            this.button_conferma = new System.Windows.Forms.Button();
            this.button_annulla = new System.Windows.Forms.Button();
            this.label_meme_path = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_tempo_risposta)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(7, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(146, 41);
            this.label1.TabIndex = 0;
            this.label1.Text = "Testo domanda:";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.LightSkyBlue;
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel1.Controls.Add(this.label10);
            this.panel1.Controls.Add(this.label9);
            this.panel1.Controls.Add(this.label8);
            this.panel1.Controls.Add(this.label7);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.label6);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Location = new System.Drawing.Point(12, 21);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(161, 528);
            this.panel1.TabIndex = 1;
            // 
            // richTextBox_testo
            // 
            this.richTextBox_testo.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox_testo.Location = new System.Drawing.Point(3, 15);
            this.richTextBox_testo.Name = "richTextBox_testo";
            this.richTextBox_testo.Size = new System.Drawing.Size(593, 38);
            this.richTextBox_testo.TabIndex = 2;
            this.richTextBox_testo.Text = "";
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label2.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(7, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(146, 41);
            this.label2.TabIndex = 1;
            this.label2.Text = "Argomento:";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // label3
            // 
            this.label3.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label3.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(7, 115);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(146, 41);
            this.label3.TabIndex = 2;
            this.label3.Text = "Risposta A:";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label4
            // 
            this.label4.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label4.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(7, 165);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(146, 41);
            this.label4.TabIndex = 3;
            this.label4.Text = "Risposta B:";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label5
            // 
            this.label5.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label5.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.Location = new System.Drawing.Point(7, 265);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(146, 41);
            this.label5.TabIndex = 5;
            this.label5.Text = "Risposta D:";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label6
            // 
            this.label6.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label6.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.Location = new System.Drawing.Point(7, 215);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(146, 41);
            this.label6.TabIndex = 4;
            this.label6.Text = "Risposta C:";
            this.label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label7
            // 
            this.label7.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label7.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label7.Location = new System.Drawing.Point(7, 314);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(146, 41);
            this.label7.TabIndex = 6;
            this.label7.Text = "Risposta corretta:";
            this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label8
            // 
            this.label8.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label8.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label8.Location = new System.Drawing.Point(7, 366);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(146, 41);
            this.label8.TabIndex = 7;
            this.label8.Text = "Difficoltà:";
            this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.label8.Click += new System.EventHandler(this.label8_Click);
            // 
            // label9
            // 
            this.label9.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label9.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label9.Location = new System.Drawing.Point(7, 417);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(146, 41);
            this.label9.TabIndex = 8;
            this.label9.Text = "Tempo risposta:";
            this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label10
            // 
            this.label10.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label10.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label10.Location = new System.Drawing.Point(7, 469);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(146, 41);
            this.label10.TabIndex = 9;
            this.label10.Text = "Meme:";
            this.label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // richTextBox_rispostaA
            // 
            this.richTextBox_rispostaA.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox_rispostaA.Location = new System.Drawing.Point(3, 115);
            this.richTextBox_rispostaA.Name = "richTextBox_rispostaA";
            this.richTextBox_rispostaA.Size = new System.Drawing.Size(593, 38);
            this.richTextBox_rispostaA.TabIndex = 4;
            this.richTextBox_rispostaA.Text = "";
            this.richTextBox_rispostaA.TextChanged += new System.EventHandler(this.richTextBox_rispostaA_TextChanged);
            // 
            // richTextBox_rispostaB
            // 
            this.richTextBox_rispostaB.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox_rispostaB.Location = new System.Drawing.Point(3, 164);
            this.richTextBox_rispostaB.Name = "richTextBox_rispostaB";
            this.richTextBox_rispostaB.Size = new System.Drawing.Size(593, 38);
            this.richTextBox_rispostaB.TabIndex = 5;
            this.richTextBox_rispostaB.Text = "";
            this.richTextBox_rispostaB.TextChanged += new System.EventHandler(this.richTextBox_rispostaB_TextChanged);
            // 
            // richTextBox_rispostaC
            // 
            this.richTextBox_rispostaC.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox_rispostaC.Location = new System.Drawing.Point(3, 215);
            this.richTextBox_rispostaC.Name = "richTextBox_rispostaC";
            this.richTextBox_rispostaC.Size = new System.Drawing.Size(593, 38);
            this.richTextBox_rispostaC.TabIndex = 6;
            this.richTextBox_rispostaC.Text = "";
            this.richTextBox_rispostaC.TextChanged += new System.EventHandler(this.richTextBox_rispostaC_TextChanged);
            // 
            // richTextBox_rispostaD
            // 
            this.richTextBox_rispostaD.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox_rispostaD.Location = new System.Drawing.Point(3, 267);
            this.richTextBox_rispostaD.Name = "richTextBox_rispostaD";
            this.richTextBox_rispostaD.Size = new System.Drawing.Size(593, 38);
            this.richTextBox_rispostaD.TabIndex = 7;
            this.richTextBox_rispostaD.Text = "";
            this.richTextBox_rispostaD.TextChanged += new System.EventHandler(this.richTextBox_rispostaD_TextChanged);
            // 
            // comboBox_risposta_corretta
            // 
            this.comboBox_risposta_corretta.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBox_risposta_corretta.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBox_risposta_corretta.FormattingEnabled = true;
            this.comboBox_risposta_corretta.Items.AddRange(new object[] {
            "A",
            "B",
            "C",
            "D"});
            this.comboBox_risposta_corretta.Location = new System.Drawing.Point(3, 322);
            this.comboBox_risposta_corretta.Name = "comboBox_risposta_corretta";
            this.comboBox_risposta_corretta.Size = new System.Drawing.Size(593, 29);
            this.comboBox_risposta_corretta.TabIndex = 8;
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.panel2.Controls.Add(this.label_meme_path);
            this.panel2.Controls.Add(this.button_meme);
            this.panel2.Controls.Add(this.label19);
            this.panel2.Controls.Add(this.label20);
            this.panel2.Controls.Add(this.label21);
            this.panel2.Controls.Add(this.label15);
            this.panel2.Controls.Add(this.label16);
            this.panel2.Controls.Add(this.label17);
            this.panel2.Controls.Add(this.label18);
            this.panel2.Controls.Add(this.label13);
            this.panel2.Controls.Add(this.label14);
            this.panel2.Controls.Add(this.label12);
            this.panel2.Controls.Add(this.label11);
            this.panel2.Controls.Add(this.trackBar_tempo_risposta);
            this.panel2.Controls.Add(this.domainUpDown_difficolta);
            this.panel2.Controls.Add(this.comboBox_argomento);
            this.panel2.Controls.Add(this.richTextBox_testo);
            this.panel2.Controls.Add(this.richTextBox_rispostaA);
            this.panel2.Controls.Add(this.richTextBox_rispostaB);
            this.panel2.Controls.Add(this.comboBox_risposta_corretta);
            this.panel2.Controls.Add(this.richTextBox_rispostaC);
            this.panel2.Controls.Add(this.richTextBox_rispostaD);
            this.panel2.Location = new System.Drawing.Point(179, 23);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(611, 526);
            this.panel2.TabIndex = 3;
            this.panel2.Paint += new System.Windows.Forms.PaintEventHandler(this.panel2_Paint);
            // 
            // comboBox_argomento
            // 
            this.comboBox_argomento.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBox_argomento.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBox_argomento.FormattingEnabled = true;
            this.comboBox_argomento.Location = new System.Drawing.Point(3, 73);
            this.comboBox_argomento.Name = "comboBox_argomento";
            this.comboBox_argomento.Size = new System.Drawing.Size(593, 29);
            this.comboBox_argomento.TabIndex = 9;
            // 
            // domainUpDown_difficolta
            // 
            this.domainUpDown_difficolta.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.domainUpDown_difficolta.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.domainUpDown_difficolta.Items.Add("1");
            this.domainUpDown_difficolta.Items.Add("2");
            this.domainUpDown_difficolta.Items.Add("3");
            this.domainUpDown_difficolta.Location = new System.Drawing.Point(5, 375);
            this.domainUpDown_difficolta.Name = "domainUpDown_difficolta";
            this.domainUpDown_difficolta.Size = new System.Drawing.Size(120, 29);
            this.domainUpDown_difficolta.TabIndex = 10;
            // 
            // trackBar_tempo_risposta
            // 
            this.trackBar_tempo_risposta.AutoSize = false;
            this.trackBar_tempo_risposta.LargeChange = 1;
            this.trackBar_tempo_risposta.Location = new System.Drawing.Point(5, 413);
            this.trackBar_tempo_risposta.Name = "trackBar_tempo_risposta";
            this.trackBar_tempo_risposta.Size = new System.Drawing.Size(591, 33);
            this.trackBar_tempo_risposta.TabIndex = 11;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(8, 446);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(19, 13);
            this.label11.TabIndex = 12;
            this.label11.Text = "10";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(66, 446);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(19, 13);
            this.label12.TabIndex = 13;
            this.label12.Text = "15";
            this.label12.Click += new System.EventHandler(this.label12_Click);
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(181, 446);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(19, 13);
            this.label13.TabIndex = 15;
            this.label13.Text = "25";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(123, 446);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(19, 13);
            this.label14.TabIndex = 14;
            this.label14.Text = "20";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(406, 446);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(19, 13);
            this.label15.TabIndex = 19;
            this.label15.Text = "45";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(348, 446);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(19, 13);
            this.label16.TabIndex = 18;
            this.label16.Text = "40";
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(291, 446);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(19, 13);
            this.label17.TabIndex = 17;
            this.label17.Text = "35";
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(233, 446);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(19, 13);
            this.label18.TabIndex = 16;
            this.label18.Text = "30";
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(573, 446);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(19, 13);
            this.label19.TabIndex = 22;
            this.label19.Text = "60";
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Location = new System.Drawing.Point(515, 446);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(19, 13);
            this.label20.TabIndex = 21;
            this.label20.Text = "55";
            // 
            // label21
            // 
            this.label21.AutoSize = true;
            this.label21.Location = new System.Drawing.Point(458, 446);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(19, 13);
            this.label21.TabIndex = 20;
            this.label21.Text = "50";
            // 
            // button_meme
            // 
            this.button_meme.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button_meme.Location = new System.Drawing.Point(11, 477);
            this.button_meme.Name = "button_meme";
            this.button_meme.Size = new System.Drawing.Size(94, 30);
            this.button_meme.TabIndex = 23;
            this.button_meme.Text = "Seleziona";
            this.button_meme.UseVisualStyleBackColor = true;
            this.button_meme.Click += new System.EventHandler(this.button1_Click);
            // 
            // button_conferma
            // 
            this.button_conferma.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button_conferma.Location = new System.Drawing.Point(20, 568);
            this.button_conferma.Name = "button_conferma";
            this.button_conferma.Size = new System.Drawing.Size(94, 30);
            this.button_conferma.TabIndex = 24;
            this.button_conferma.Text = "Conferma";
            this.button_conferma.UseVisualStyleBackColor = true;
            this.button_conferma.Click += new System.EventHandler(this.button_conferma_Click);
            // 
            // button_annulla
            // 
            this.button_annulla.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button_annulla.Location = new System.Drawing.Point(138, 568);
            this.button_annulla.Name = "button_annulla";
            this.button_annulla.Size = new System.Drawing.Size(94, 30);
            this.button_annulla.TabIndex = 25;
            this.button_annulla.Text = "Annulla";
            this.button_annulla.UseVisualStyleBackColor = true;
            this.button_annulla.Click += new System.EventHandler(this.button3_Click);
            // 
            // label_meme_path
            // 
            this.label_meme_path.BackColor = System.Drawing.Color.White;
            this.label_meme_path.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label_meme_path.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label_meme_path.Location = new System.Drawing.Point(111, 477);
            this.label_meme_path.Name = "label_meme_path";
            this.label_meme_path.Size = new System.Drawing.Size(485, 32);
            this.label_meme_path.TabIndex = 24;
            // 
            // FormInserimento
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.DarkSeaGreen;
            this.ClientSize = new System.Drawing.Size(807, 610);
            this.Controls.Add(this.button_annulla);
            this.Controls.Add(this.button_conferma);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormInserimento";
            this.Text = "Nuova Domanda";
            this.Load += new System.EventHandler(this.FormInserimento_Load);
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_tempo_risposta)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.RichTextBox richTextBox_testo;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.RichTextBox richTextBox_rispostaA;
        private System.Windows.Forms.RichTextBox richTextBox_rispostaB;
        private System.Windows.Forms.RichTextBox richTextBox_rispostaC;
        private System.Windows.Forms.RichTextBox richTextBox_rispostaD;
        private System.Windows.Forms.ComboBox comboBox_risposta_corretta;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.TrackBar trackBar_tempo_risposta;
        private System.Windows.Forms.DomainUpDown domainUpDown_difficolta;
        private System.Windows.Forms.ComboBox comboBox_argomento;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Button button_meme;
        private System.Windows.Forms.Button button_conferma;
        private System.Windows.Forms.Button button_annulla;
        private System.Windows.Forms.Label label_meme_path;
    }
}