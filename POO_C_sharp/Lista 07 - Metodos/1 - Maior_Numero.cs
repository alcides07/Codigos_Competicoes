using System;

class Program {
  public static double Maior(double x, double y){
      double maior;
      maior = x;

      if (y > maior){
        maior = y;
      }
      
      return maior;
  }

  public static void Main (string[] args) {
    double n1 = double.Parse(Console.ReadLine());
    double n2 = double.Parse(Console.ReadLine());
    double maior = Maior(n1, n2);
    Console.WriteLine($"O maior entre os dois números digitados é: {maior}");
  }

}