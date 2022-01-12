using System;

class Program {
  public static void Main (string[] args) {
    float nota1 = float.Parse(Console.ReadLine());
    float nota2 = float.Parse(Console.ReadLine());

    bool situacao_n1 = false;
    bool situacao_n2 = false;

    float media;

    if (nota1 < 0 || nota1 > 10){
      while (situacao_n1 == false){
        Console.WriteLine("nota invalida");
        nota1 = float.Parse(Console.ReadLine());

        if (nota1 >= 0 && nota1 <= 10){
          situacao_n1 = true;
          break;
        }
      }
    }

    else{
      situacao_n1 = true;
    }

    if (nota2 < 0 || nota2 > 10){
      while (situacao_n2 == false){
        Console.WriteLine("nota invalida");
        nota2 = float.Parse(Console.ReadLine());

        if (nota2 >= 0 && nota2 <= 10){
          situacao_n2 = true;
          break;
        }
      }
    }

    else{
      situacao_n2 = true;
    }

    if (situacao_n1 == true && situacao_n2 == true){
      media = (nota1 + nota2) / 2;
      Console.WriteLine($"media = {media:0.00}");
    }
  }
}