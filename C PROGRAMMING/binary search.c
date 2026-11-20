#include<stdio.h>
void main()
{
	
	int s[50],i,e,n,x,first ,mid, last;
	printf("enter the number of elements in array :");
	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
		scanf("%d",&s[i]);
	}
	printf("enter the element to search:");
	scanf("%d",&e);
	first = 0;
	last = n-1;
	while (first <=last)
	{
		mid = (first+last)/2;
		
	
	if (mid == e)
	{
		printf("element found");
		x = 1;
		break;
	}
	else if (mid >e)
	{
		last = mid-1;
	}
	else
	{
		first = mid+1; 
	}
}
    if (x==1)
    {
    	printf("");	}
    else 
    {
    	printf("element not found");
	}
	
	
	
}