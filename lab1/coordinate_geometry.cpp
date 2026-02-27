#include <string>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x1;
    double x2;
    double y1;
    double y2;

    cout << "Enter x1: ";
    cin >> x1;
    cout << "Enter x2: ";
    cin >> x2;
    cout << "Enter y1: ";
    cin >> y1;
    cout << "Enter y2: ";
    cin >> y2;

    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1 ,2));
    cout << distance;


    cout << "\n*******" << "\n *****" << "\n  ***" << "\n   *";
    return 0;
}