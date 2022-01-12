using System; 

public class Program {

  public static void Main(string[] args) {
    string nome = Console.ReadLine();
    double salario = double.Parse(Console.ReadLine());
    double vendas = double.Parse(Console.ReadLine());

    double bonus = (vendas * 15) / 100;

    double total = bonus + salario;

    Console.WriteLine($"TOTAL = R$ {total:0.00}");
  }
}