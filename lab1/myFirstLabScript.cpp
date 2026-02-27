#include <string>
#include <iostream>
using namespace std;
int main() {
    string name;
    string ID;

    cout << "What is your name?";
    cin >> name;

    cout << "Hello" << name << "\n What is your Student ID?";
    cin >> ID;
    cout << "Your ID is " << ID;
    return 0;
}