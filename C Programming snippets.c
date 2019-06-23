#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<time.h>

int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}

/*PRINT TACTICS*/

//print float with specified accuracy
printf("%.2f",floatvar);		// prints 2 decimal places

printf("%.0f"floatvar);			//prints 0 decimal places



/*DYNAMIC MEMORY ALLOCATION*/

// single memory allocation of size*n block 
int* ptr;
ptr = (int*) malloc(100 * sizeof(int));

//check if memory allocated
if (ptr == NULL) 
{ 
	printf("Memory not allocated.\n"); 
	exit(0); 
}

// continuos memory allocation of n blocks of int size
ptr = (int*)calloc(n, sizeof(int));		//memory is initialised to 0 for each int block

// frees memory allocated associated with the pointer
free(ptr);

// reallocates new memory space with inceased size
ptr = realloc(ptr, n * sizeof(int)); 