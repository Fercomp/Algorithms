#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string multiplyStrings(string a, string b) {
    int n = a.size();
    int m = b.size();
    vector<int> result(n + m, 0);

    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            int p = (a[i] - '0') * (b[j] - '0');
            int sum = p + result[i + j + 1];

            result[i + j + 1] = sum % 10;
            result[i + j] += sum / 10;
        }
    }

    string r;
    for (int num : result) {
        if (!(r.empty() && num == 0))
            r.push_back(num + '0');
    }

    return r.empty() ? "0" : r;
}

int main() {
    string n, g;
    while (cin >> n >> g) {
        cout << multiplyStrings(n, g) << endl;
    }
    return 0;
}