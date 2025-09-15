// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>
// using namespace std;

// string sum_reversed(string a, string b) {
//     int n = a.size();
//     int m = b.size();
//     int minimo = min(m, n); 
//     vector<int> result(max(m, n) + 1, 0);

//     for (int i=0; i<minimo; i++) {
//         int p = (a[i] - '0') + (b[i] - '0') + result[i];
//         result[i] = p % 10;
//         result[i + 1] = p / 10;
//     }

//     while (n < m) {
//         int p =  (b[n] - '0') + result[n];
//         result[n] = p % 10;
//         result[n + 1] = p / 10;
//     }

//     while (m < n) {
//         int p = (a[m] - '0') + result[m];
//         result[m] = p % 10;
//         result[m + 1] = p / 10;
//     }

//     string r;
//     for (int num : result) {
//         if (!(r.empty() && num == 0))
//             r.push_back(num + '0');
//     }

//     return r.empty() ? "0" : r;
// }

// int main() {
//     int n;
//     cin >> n;

//     for (int i=0; i<n; i++) {
//         string n, g;
//         cin >> n >> g;
//         cout << sum_reversed(n, g) << endl;
//     }
//     return 0;
// }

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void sum_rever(string a, string b) {
    int n = a.size();
    int m = b.size();
    int l = max(n, m);
    vector<int> result(l + 1, 0);

    for (int i = 0; i < l; i++) {
        int da = (i < n ? a[i] - '0' : 0);
        int db = (i < m ? b[i] - '0' : 0);
        int p = da + db + result[i];

        result[i] = p % 10;
        result[i + 1] += p / 10;
    }
 
    int last = l;
    while (last > 0 && result[last] == 0) {
        last--;
    }

    string r;
    for (int i = 0; i <= last; i++) {
        r.push_back(result[i] + '0');
    }
    cout << r << endl;
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        string n, g;
        cin >> n >> g;
        sum_rever(n, g);
    }
    return 0;
}