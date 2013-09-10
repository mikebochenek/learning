#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * http://stackoverflow.com/questions/7684359/using-nanosleep-in-c
 */
int main(int argc, char **argv) {
   struct timespec tim, tim2;
   tim.tv_sec  = 0;
   tim.tv_nsec = 100000000L;
   int i = 0;

   struct timeval cur_time1, cur_time2, tdiff;

   gettimeofday(&cur_time1,NULL);
   
   for (i = 0; i < 10000; i++) {
      if(nanosleep(&tim , &tim2) < 0 ) {
         printf("Nano sleep system call failed \n");
         return -1;
      } else {
		  printf("%10d.%d\n", i / 10, i % 10);
		  fflush(stdout); 
	  }
   }

   gettimeofday(&cur_time2,NULL);

   tdiff.tv_sec = cur_time2.tv_sec - cur_time1.tv_sec;
   tdiff.tv_usec = cur_time2.tv_usec + (1000000 - cur_time1.tv_usec);

   // thx http://stackoverflow.com/questions/1444428/time-stamp-in-the-c-programming-language
   printf("end tdiff tv_sec:%ld tv_usec:%ld\n",tdiff.tv_sec, tdiff.tv_usec);

   printf("Nano sleep successfull \n");

   return 0;
}

