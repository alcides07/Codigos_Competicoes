using System;

class Program {
  public static void Main (string[] args) {
    string[] valores = Console.ReadLine().Split(' ');

    double A = double.Parse(valores[0]);
    double B = double.Parse(valores[1]);
    double C = double.Parse(valores[2]);

    double triangulo = (A * C) / 2;
    double circulo = 3.14159 * Math.Pow(C, 2);
    double trapezio = ((A + B) * C ) / 2;
    double quadrado = B * B;
    double retangulo = A * B;

    Console.WriteLine($"TRIANGULO: {triangulo:0.000}");
    Console.WriteLine($"CIRCULO: {circulo:0.000}");
    Console.WriteLine($"TRAPEZIO: {trapezio:0.000}");
    Console.WriteLine($"QUADRADO: {quadrado:0.000}");
    Console.WriteLine($"RETANGULO: {retangulo:0.000}");
  }
}