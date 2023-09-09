class Player:
    def __init__(self, player_id, nickname, punteggio):
        self.player_id = player_id
        self.nickname = nickname
        self.punteggio = punteggio

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

    # Getter per il punteggio
    def get_punteggio(self):
        return self.punteggio

    # Setter per il punteggio
    def set_punteggio(self, punteggio):
        self.punteggio = punteggio

    # Metodo per rappresentare l'oggetto come stringa
    def __str__(self):
        return f"Player [ID: {self.player_id}, Nickname: {self.nickname}, Punteggio: {self.punteggio}]"
