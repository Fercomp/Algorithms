#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    int n = a.size();
    int m = b.size();
    if (n != m) {
        cout << 1;
        return 0;
    }

    for (int i=0; i<n; i++) {
        if (a[i] != b[i]) {
            cout << 1;
            return 0;
        }
    }
    
    cout << a;
    return 0;
}