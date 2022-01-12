using System; 

public class Program {

  public static void Main(string[] args) {
    int distancia = int.Parse(Console.ReadLine());
    double combustivel = double.Parse(Console.ReadLine());

    double consumo = distancia / combustivel;

    Console.WriteLine($"{consumo:0.000} km/l");
  }
}