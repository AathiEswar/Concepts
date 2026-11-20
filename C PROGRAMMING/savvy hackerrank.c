#include<stdio.h>

int main()

{
	int a= 3 , b = 4,i,sum = 0,*avg;
	int *ptr1 ,*ptr2;
	ptr1 = &a;
	ptr2 = &b;
	
	
	avg = *ptr1 + *ptr2;

	printf("%d",avg);
	return 0;
	
}