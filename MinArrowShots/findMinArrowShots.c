#include <stdio.h>
void printArray(int** array, int rows, int cols){
    int i, j;
    for (i=0; i<rows; i++){
        for (j=0; j<cols; j++){
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}

/* compare function, compares the first element of the points by ascending order */
int compare ( const void *pa, const void *pb ) {
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;
    if(a[0] > b[0])
        return 1;
    else
        return -1;
}

/*wrong test case [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]*/
int findMinArrowShots(int** points, int pointsSize, int* pointsColSize){
    /*return the value when pointsSize is 0 and 1*/
    if(pointsSize==0) return 0;
    if(pointsSize==1) return 1;

    int shots = 1;  //last shot
    /* sort the array by ascending order of x.start*/
    qsort(points, pointsSize, sizeof(points[0]), compare);

    int i, boundary = points[0][1]; 
    for (i=1; i<pointsSize; i++){
        /*the ballon that intersect with previous ballon*/
        if(points[i][0]<=boundary){
            //narrow the boundary
            if(boundary>=points[i][1]) boundary = points[i][1]; 
        }else{
            /*the ballon is not intersect with previous ballon, 
            then need to shoot at the previous boundary(which is all previous ballon)*/
            shots++; 
            boundary= points[i][1]; 
        }
    }
    return shots;
}