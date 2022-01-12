using System;

class Program {
  public static int MDC(int x, int y){
    if (y == 0){
        return x;
    }

    return MDC(y, x % y);
  }

  public static int MMC(int x, int y){
      return Math.Abs(x * y) / MDC(x, y);
  }

  public static void Main (string[] args) {
    int n1 = int.Parse(Console.ReadLine());
    int n2 = int.Parse(Console.ReadLine());

    Console.WriteLine($"O MMC entre {n1} e {n2} é: {MMC(n1, n2)}");
  }
}