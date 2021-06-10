#include <stdio.h>
#include <stdlib.h>


void 
printArray(int arr[], int size){
    int i; 
    for(i=0; i<size; i++){
        printf("%d ", arr[i]); 
    }
    printf("\n"); 
}

// compare function, compares two elements
int compare (const void * num1, const void * num2) {
   if(*(int*)num1 > *(int*)num2)
    return 1;
   else
    return -1;
}

void useqsort(int arr[], int size) {
   int i;
   printArray(arr, size);
   // calling qsort
   qsort(arr, size, sizeof(int), compare);

   printArray(arr, size);
  
}