#include<stdio.h>
#include<stdlib.h>

int mySqrt(int num){
    /*In case divide 0, we take the 0 out at the beginning of the program*/
    if (num == 0){return 0;}

    /*Then use the binary search to find the result in range of [1:a]*/ 
    int left = 1, right = num, mid, sqrt; 
    while(left<=right){
        mid = (int)(left + (right-left)/2); 
        sqrt = (int)(num / mid); 
        if(sqrt==mid){
            return sqrt; 
        }else if(mid>sqrt){
            right = mid-1; 
        }else{
            left = mid+1; 
        }
    }
    return right; 
}