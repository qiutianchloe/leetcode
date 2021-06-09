/*if the header file happens to be included twice, the compiler will process its contents twice 
and it will result in an error. The standard way to prevent this is to enclose the entire real
contents of the file in a conditional*/
#ifndef EXAMPLE_H
//this construct is commonly known as a wrapper #ifdef. when the header is included again, the 
//conditional will be false, because the EXAMPLE_H is defined. the preprocessor will skip over the entire
//contents of the file, and the compiler wiil not see it twice.   
#define EXAMPLE_H
//the entire header file file

/*THREE TYPE DECLARATION*/

//function declaration 
int add(int, int);

//macro declaration
#define ADD(n1, n2) n1+n2; 

//typedef declaration
typedef struct{
    int age; 
    char *name 
}person; 


#endif