#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main() {
  int casos, n, x; 
  cin >> casos;
  for (int i = 0; i < casos; i++) {
    cin >> n;
    cin >> x;
    int array[n * 2];
    
    for (int i = 0; i < n * 2; i++) {
      cin >> array[i];
    }
    sort(array, array + n*2);
    
    int array1[n];
    int array2[n];
 
    for (int i = 0; i < n; i++) {
      array1[i] = array[i];
    }
 
    int m = n;
    for (int i = 0; i < n; i++) {
      array2[i] = array[m];
      m++;
    }
    string ans;
    for (int i = 0; i < n; i++) {
      if (array2[i] - array1[i] >= x) {
        ans = "YES";
      }
      else {
        ans = "NO";
        break;
      }
    }
    cout << ans << "\n";
  }
}