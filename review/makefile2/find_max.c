#include <stdio.h>



int find_max(int arr[], int length){
    int max = arr[0]; 
    int i; 
    for(i=0; i<length; i++){
        if (arr[i]>max){
            max = arr[i]; 
        }
    }
    return max; 
}

int main(){
    int arr[5] = {1, 8, 6, 3, 4}; 
    int m = find_max(arr, 5); 
    printf("%d is the maximum in the array\n", m);
    return 0;  
}