#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    while (cin >> n) {
        if (n == "0") break;

        int mod = 0;
        for (char c : n) {
            mod = (mod * 10 + (c - '0')) % 17;
        }

        cout << (mod == 0 ? 1 : 0) << endl;
    }
    return 0;
}