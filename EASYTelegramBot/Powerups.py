from enum import Enum


class Powerups(Enum):

    # Streak
    STREAK = (
        "Streak 🔥",
        "Il giocatore aumenta la sua streak di 3 punti"
    )

    # Regalo
    REGALO = (
        "Regalo 🎁",
        "Il giocatore riceve un numero di punti casuale tra 10 e 30 moltiplicati per la difficoltà della domanda"
    )

    # Doppio Rischio
    DOPPIO_RISCHIO = (
        "Doppio Rischio 🎲",
        "Il giocatore guadagna 2x punti se la risposta è corretta, altrimenti perde 2x punti"
    )

    # 2x
    DOPPIO = (
        "2x 💰",
        "Il giocatore guadagna 2x punti"
    )

    # 50/50
    CINQUANTA_CINQUANTA = (
        "50/50 🔘",
        "Vengono eliminate 2 risposte sbagliate"
    )

    # Gomma
    GOMMA = (
        "Gomma 🧼",
        "Viene eliminata 1 risposta sbagliata"
    )

    # Immunità
    IMMUNITA = (
        "Immunità 🛡️",
        "Il giocatore non perde punti se la risposta è sbagliata"
    )

    # Gioco di Potere
    GIOCO_DI_POTERE = (
        "Gioco di Potere 💥",
        "Il giocatore guadagna 2x punti se la risposta è corretta, mentre gli altri giocatori perdono 2x punti in caso di risposta sbagliata"
    )

    def nome(self):
        return self.value[0]

    def descrizione(self):
        return self.value[1]
