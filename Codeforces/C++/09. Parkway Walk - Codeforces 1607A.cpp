#include <iostream>
using namespace std;

int main(){
    int casos;
    cin >> casos;
    while (casos--){
        int qtd_bancos, energia, restauracao = 0;
        cin >> qtd_bancos >> energia;
        int bancos[qtd_bancos];
        for (int i = 0; i < qtd_bancos; i++){
            cin >> bancos[i];
        }

        for (int i = 0; i < qtd_bancos; i++){
            if (energia < bancos[i]){
                restauracao += bancos[i] - energia;
                energia = 0;
            }

            else{
                energia -= bancos[i];       
            }
        }
        cout << restauracao << "\n";

    }
    return 0;
}