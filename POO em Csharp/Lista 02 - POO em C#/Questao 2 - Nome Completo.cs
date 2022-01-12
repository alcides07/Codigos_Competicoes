using System;

class Program {
  public static void Main (string[] args) {
    Console.WriteLine ("Digite seu nome completo:");
    string[] nome = Console.ReadLine().Split(' ');
    Console.WriteLine($"Bem-vindo ao c#, {nome[0]}");
  }
}