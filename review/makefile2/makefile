#gcc -o main main.c sep.c
#start from back, which is the file include main() function
CC=gcc
main:main.c sep.o 
	$(CC) main.c sep.o -o main

sep.o: sep.c
	$(CC) -c sep.c

#clean command : make clean
clean: 
	rm *.o main