/* Show pointer operations, example 3.
*/
#include  <stdio.h>

void int_swap(int *p1, int *p2);

int
main(int argc, char *argv[]) {
	int x=2, y=3, z=4;
	printf("main: x=%2d, y=%2d, z=%2d\n", x, y, z);
	int_swap(&x, &y);
	printf("main: x=%2d, y=%2d, z=%2d\n", x, y, z);
	int_swap(&x, &z);
	printf("main: x=%2d, y=%2d, z=%2d\n", x, y, z);
	int_swap(&y, &x);
	printf("main: x=%2d, y=%2d, z=%2d\n", x, y, z);
	return 0;
}

/* exchange the values of the two variables indicated 
	by the arguments */
void
int_swap(int *p1, int *p2) {
	int tmp;
	tmp = *p1;
	*p1 = *p2;
	*p2 = tmp;
}

/* =====================================================================
   Program written by Alistair Moffat, as an example for the book
   "Programming, Problem Solving, and Abstraction with C", Pearson
   Custom Books, Sydney, Australia, 2002; revised edition 2012,
   ISBN 9781486010974.

   See http://people.eng.unimelb.edu.au/ammoffat/ppsaa/ for further
   information.

   Prepared December 2012 for the Revised Edition.
   ================================================================== */