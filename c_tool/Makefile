CC=gcc
main:main.c useqsort.o
	$(CC) main.c useqsort.o -o main

useqsort.o: useqsort.c
	$(CC) -c useqsort.c

#clean command : make clean
clean: 
	rm *.o main