class Settings:
    def __init__(self, messaggio_opzioni):
        self.messaggio_opzioni = messaggio_opzioni

    def get_messaggio_opzioni(self):
        return self.messaggio_opzioni

    def set_messaggio_opzioni(self, messaggio_opzioni):
        self.messaggio_opzioni = messaggio_opzioni

    def __str__(self):
        return f"Settings [Messaggio Opzioni: {self.messaggio_opzioni}]"
