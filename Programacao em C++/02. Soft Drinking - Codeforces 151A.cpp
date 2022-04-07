#include <iostream>

using namespace std;

int brindes(int n, int k, int l, int c, int d, int p, int nl, int np){
    int qtd_brindes, tml, tbml, tbl, tbs;
    tml = k * l;      //Total de mililitros
    tbml = tml / nl;  //Total de brindes possíveis com mililitros da bebida.
    tbl = c * d;      //Total de brindes possíveis com limões.
    tbs = p / np;     //Total de brindes possíveis com o sal.

    int menor = tbml;
    if (tbl < menor){
        menor = tbl;
    }
    if (tbs < menor){
        menor = tbs;
    }
    qtd_brindes = menor / n;
    return qtd_brindes;
}

int main(){
    int n, k , l , c, d, p, nl, np;
    cin >> n >> k >> l >> c >> d >> p >> nl >> np;
    cout << brindes(n, k , l , c, d, p, nl, np) << "\n";
    return 0;
}