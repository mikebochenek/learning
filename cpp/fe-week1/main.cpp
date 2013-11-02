#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    double total = 0.0;
    for (int i = 0; i < 20; i++) {
        total += 50000 / pow (1.1, i);
        //cout << total << endl;
        printf ("%f\n", total);
    }

    return 0;
}
