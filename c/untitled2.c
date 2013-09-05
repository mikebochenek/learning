#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * http://stackoverflow.com/questions/7684359/using-nanosleep-in-c
 */
int main(int argc, char **argv) {
   struct timespec tim, tim2;
   tim.tv_sec  = 0;
   tim.tv_nsec = 500000000L;
   int i = 0;

   for (i = 0; i < 100; i++) {
      if(nanosleep(&tim , &tim2) < 0 ) {
         printf("Nano sleep system call failed \n");
         return -1;
      } else {
		  printf(".");
		  fflush(stdout); 
	  }
   }

   printf("Nano sleep successfull \n");

   return 0;
}

