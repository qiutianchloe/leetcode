CC=gcc
main:main.c findMinArrowShots.o
	$(CC) main.c findMinArrowShots.o -o main

findMinArrowShots.o: findMinArrowShots.c
	$(CC) -c findMinArrowShots.c

#clean command : make clean
clean: 
	rm *.o main