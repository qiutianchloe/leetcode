CC=gcc
main:main.c findContentChildren.o
	$(CC) main.c findContentChildren.o -o main

findContentChildren.o: findContentChildren.c
	$(CC) -c findContentChildren.c

#clean command : make clean
clean: 
	rm *.o main