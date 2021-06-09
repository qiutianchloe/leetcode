#include "sep.h"
#include <stdio.h>


int main(){
    int arr[5] = {1, 8, 6, 3, 4}; 
    int m = find_max(arr, 5); 
    printf("%d is the maximum in the array\n", m);
    return 0;  
}