#include <stdio.h>
#include <stdlib.h>
#include "eraseOverlapIntervals.h"


int main(){
    int rows=4, cols=2, i=0;
    int **x;
 
    /* allocate the array */
    x = malloc(rows * sizeof *x);
    for (i=0; i<rows; i++){
        x[i] = malloc(cols * sizeof *x[i]);
    }
    x[0][0] = 1;
    x[0][1] = 2;
    x[1][0] = 2;
    x[1][1] = 3;
    x[2][0] = 3;
    x[2][1] = 4;
    x[3][0] = 1;
    x[3][1] = 3;

    int rannum = 0; 
    int* fake;
    fake = &rannum;  

    int num = eraseOverlapIntervals(x, rows, fake); 
    
    printf("the result is %d\n", num);

    /* deallocate the array */
    for (i=0; i<rows; i++){
        free(x[i]);
    }
    free(x);
}
