using System;

class Program {
  public static void Main (string[] args) {
    string[] cartas = Console.ReadLine().Split(' ');

    string situacao = "";
    bool crescente = false;
    bool decrescente = false;
                             
    for (int i = 0; i < 4; i++){ 
      if (int.Parse(cartas[i]) < int.Parse(cartas[i + 1])){  
        situacao = "C";
        crescente = true;
      }

      else if (int.Parse(cartas[i]) > int.Parse(cartas[i + 1])){
        situacao = "D";
        decrescente = true;
      }

      if (crescente == true && decrescente == true){
        situacao = "N";
      }

    } //Fechamento do for

    Console.WriteLine(situacao);
  }
    }