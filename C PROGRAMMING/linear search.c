#include<stdio.h>
int main ()
{
	int e,s[100],i,n,tk;
	printf("number of elements in array:");
	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
		scanf("%d",&s[i]);
	}
	printf("enter the element to search:");
	scanf("%d",&e);
	for(i=0;i<5;i++)
	{
	if(e==s[i])
		{
		
		printf("element found");
		tk = 1;
	}
	else 
	{
	 ;
	}
	if (tk !=1)
	printf("element not found ");
	
	return 0;
	
}
}