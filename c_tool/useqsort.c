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

   /*
   Parameters
        base − This is the pointer to the first element of the array to be sorted.

        nitems − This is the number of elements in the array pointed by base.

        size − This is the size in bytes of each element in the array.

        compar − This is the function that compares two elements.
   */
   qsort(arr, size, sizeof(int), compare);

   printArray(arr, size);
  
}