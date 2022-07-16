#include <iostream>
using namespace std;
 
void prox_ano(string ano){
    for(int i = stoi(ano) + 1; i < 10001; i++){ //Conversão de string para inteiro
        bool exito = true;
        string atual = to_string(i); //Conversão de inteiro para string
        for (int j = 0; j < 4; j++){
            for (int k = j + 1; k < 4; k++){
                if (atual[j] == atual[k]){
                    exito = false;
                    break;
                }
            }
        }
        if (exito){
            cout << atual[0] << atual[1] << atual[2] << atual[3] << "\n";
            break;
        }
    }
}
 
int main(){
    string ano;
    cin >> ano;
    prox_ano(ano);
    return 0;
}