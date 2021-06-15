#include <stdio.h>
#include "findContentChildren.h"

int main(){
    int g1[2] = {1,2}; 
    int s1[3] = {1,2,3};
    
    int *g = g1; 
    int *s = s1; 

    int num = findContentChildren(g, 2, s, 3); 

    printf("The result is %d\n", num); 
    return 0; 
}