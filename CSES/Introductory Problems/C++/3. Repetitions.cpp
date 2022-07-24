#include <iostream>
using namespace std;

void solve(string sequencia){
    int maior_momentanea = 1, maior = 1;
    
    for(int i = 0; i < (int)sequencia.size(); i++){
        if (sequencia[i] == sequencia[i + 1]){
            maior_momentanea++;
        }
        else{
            if (maior_momentanea >= maior){
                maior = maior_momentanea;
            }
            maior_momentanea = 1;
        }
    }
    cout << maior << "\n";
}

int main(){
    string sequencia;
    cin >> sequencia;
    solve(sequencia);
    return 0;
}