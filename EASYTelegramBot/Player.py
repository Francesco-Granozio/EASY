class Player:
    def __init__(self, player_id, nickname, punteggio_totale, domande_risposte=0, risposte_corrette=0,
                 risposte_errate=0, quiz_completati=0, powerup_utilizzati=0, numero_podi=0):
        self.player_id = player_id
        self.nickname = nickname
        self.punteggio_totale = punteggio_totale
        self.domande_risposte = domande_risposte
        self.risposte_corrette = risposte_corrette
        self.risposte_errate = risposte_errate
        self.quiz_completati = quiz_completati
        self.powerup_utilizzati = powerup_utilizzati
        self.numero_podi = numero_podi

    # Getter per l'ID
    def get_id(self):
        return self.player_id

    # Setter per l'ID
    def set_id(self, player_id):
        self.player_id = player_id

    # Getter per il nickname
    def get_nickname(self):
        return self.nickname

    def get_unique_nickname(self):
        return self.nickname + str(self.player_id)

    # Setter per il nickname
    def set_nickname(self, nickname):
        self.nickname = nickname

    # Getter per il punteggio_totale
    def get_punteggio_totale(self):
        return self.punteggio_totale

    # Setter per il punteggio_totale
    def set_punteggio_totale(self, punteggio_totale):
        self.punteggio_totale = punteggio_totale

        # Getter per le domande_risposte

    def get_domande_risposte(self):
        return self.domande_risposte

    # Setter per le domande_risposte
    def set_domande_risposte(self, domande_risposte):
        self.domande_risposte = domande_risposte

    # Getter per le risposte_corrette
    def get_risposte_corrette(self):
        return self.risposte_corrette

    # Setter per le risposte_corrette
    def set_risposte_corrette(self, risposte_corrette):
        self.risposte_corrette = risposte_corrette

    # Getter per le risposte_errate
    def get_risposte_errate(self):
        return self.risposte_errate

    # Setter per le risposte_errate
    def set_risposte_errate(self, risposte_errate):
        self.risposte_errate = risposte_errate

    # Getter per i quiz_completati
    def get_quiz_completati(self):
        return self.quiz_completati

    # Setter per i quiz_completati
    def set_quiz_completati(self, quiz_completati):
        self.quiz_completati = quiz_completati

    # Getter per i powerup_utilizzati
    def get_powerup_utilizzati(self):
        return self.powerup_utilizzati

    # Setter per i powerup_utilizzati
    def set_powerup_utilizzati(self, powerup_utilizzati):
        self.powerup_utilizzati = powerup_utilizzati

    # Getter per il numero_podi
    def get_numero_podi(self):
        return self.numero_podi

    # Setter per il numero_podi
    def set_numero_podi(self, numero_podi):
        self.numero_podi = numero_podi

    # Metodo per rappresentare l'oggetto come stringa
    def __str__(self):
        return (f"Player [ID: {self.player_id}, "
                f"Nickname: {self.nickname}, "
                f"punteggio_totale: {self.punteggio_totale}, "
                f"domande_risposte: {self.domande_risposte}, "
                f"risposte_corrette: {self.risposte_corrette}, "
                f"risposte_errate: {self.risposte_errate}, "
                f"quiz_completati: {self.quiz_completati}, "
                f"powerup_utilizzati: {self.powerup_utilizzati}, "
                f"numero_podi: {self.numero_podi}]")
