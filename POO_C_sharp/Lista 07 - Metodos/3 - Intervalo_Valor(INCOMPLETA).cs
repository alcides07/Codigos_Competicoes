using System;

class Program {

  public static void Intervalo(double x, out int inicio, out int fim){
    string conversor = x.ToString();
    char conversor_2 = conversor[0];

    char valor = conversor_2;

    Console.WriteLine(valor);

    inicio = 0;
    fim = 0;

    
  }

  public static void Main (string[] args) {
      double numero = double.Parse(Console.ReadLine());
      int inicio;
      int fim;
      Intervalo(numero, out inicio, out fim);

      //Console.WriteLine($"{inicio} {fim}");

  }
}