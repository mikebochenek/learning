#include <stdio.h>
#include <stdlib.h>

/**
 * Mike Bochenek 18.02.2013 21:49:52
 */

struct card {
	char *face;
	char *suit;
};

struct deck  {
	struct card c[52];
};

void bsort()  {
	//TODO
}

void play() {
	int i;
	struct card c;
	for (i = 0; i < 1000/*00000*/; i++) {
		c.face = malloc(10); // but wait, that makes no sense!
	}
	int x = 10;
	c.suit = "hearts";
	printf("welcome to my world of pointers %p", &c);
	printf("\n%ld %d", sizeof(c.face), x);
	printf("\n%s\n", c.suit);
	free(c.face);
}

int main(void) {
	play();
	bsort();
	return 0;
}

