using Domande;
using System.Text;
using Utils;

class Program
{
    static void Main()
    {
        /*string filePath = @"C:\Shared\Unisa\Tesi\EASY\ImportExportDomandeAutomatico\ImportExportDomandeAutomatico\ImportIstruzioniPreProcessore.txt";
        List<Domanda> domande = LeggiDomandeDaFile(filePath, Argomenti.ISTRUZIONI_PREPROCESSORE);

        if (domande is null)
            return;

        foreach (Domanda domanda in domande)
        {
            Console.WriteLine(domanda.ToString());

            DatabaseManager.Instance.Execute(connection =>
            {
                DomandaDAO dao = new DomandaDAO(connection);

                dao.DoSaveOrUpdate(domanda);
            });


        }
        */

        EsportaDomande();
    }

    static void EsportaDomande()
    {
        List<Domanda> domande = null;
        DatabaseManager.Instance.Execute(connection =>
        {
            DomandaDAO dao = new DomandaDAO(connection);

            domande = dao.DoRetrieveAll();
        });
        string path = @"C:\Shared\Unisa\Tesi\EASY\ImportExportDomandeAutomatico\ImportExportDomandeAutomatico\ExportDomande.txt";

        StringBuilder exportContent = new StringBuilder();

        // Itera attraverso ciascuna domanda e aggiungi le informazioni nel formato richiesto
        foreach (var domanda in domande)
        {
            exportContent.AppendLine("Domanda: " + domanda.Testo);
            exportContent.AppendLine("Risposta 1: " + domanda.RispostaA);
            exportContent.AppendLine("Risposta 2: " + domanda.RispostaB);
            exportContent.AppendLine("Risposta 3: " + domanda.RispostaC);
            exportContent.AppendLine("Risposta 4: " + domanda.RispostaD);
            exportContent.AppendLine("Indice risposta corretta: " + domanda.RispostaCorretta);
            exportContent.AppendLine("Difficoltà: " + domanda.Difficolta);
            exportContent.AppendLine("Fonte: " + domanda.Fonte);
            exportContent.AppendLine(); // Aggiungi una riga vuota tra le domande
        }

        try
        {
            // Scrivi il contenuto nel file specificato
            File.WriteAllText(path, exportContent.ToString());

            Console.WriteLine("Le domande sono state esportate con successo nel file.");
        }
        catch (IOException e)
        {
            Console.WriteLine("Si è verificato un errore durante l'esportazione delle domande: " + e.Message);
        }
    }


    static List<Domanda> LeggiDomandeDaFile(string filePath, string argomento_)
    {
        List<Domanda> domande = new List<Domanda>();
        string[] lines = File.ReadAllLines(filePath);

        for (int i = 0; i < lines.Length; i += 9) // Supponendo che ogni domanda occupi 8 righe
        {

            string testo = lines[i].Split(":")[1];
            string argomento = argomento_;
            string rispostaA = lines[i + 1].Split(":")[1];
            string rispostaB = lines[i + 2].Split(":")[1];
            string rispostaC = lines[i + 3].Split(":")[1];
            string rispostaD = lines[i + 4].Split(":")[1];
            int rispostaCorretta = int.Parse(lines[i + 5].Split(":")[1]);
            int difficolta = int.Parse(lines[i + 6].Split(":")[1]);
            int tempoRisposta = 10;
            string fonte = lines[i + 7].Split(":")[1];

            Domanda domanda = new Domanda(testo, argomento, rispostaA, rispostaB, rispostaC, rispostaD, rispostaCorretta, difficolta, tempoRisposta, null, fonte);
            domande.Add(domanda);


        }

        return domande;
    }

}
