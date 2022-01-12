using System;

class Program {
  public static void Main (string[] args) {
    Console.WriteLine("Digite a base e a altura do retângulo:");
    double bas = double.Parse(Console.ReadLine());
    double alt = double.Parse(Console.ReadLine());

    double area = bas * alt;
    double perimetro = (bas * 2) + (alt * 2);
    double diagonal = Math.Pow(bas, 2) + Math.Pow(alt, 2);
    diagonal = Math.Sqrt(diagonal);

    Console.WriteLine($"Área = {area:0.00} - Perímetro = {perimetro:0.00} - Diagonal = {diagonal:0.00}");
  }
}