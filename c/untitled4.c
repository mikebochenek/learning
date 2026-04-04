#include <stdint.h>
#include <stdio.h>

/** https://www.hanshq.net/big-endian-qemu.html
$ sudo apt-get install qemu-user gcc-mips-linux-gnu
$ mips-linux-gnu-gcc -static endian.c && qemu-mips a.out
$ sudo apt-get install gcc-s390x-linux-gnu
$ s390x-linux-gnu-gcc -static endian.c && qemu-s390x a.out
*/
int main(void)
{
   uint32_t x = 0x12345678;
   int i;

   for (i = 0; i < sizeof(x); i++) {
      printf("mem[%d] = 0x%02x\n", i, ((char*)&x)[i]);
    }

    return 0;
}
