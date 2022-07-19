#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int array[n];

    if (n != 2 && n != 3){
        for (int i = 0; i < n; i++){ // Preenchendo o array
            array[i] = i + 1;
        }

        for (int i = 1; i < n; i+= 2){ // Mostrando os pares
            cout << array[i] << " ";
        }

        for (int i = 0; i < n; i+= 2){ // Mostrando os ímpares
            cout << array[i] << " ";
        }
        cout << "\n";
    }

    else{
        cout << "NO SOLUTION\n";
    }
}  