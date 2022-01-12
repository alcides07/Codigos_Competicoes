using System; 

public class Program {

  public static void Main(string[] args) {
    string[] valores = Console.ReadLine().Split(' ');
    int maior = int.Parse(valores[0]);

    int n1 = int.Parse(valores[1]);
    int n2 = int.Parse(valores[2]);

    if (n1 > maior){
      maior = n1;
    }

    if (n2 > maior){
      maior = n2;
    }

    Console.WriteLine($"{maior} eh o maior");
  }
}