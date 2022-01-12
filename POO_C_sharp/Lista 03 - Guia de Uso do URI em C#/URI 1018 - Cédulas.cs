using System; 

public class Program {

  public static void Main(string[] args) {
    int valor = int.Parse(Console.ReadLine());

    int nota_100 = valor / 100;

    int nota_50 = (valor % 100) / 50;

    int nota_20 = ((valor % 100) % 50) / 20;

    int nota_10 = (((valor % 100) % 50) % 20) / 10;

    int nota_5 = ((((valor % 100) % 50) % 20) % 10) / 5;

    int nota_2 = (((((valor % 100) % 50) % 20) % 10) % 5) / 2;

    int nota_1 = ((((((valor % 100) % 50) % 20) % 10) % 5) % 2) / 1;

    Console.WriteLine(valor);
    Console.WriteLine($"{nota_100} nota(s) de R$ 100,00");
    Console.WriteLine($"{nota_50} nota(s) de R$ 50,00");
    Console.WriteLine($"{nota_20} nota(s) de R$ 20,00");
    Console.WriteLine($"{nota_10} nota(s) de R$ 10,00");
    Console.WriteLine($"{nota_5} nota(s) de R$ 5,00");
    Console.WriteLine($"{nota_2} nota(s) de R$ 2,00");
    Console.WriteLine($"{nota_1} nota(s) de R$ 1,00");
  }
}