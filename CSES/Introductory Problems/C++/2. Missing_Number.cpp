#include <iostream>
#include <algorithm>
using namespace std;
 
void solve(int array[], int tamanho){ 
  int num = 1; 
  for(int i = 0; i < tamanho + 1; i++){
    if (array[i] != num){
      cout << num << "\n";
      break;
    }
    num++;
  }
}
 
int main() {
  int n;
  cin >> n;
  int array[n - 1];
  
  for (int i = 0; i < n - 1; i++){
    cin >> array[i];
  }
 
  sort(array, array + (n - 1));
  solve(array, n - 1);
}