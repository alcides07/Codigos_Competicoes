#include <iostream>
using namespace std;
 
void solve(){
    int casos;
    cin >> casos;
    while(casos--){
        string numero;
        cin >> numero;
        string divisor = "1";
        int tamanho = numero.size();
        for(int i = 0; i < tamanho - 1; i++){
            divisor += "0";
        }
        cout << stoi(numero) - stoi(divisor) << "\n";
    }
}
 
int main(){
    solve();
    return 0;
}