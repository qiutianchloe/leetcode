#include <stdio.h>
#include "useqsort.h"

int main(int argc, char* argv[]){
    //use quick sort in standard library.
    int arr[] = { 33, 12, 6, 2, 76 };
    int sizeOfArr= (int)( sizeof(arr) / sizeof(arr[0]));//you can only pass the size of array as the parameter into another function, otherwise, it is impossible to calculate the size of array. cause the pointer that deliver into the fucntion is the start of array,instead of arrary itself. 
    useqsort(arr, sizeOfArr); 
    return 0; 
}