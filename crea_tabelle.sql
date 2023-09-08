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
	PRIMARY KEY("numeroDomanda" AUTOINCREMENT)
);


CREATE TABLE "Players" (
	"id"	INTEGER NOT NULL,
	"nickname"	TEXT NOT NULL UNIQUE,
	"punteggio"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE "Powerups" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL UNIQUE,
	"descrizione"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

/*CREATE TABLE "sqlite_sequence" (
	"name"	,
	"seq"	
);*/