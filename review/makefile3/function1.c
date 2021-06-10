#include <stdio.h>
#include "function2.h"


void function1(int num){
    printf("This is function 1, the parameter is %d\n", num);
    //run function2
    function2(2); 
}