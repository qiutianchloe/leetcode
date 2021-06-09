#include <stdio.h>

void swap(int* a, int* b){
    int temp; 
    temp = *a; 
    *a = *b; 
    *b = temp; 
}

int main(){
    int a = 10; 
    int b = 20; 

    int* pa = &a; 
    int* pb = &b; 

    swap(pa, pb); 

    printf("a = %d, b =%d", a, b); 
}