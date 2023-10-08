CREATE TABLE "Domande" (
	"numeroDomanda"	INTEGER NOT NULL,
	"testo"	TEXT NOT NULL,
	"argomento"	TEXT NOT NULL,
	"rispostaA"	TEXT NOT NULL,
	"rispostaB"	TEXT NOT NULL,
	"rispostaC"	TEXT NOT NULL,
	"rispostaD"	TEXT NOT NULL,
	"rispostaCorretta"	TEXT NOT NULL,
	"difficolta"	TEXT NOT NULL,
	"tempoRisposta"	INTEGER NOT NULL,
	"meme"	TEXT,
	"fonte"	TEXT,
	PRIMARY KEY("numeroDomanda" AUTOINCREMENT)
);


CREATE TABLE "Players" (
	"id"	TEXT NOT NULL,
	"nickname"	TEXT NOT NULL UNIQUE,
	"punteggio_totale"	REAL NOT NULL DEFAULT 0,
	"domande_risposte"	INTEGER DEFAULT 0,
	"risposte_corrette"	INTEGER DEFAULT 0,
	"risposte_errate"	INTEGER DEFAULT 0,
	"quiz_completati"	INTEGER DEFAULT 0,
	"powerup_utilizzati"	INTEGER DEFAULT 0,
	"numero_podi"	INTEGER DEFAULT 0,
	PRIMARY KEY("id")
);


CREATE TABLE "Settings" (
	"messaggio_opzioni"	INTEGER
);
