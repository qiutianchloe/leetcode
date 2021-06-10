#include <stdio.h>
#include "candy.h"

int main(){
    //case 1
    int rating[3] = {1,0,2}; 
    int num = candy(rating, 3); 
    printf("Case 1 {1,0,2}. minimum number of candies I need to have is %d.\n", num);

    //case 2
    int rating2[3] = {1,2,2}; 
    int num2 = candy(rating2, 3); 
    printf("Case 2 {1,2,2}. minimum number of candies I need to have is %d.\n", num2);

    //case 3
    int rating3[5] = {1,3,4,5,2}; 
    int num3 = candy(rating3, 5); 
    printf("Case 3 {1,3,4,5,2}. minimum number of candies I need to have is %d.\n", num3);
    return 0; 
}

