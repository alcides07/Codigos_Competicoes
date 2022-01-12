using System;

class Program {
  public static void Main (string[] args) {
    string[] valores = Console.ReadLine().Split(' ');
    
    int A = int.Parse(valores[0]);
    int B = int.Parse(valores[1]);
    int C = int.Parse(valores[2]);

    int[] ordem = {A, B, C};

    Array.Sort(ordem);

    Console.WriteLine(ordem[0]);
    Console.WriteLine(ordem[1]);
    Console.WriteLine($"{ordem[2]}\n");

    Console.WriteLine(A);
    Console.WriteLine(B);
    Console.WriteLine(C);
  }
}