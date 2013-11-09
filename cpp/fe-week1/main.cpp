#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

using namespace std;

void question1() {
    double total = 0.0;
    for (int i = 0; i < 20; i++) {
        total += 50000 / pow (1.1, i);
        //cout << total << endl;
        //printf ("%f\n", total);
    }
}

int fibonacci(int i) {
    if (i <= 1) {
        return 1;
    } else {
        return fibonacci(i - 2) + fibonacci(i - 1);
    }
}

int main() {
    question1();
    for (int i = 0; i < 10; i++) {
        //cout << fibonacci(i) << endl;
        fibonacci(i);
    }
    return 0;
}

