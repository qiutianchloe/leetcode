CC=gcc
main:main.c eraseOverlapIntervals.o
	$(CC) main.c eraseOverlapIntervals.o -o main

eraseOverlapIntervals.o: eraseOverlapIntervals.c
	$(CC) -c eraseOverlapIntervals.c

#clean command : make clean
clean: 
	rm *.o main