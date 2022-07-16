#include <iostream>
using namespace std;

int calc(int custo_banana, int saldo, int qtd_bananas){
    int qtd_emprestado, valor_total = 0;

    for (int i = 1; i < qtd_bananas + 1; i++){
        valor_total += (custo_banana * i);
    }

    qtd_emprestado = valor_total - saldo;

    return (qtd_emprestado > 0) ? qtd_emprestado : 0;
}

int main(){
    int custo_banana, saldo, qtd_bananas;
    cin >> custo_banana >> saldo >> qtd_bananas;
    cout << calc(custo_banana, saldo, qtd_bananas) << "\n";
    return 0;
}