#include<stdio.h>
#include<string.h>


int main()
{
	char a[200],b[100];
	int i,j;
	printf("enter a string:");
	gets(a);
	 for(i = 0;a[i] != '\0';i++)
	 {
	 	;
	 }
	 
	
	printf("enter a string:");
	gets(b);
	 for(j = 0;b[j] != '\0';j++,i++)
	 {
	 	a[i] = b[j];
	 }
	 
	printf("output:%s",a);
	
 return 0;
	
}