CC=gcc
main:main.c canPlaceFlowers.o
	$(CC) main.c canPlaceFlowers.o -o main

canPlaceFlowers.o: canPlaceFlowers.c
	$(CC) -c canPlaceFlowers.c

#clean command : make clean
clean: 
	rm *.o main