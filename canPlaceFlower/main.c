#include <stdio.h>
#include <stdbool.h>
#include "canPlaceFlowers.h"

int main(){
    int flowerbed[7] = {1, 0, 0, 0, 0, 0, 1};

    bool value = canPlaceFlowers(flowerbed, 7, 2);
    return 0; 
}
