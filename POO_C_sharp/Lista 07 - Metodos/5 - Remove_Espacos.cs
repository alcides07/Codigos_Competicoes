using System;

class Program {
  public static string FormatarTexto(string texto){
    string texto_formatado = texto.Trim();
    return texto_formatado;
  }

  public static void Main (string[] args) {
      string texto = Console.ReadLine();
      Console.WriteLine($"O texto antes da formatação era: {texto}\n");
      Console.WriteLine($"O novo texto sem espaços no início e no fim é: {FormatarTexto(texto)}");
      
   }
}