using System;

class Program {
  public static void Main (string[] args) {
    
    string[] aposta = Console.ReadLine().Split(' ');
    string[] sorteados = Console.ReadLine().Split(' ');

    int n1 = int.Parse(aposta[0]);
    int n2 = int.Parse(aposta[1]);
    int n3 = int.Parse(aposta[2]);
    int n4 = int.Parse(aposta[3]);
    int n5 = int.Parse(aposta[4]);
    int n6 = int.Parse(aposta[5]);

    int acertos = 0;
    
    for (int i = 0; i < 6; i++){ 

      if (int.Parse(sorteados[i]) == n1 ||
          int.Parse(sorteados[i]) == n2 ||
          int.Parse(sorteados[i]) == n3 ||
          int.Parse(sorteados[i]) == n4 ||
          int.Parse(sorteados[i]) == n5 ||
          int.Parse(sorteados[i]) == n6
        )

        acertos++; //Execução da condicional caso verdadeira

    } //Fechamento do for

    switch (acertos){
      case 3:
        Console.WriteLine("terno"); break;

      case 4:
        Console.WriteLine("quadra"); break;

      case 5:
        Console.WriteLine("quina"); break;

      case 6:
        Console.WriteLine("sena"); break;

      default: 
        Console.WriteLine("azar"); break;
  }
  }
  }