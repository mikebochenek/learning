#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <sys/time.h>

// using namespace std;

int timeexample();

void question1() {
    double total = 0.0;
    for (int i = 0; i < 20; i++) {
        total += 50000 / pow (1.1, i);
        printf ("%f\n", total);
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
        int f = fibonacci(i);
        printf ("fib: %i -> %i\n", i, f);
    }
    timeexample();

    return 0;
}

int timeexample() {
   struct timespec tim, tim2;
   tim.tv_sec  = 0;
   tim.tv_nsec = 100000000L;
   int i = 0;
   timespec ts;
   double* myPtr = (double*)malloc(sizeof(double)*5);

   // http://stackoverflow.com/questions/275004/c-timer-function-to-provide-time-in-nano-seconds
   //clock_gettime(CLOCK_REALTIME, &ts); // Works on Linux

   for (i = 0; i < 12; i++) {
      if(nanosleep(&tim , &tim2) < 0 ) {
         printf("Nano sleep system call failed \n");
         return -1;
      } else {
		  printf("%6d.%d\n", i / 10, i % 10);
		  fflush(stdout);
	  }
   }

   printf("Nano sleep successfull \n");
   free(myPtr);
   return 0;
}
