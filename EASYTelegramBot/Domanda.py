class Domanda:
    def __init__(self, numeroDomanda, testo, argomento, rispostaA, rispostaB, rispostaC, rispostaD, rispostaCorretta,
                 difficolta, tempoRisposta, meme):
        self.numeroDomanda = numeroDomanda
        self.testo = testo
        self.argomento = argomento
        self.rispostaA = rispostaA
        self.rispostaB = rispostaB
        self.rispostaC = rispostaC
        self.rispostaD = rispostaD
        self.rispostaCorretta = rispostaCorretta
        self.difficolta = difficolta
        self.tempoRisposta = tempoRisposta
        self.meme = meme

    def __str__(self):
        return f"Domanda [Numero: {self.numeroDomanda}, Testo: {self.testo}, Argomento: {self.argomento}, Risposta A: {self.rispostaA}, Risposta B: {self.rispostaB}, Risposta C: {self.rispostaC}, Risposta D: {self.rispostaD}, Risposta Corretta: {self.rispostaCorretta}, Difficolta: {self.difficolta}, Tempo Risposta: {self.tempoRisposta}, Meme: {self.meme}]"

    def get_numeroDomanda(self):
        return self.numeroDomanda

    def get_testo(self):
        return self.testo

    def get_argomento(self):
        return self.argomento

    def get_rispostaA(self):
        return self.rispostaA

    def get_rispostaB(self):
        return self.rispostaB

    def get_rispostaC(self):
        return self.rispostaC

    def get_rispostaD(self):
        return self.rispostaD

    def get_rispostaCorretta(self):
        return self.rispostaCorretta

    def get_difficolta(self):
        return self.difficolta

    def get_tempoRisposta(self):
        return self.tempoRisposta

    def get_meme(self):
        return self.meme

    def set_numeroDomanda(self, numeroDomanda):
        self.numeroDomanda = numeroDomanda

    def set_testo(self, testo):
        self.testo = testo

    def set_argomento(self, argomento):
        self.argomento = argomento

    def set_rispostaA(self, rispostaA):
        self.rispostaA = rispostaA

    def set_rispostaB(self, rispostaB):
        self.rispostaB = rispostaB

    def set_rispostaC(self, rispostaC):
        self.rispostaC = rispostaC

    def set_rispostaD(self, rispostaD):
        self.rispostaD = rispostaD

    def set_rispostaCorretta(self, rispostaCorretta):
        self.rispostaCorretta = rispostaCorretta

    def set_difficolta(self, difficolta):
        self.difficolta = difficolta

    def set_tempoRisposta(self, tempoRisposta):
        self.tempoRisposta = tempoRisposta

    def set_meme(self, meme):
        self.meme = meme
