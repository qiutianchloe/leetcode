#include  <stdio.h>

int
main(int argc, char *argv[]) {
	int n=123, *pi;
	double x=456.789, *pd;
	printf("  n = %3d,   x = %7.3f\n", n, x);
	pi = &n;
	pd = &x;
	printf("*pi = %3d, *pd = %7.3f\n", *pi, *pd);
	*pi = *pi+1;
	*pd = *pd / *pi;
	printf("*pi = %3d, *pd = %7.3f\n", *pi, *pd);
	printf("  n = %3d,   x = %7.3f\n", n, x);
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