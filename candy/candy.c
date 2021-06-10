#include <stdio.h>

void 
printArray(int arr[], int size){
    int i; 
    for(i=0; i<size; i++){
        printf("%d ", arr[i]); 
    }
    printf("\n"); 
}

int
addArrayNum(int arr[], int size){
    int sumOfArray = 0; 
    int i; 
    for(i=0; i<size; i++){
        sumOfArray = sumOfArray+arr[i]; 
    }
    return sumOfArray; 
}


int candy(int* ratings, int ratingsSize){
    int candies[ratingsSize]; 
    /*fill the array with all 1s*/
    int counter = 0; 
    for(counter = 0; counter<ratingsSize; counter++){
        candies[counter]=1; 
    }

    /*change the value from left to right*/
    for (counter = 1; counter<ratingsSize; counter++){
        if(ratings[counter]>ratings[counter-1]){
            candies[counter] = candies[counter-1]+1; 
        }
    }
    //printf("the left filling candy array\n");
    //printArray(candies, ratingsSize); 

    /*change the value from right to left*/
    for (counter = ratingsSize-2; counter>-1; counter--){
        //case [1, 3, 4, 5, 2]
        if(ratings[counter]>ratings[counter+1]&&candies[counter]<=candies[counter+1]){
            candies[counter] = candies[counter+1]+1; 
        }
    }
    //printf("the right filling candy array\n");
    //printArray(candies, ratingsSize); 

    return addArrayNum(candies, ratingsSize); 
}


















