using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EasyProfessorInterface
{
    internal class Domanda
    {
        private int numeroDomanda = 0;
        private string testo;
        private string argomento;
        private string rispostaA;
        private string rispostaB;
        private string rispostaC;
        private string rispostaD;
        private int rispostaCorretta;
        private int difficolta;
        private int tempoRisposta;
        private string meme;

        public Domanda(int numeroDomanda, string testo, string argomento, string rispostaA, string rispostaB, string rispostaC, string rispostaD, int rispostaCorretta, int difficolta, int tempoRisposta, string meme)
        {
            this.numeroDomanda = numeroDomanda;
            this.testo = testo;
            this.argomento = argomento;
            this.rispostaA = rispostaA;
            this.rispostaB = rispostaB;
            this.rispostaC = rispostaC;
            this.rispostaD = rispostaD;
            this.rispostaCorretta = rispostaCorretta;
            this.difficolta = difficolta;
            this.tempoRisposta = tempoRisposta;
            this.meme = meme;
        }

        public Domanda(string testo, string argomento, string rispostaA, string rispostaB, string rispostaC, string rispostaD, int rispostaCorretta, int difficolta, int tempoRisposta, string meme)
        {
            this.testo = testo;
            this.argomento = argomento;
            this.rispostaA = rispostaA;
            this.rispostaB = rispostaB;
            this.rispostaC = rispostaC;
            this.rispostaD = rispostaD;
            this.rispostaCorretta = rispostaCorretta;
            this.difficolta = difficolta;
            this.tempoRisposta = tempoRisposta;
            this.meme = meme;
        }

        public override string ToString()
        {
            return $"Numero Domanda: {numeroDomanda}\n" +
                   $"Testo: {testo}\n" +
                   $"Argomento: {argomento}\n" +
                   $"Risposta A: {rispostaA}\n" +
                   $"Risposta B: {rispostaB}\n" +
                   $"Risposta C: {rispostaC}\n" +
                   $"Risposta D: {rispostaD}\n" +
                   $"Risposta Corretta: {rispostaCorretta}\n" +
                   $"Difficoltà: {difficolta}\n" +
                   $"Tempo Risposta: {tempoRisposta}\n" +
                   $"Meme: {meme}\n";
        }

        public int NumeroDomanda { get => numeroDomanda; set => numeroDomanda = value; }
        public string Testo { get => testo; set => testo = value; }
        public string Argomento { get => argomento; set => argomento = value; }
        public string RispostaA { get => rispostaA; set => rispostaA = value; }
        public string RispostaB { get => rispostaB; set => rispostaB = value; }
        public string RispostaC { get => rispostaC; set => rispostaC = value; }
        public string RispostaD { get => rispostaD; set => rispostaD = value; }
        public int RispostaCorretta { get => rispostaCorretta; set => rispostaCorretta = value; }
        public int Difficolta { get => difficolta; set => difficolta = value; }
        public int TempoRisposta { get => tempoRisposta; set => tempoRisposta = value; }
        public String Meme { get => meme; set => meme = value; }
    }
}
