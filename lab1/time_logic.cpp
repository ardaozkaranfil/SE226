#include <string>
#include <iostream>
using namespace std;

int main() {
    int inputSeconds;
    cout << "Please enter a large integer representing total number of seconds.";
    cin >> inputSeconds;

    int seconds = inputSeconds % 60;
    int minutes = (inputSeconds % 3600) / 60;
    int hours = inputSeconds / 3600;

    cout << inputSeconds << " seconds is " << hours << " hours, " << minutes << " minutes, " << seconds << " seconds.";
    return 0;
}