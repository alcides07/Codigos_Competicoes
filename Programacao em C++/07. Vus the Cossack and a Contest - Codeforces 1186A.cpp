#include <iostream>
using namespace std;
 
int main(){
    int participantes, canetas, cadernos;
    cin >> participantes >> canetas >> cadernos;
 
    if (canetas - participantes < 0 || cadernos - participantes < 0){
        cout << "No\n";
    }
 
    else{
        cout << "Yes\n";
    }
 
    return 0;
}