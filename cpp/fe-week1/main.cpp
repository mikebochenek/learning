#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

using namespace std;

int timeexample();

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
    timeexample();
    return 0;
}

int timeexample() {
   struct timespec tim, tim2;
   tim.tv_sec  = 0;
   tim.tv_nsec = 100000000L;
   int i = 0;

   for (i = 0; i < 10; i++) {
      if(nanosleep(&tim , &tim2) < 0 ) {
         printf("Nano sleep system call failed \n");
         return -1;
      } else {
		  printf("%10d.%d\n", i / 10, i % 10);
		  fflush(stdout);
	  }
   }

   printf("Nano sleep successfull \n");

   return 0;
}
