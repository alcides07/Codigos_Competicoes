#include <iostream>
using namespace std;

int resposta(int peso){
    if (peso % 2 != 0){ //Se é ímpar
        return 0;
    }

    else if (peso % 2 == 0 && (peso/2) % 2 == 0){ //Partes pares iguais
        return 1;
    }
    
    else{ //Possíveis partes diferentes resultando em um par
        for (int i = 4; i < peso; i += 2){
            if (i + 2 == peso){
                return 1;
            }
        }
    }  
    return 0; 
}

int main(){
    int peso;
    cin >> peso;
    if (resposta(peso)){
        cout << "YES\n";
    }

    else{
        cout << "NO\n";
    }
    return 0;
}