#include <iostream>
using namespace std;

int main(){
    int n, contador = 0;
    string s;
    cin >> n >> s;
    int tamanho = s.size();
    for (int i = 0; i < tamanho; i++){
        if (s[i] == s[i + 1]){
            contador++;
        }
    }
    cout << contador << "\n";
}