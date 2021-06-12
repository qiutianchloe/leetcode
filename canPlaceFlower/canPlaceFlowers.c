#include <stdbool.h>
#include <stdio.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    int i; 
    int canplace = 0; 
    for(i = 0; i<flowerbedSize; i++){
        //current positition is empty
        if(flowerbed[i]==0){
            //make sure that the left side of the position is empty
            if(i==0||flowerbed[i-1]==0){
                //make sure that the right side of the postion is empty
                if(i==flowerbedSize-1||flowerbed[i+1]==0){
                    flowerbed[i] = 1; 
                    canplace++; 
                }
            }
        }
    }
    if(canplace<n){
        return false; 
    }else{
        return true; 
    }
}