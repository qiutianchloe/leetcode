#include<stdio.h>
#include<stdlib.h>
#include"sqrtx.h"

int main(int argc, char** argv){
    int num = 8; 
    int result = mySqrt(num); 
    printf("result for %d is %d\n", num, result);
    return 0; 
}