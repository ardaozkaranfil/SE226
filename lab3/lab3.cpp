#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
}

int findMax(int* arr, int size) {
    int max = INT_MIN;

    for (int i = 0; i < size; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
    }
    return max;
}

void reverseArray(int* arr, int size) {
    int* start = arr;
    int* end = arr + size - 1;

    while (start < end) {
        swapValues(start, end);
        start++;
        end--;
    }
}

int* createArray(int size) {
    int* array = new int[size];
    cout << "Enter values:" << endl;
    for (int i = 0; i < size; i++) {
        cin >> array[i];
    }
    return array;
}

void deleteArray(int* arr) {
    delete[] arr;
}
int main() {
    int arraySize;
    cout << "Creating dynamic array..." << "\n\nEnter array size:";
    cin >> arraySize;
    int* array = createArray(arraySize);
    cout << "Maximum element: " << findMax(array, arraySize) << "\n----------------------------------\n";

    int a = 5;
    int b = 8;
    cout << "Swapping two numbers" << "\n\nBefore Swap" << "\na = " << a << "\nb = " << b;
    swapValues(&a, &b);
    cout << "\n\nAfter Swap" << "\na = " << a << "\nb = " << b << "\n----------------------------------\n";

    cout << "Reversing array...\n";
    reverseArray(array, arraySize);
    cout << "Array after reverseArray:\n";
    printArray(array, arraySize);
    cout << "\n----------------------------------\n";

    cout << "Deleting array...";
    deleteArray(array);
    cout << "\nMemory released successfully.";
}
