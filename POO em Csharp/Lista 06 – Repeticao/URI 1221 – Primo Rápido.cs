using System;

class Program {

  public static bool divisores(long num){
        if (num == 2){
            return true;
        }

        if (num % 2 == 0){
            return false;
        }

        for (long i = 3; i * i < num + 1; i += 2){
            if (num % i == 0){
                return false;
            }
        }
        return true;
  }

  public static void Main (string[] args) {
    int casos = int.Parse(Console.ReadLine());
    int i = 0;
    while (i < casos){
      long numero = long.Parse(Console.ReadLine());

      if (divisores(numero)){ 
           Console.WriteLine("Prime");
      }
      
      else{
            Console.WriteLine("Not Prime");
      }
        i++;

       }
    } 
  }