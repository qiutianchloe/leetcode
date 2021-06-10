CC=gcc
main:main.c function1.o function2.o
	$(CC) main.c function1.o function2.o -o main

function1.o: function1.c
	$(CC) -c function1.c 

function2.o: function2.c
	$(CC) -c function2.c 

#clean command : make clean
clean: 
	rm *.o main