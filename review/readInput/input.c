#include <stdio.h>

int main(int argc, char* argv[]){
    int counter;
    printf("name of the program is: %s", argv[0]); 
    if(argc==1){
        printf("\n there is no extra command line argument passed other than program name. "); 
    }
    if(argc>=2){
        printf("\n Number of argument passed, %d", argc); 
        printf("\n Following are the command line argument passed: "); 
        for(counter=0; counter<argc; counter++){
            printf("\n argv[%d]: %s", counter, argv[counter]); 
        }
    }

    int scanned_val;
    printf("\ntype some integer. \n");  
    scanf("%d", &scanned_val); //there should have no \n or anyother character here 
    printf("this is the value you type in %d\n", scanned_val);
    return 0 ; 
}