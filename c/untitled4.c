#include <stdint.h>
#include <stdio.h>
#include <time.h>

/** https://www.hanshq.net/big-endian-qemu.html
      $ sudo apt-get install qemu-user gcc-mips-linux-gnu
      $ mips-linux-gnu-gcc -static endian.c && qemu-mips a.out
      $ sudo apt-get install gcc-s390x-linux-gnu
      $ s390x-linux-gnu-gcc -static endian.c && qemu-s390x a.out
   and also from - https://stackoverflow.com/a/1445808
*/
int main(void) {
   uint32_t x = 0x12345678;
   time_t t0 = time(0);
   struct tm *tm =localtime(&t0);

   for (int i = 0; i < sizeof(x); i++) {
      printf("\tmem[%d] = 0x%02x\n", i, ((char*)&x)[i]);
   }

   printf (" (%ti) ◼ %d-%d-%d ◼ %02d:%02d:%02d\n", 
      t0, tm->tm_year+1900, tm->tm_mon+1, tm->tm_mday, 
      tm->tm_hour, tm->tm_min, tm->tm_sec);

   return 0;
}
