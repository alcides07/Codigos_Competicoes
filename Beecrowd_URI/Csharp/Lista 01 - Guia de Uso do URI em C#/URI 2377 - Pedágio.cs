using System; 

public class Program {

  public static void Main(string[] args) {
    string[] l1 = Console.ReadLine().Split(' ');
    string[] l2 = Console.ReadLine().Split(' ');

    int comprimento = int.Parse(l1[0]);
    int distancia_pedagios = int.Parse(l1[1]);

    int custo_km = int.Parse(l2[0]);
    int valor_pedagio = int.Parse(l2[1]);

    int qtd_pedagios = comprimento/distancia_pedagios;

    int gasto_pedagios = qtd_pedagios * valor_pedagio;
    int gasto_gasolina = comprimento * custo_km;

    Console.WriteLine($"{gasto_gasolina + gasto_pedagios}");
  }
}