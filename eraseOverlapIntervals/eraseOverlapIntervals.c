#include <stdio.h>
#include <stdlib.h>


void printArray(int** array, int rows, int cols){
    int i, j;
    for (i=0; i<rows; i++){
        for (j=0; j<cols; j++){
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}

/* compare function, compares the second element of the interval by ascending order */
int compare ( const void *pa, const void *pb ) {
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;
    if(a[1] > b[1])
        return 1;
    else
        return -1;
}


int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize){
    /* return 0 for 0 and 1 interval condition */
    int remove = 0; 
    if(intervalsSize==0||intervalsSize==1){
        return remove; 
    }
    /* sort the array */
    qsort(intervals, intervalsSize, sizeof(intervals[0]), compare);
    int i=0, boundary=intervals[0][1]; 
    for (i=1; i<intervalsSize; i++){
        if(intervals[i][0]<boundary){
            //delete the interval that intersect with the previous interval
            remove++; 
        }else{
            boundary=intervals[i][1];
        }
    }
    return remove; 
}

