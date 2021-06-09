/* Show pointer operations, example 1.
*/
#include  <stdio.h>

int
main(int argc, char *argv[]) {
	static int w;
	int x, y, z;
	printf("&w = %16p\n&x = %16p\n&y = %16p\n&z = %16p\n",
		&w, &x, &y, &z);
	return 0;
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