class Powerup:
    def __init__(self, id_powerup, nome, descrizione):
        self.id_powerup = id_powerup
        self.nome = nome
        self.descrizione = descrizione

    # Getter per l'ID del powerup
    def get_id(self):
        return self.id_powerup

    # Setter per l'ID del powerup
    def set_id_powerup(self, id_powerup):
        self.id_powerup = id_powerup

    # Getter per il nome del powerup
    def get_nome(self):
        return self.nome

    # Setter per il nome del powerup
    def set_nome(self, nome):
        self.nome = nome

    # Getter per la descrizione del powerup
    def get_descrizione(self):
        return self.descrizione

    # Setter per la descrizione del powerup
    def set_descrizione(self, descrizione):
        self.descrizione = descrizione

    # Metodo per rappresentare l'oggetto come stringa
    def __str__(self):
        return f"Powerup [ID: {self.id_powerup}, Nome: {self.nome}, Descrizione: {self.descrizione}]"
