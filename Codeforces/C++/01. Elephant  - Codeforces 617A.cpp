#include <iostream>
using namespace std;

int func(int pos_atual, int pos_amg, int passos){
    int num = 5;
    while (pos_atual < pos_amg){
        if (pos_atual + num <= pos_amg){
            pos_atual += num;
            passos++;
        }
        else{
            num--;
        }
    }
    return passos;
}

int main(){
    int pos_amg;
    cin >> pos_amg;
    cout << func(0, pos_amg, 0) << "\n";
    return 0;
}