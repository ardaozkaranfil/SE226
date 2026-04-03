#include <iostream>
#include <cmath>
using namespace std;

double geometric_series(int n, double r) {
    if (n == 0) {
        return 1;
    }
    else {
        return pow(r, n) + geometric_series(n - 1, r);
    }
}

int main() {
    int n;
    double r;
    cout << "Enter n: ";
    cin >> n;
    cout << "Enter r: ";
    cin >> r;

    double result = geometric_series(n, r);
    cout << "Gn = " << result << endl;

    return 0;
}