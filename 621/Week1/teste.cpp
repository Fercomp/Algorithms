#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        string a, b;
        cin >> a >> b;

        int n = a.length();
        int m = b.length();
        int biggest = max(n, m);

        vector<int> result(biggest + 1, 0);
        if (a == "0" && b == "0") {
            cout << "0\n";
            continue;
        }

        for (int i = 0; i < biggest; ++i) {
            int j = (i > n - 1) ? 0 : a[i] - '0';
            int k = (i > m - 1) ? 0 : b[i] - '0';
            
            int total = result[i] + j + k;

            int unity = total % 10;
            int decimal = total / 10; 
            
            result[i] = unity;
            result[i + 1] += decimal;
        }
        
        int last = biggest;
        while (last > 0 && result[last] == 0) {
            last--;
        }
        int first = 0;
        while (first < last && result[first] == 0) {
            first++;
        }
        for (int i = first; i <= last; ++i) {
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}