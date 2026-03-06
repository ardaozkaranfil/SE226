#include <iostream>
using namespace std;

int main() {
    int n = 0;
    int steps = 0;
    int sum = 0;
    cout << "Please enter a positive integer greater than 9:";
    cin >> n;

    while (n > 9) {
        if (n > 10) {
            cout << n << "-->";
        }
        else if (n == 10) {
            cout << 10 << "-->" << 1;
            steps++;
            break;
        }
        else {
            cout << n;
        }

        steps++;

        while (n > 0) {
            int temp = n %10;
            sum += temp;
            n /= 10;
        }

        n = sum;
        sum = 0;

    }

    cout << n;

    cout << endl << "Final Value:" << n;
    cout << endl << "Total Steps:" << steps;

    return 0;
}