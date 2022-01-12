using System;

class Program {
  public static void Ordenar(ref int x, ref int y, ref int z){
    int[] ordem = {x, y, z};
    Array.Sort(ordem);

    x = ordem[0];
    y = ordem[1];
    z = ordem[2];
  }

    public static void Main (string[] args) {
        int x = int.Parse(Console.ReadLine());
        int y = int.Parse(Console.ReadLine());
        int z = int.Parse(Console.ReadLine());
        Ordenar(ref x, ref y, ref z);

        Console.WriteLine($"Resultado em ordem crescente: {x}, {y}, {z}");
    }
}