#include <iostream>
using namespace std;

void solve(long long array[], int tamanho){
    long long movimentos_total = 0, movimento_atual = 0;

    for (int i = 0; i < tamanho - 1; i++){
        if (array[i] > array[i + 1]){
            movimento_atual = (array[i] - array[i + 1]);
            movimentos_total += movimento_atual;
            array[i + 1] += movimento_atual;
        }
    }
    cout << movimentos_total << "\n";
}

int main(){
    int tamanho;
    cin >> tamanho;
    long long array[tamanho];

    for (int i = 0; i < tamanho; i++){
        cin >> array[i];
    }
    solve(array, tamanho);
    return 0;
}