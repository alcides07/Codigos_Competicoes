using System;

class Program {
  public static void Main (string[] args) {
    Console.WriteLine ("Digite o intervalo de tempo no formato HH:MM:SS");
    string[] tempo = Console.ReadLine().Split(":");

    long horas = int.Parse(tempo[0]) * 3600;
    long minutos = int.Parse(tempo[1]) * 60;
    long segundos = int.Parse(tempo[2]);

    long distancia = (horas + minutos + segundos) * 300000;

    Console.WriteLine($"A luz percorreu {distancia} km nesse intervalo");
  }
}