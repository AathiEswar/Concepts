#include<stdio.h>
void main ()
{
	int s[50],i,e,n,index,c;
	printf("enter the number of elements in array :");
	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
		scanf("%d",&s[i]);
	}
	printf("enter the element to search:");
	scanf("%d",&e);
	for (i=0;i<n;i++)
	{
		if(e==s[i])
		{
		
		printf("element found");
		break;
	}
	}
	}
	
