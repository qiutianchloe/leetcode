#include <stdio.h>
#include <stdlib.h>
#include "findMinArrowShots.h"


int main(){
    int rows=10, cols=2, i=0;
    int **x;
 
    /* allocate the array */
    x = malloc(rows * sizeof *x);
    for (i=0; i<rows; i++){
        x[i] = malloc(cols * sizeof *x[i]);
    }
    //[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    x[0][0] = 3;
    x[0][1] = 9;
    x[1][0] = 7;
    x[1][1] = 12;
    x[2][0] = 3;
    x[2][1] = 8;
    x[3][0] = 6;
    x[3][1] = 8;
    x[4][0] = 9;
    x[4][1] = 10;
    x[5][0] = 2;
    x[5][1] = 9;
    x[6][0] = 0;
    x[6][1] = 9;
    x[7][0] = 3;
    x[7][1] = 9;
    x[8][0] = 0;
    x[8][1] = 6;
    x[9][0] = 2;
    x[9][1] = 8;

    int rannum = 0; 
    int* fake;
    fake = &rannum;  

    int num = findMinArrowShots(x, rows, fake); 
    
    printf("the result is %d\n", num);

    /* deallocate the array */
    for (i=0; i<rows; i++){
        free(x[i]);
    }
    free(x);
    return 0; 
}