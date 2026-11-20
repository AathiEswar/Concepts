#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
	int  n2,n , i ;
	int *p;
	
	scanf("%d",&n);
	
	p = (int*)calloc(n,sizeof(int));
	
	if(p == NULL)
	{
	
		printf("memory not allocated");
		return(1);
	}
	printf("elements of the p");
	for(i = 0;i<n;i++)
	{
		scanf("%d\n",p+i);
	}
	for(i = 0;i<n;i++)
	{
		printf("%d\n",*(p+i));
	}
	
	printf("elements of the p2");
	
	scanf("%d\n",&n2);
	p = realloc(p,n2*sizeof(int));
	
	for(i = 0;i<n2;i++)
	{
		scanf("%d\n",p+i);
	}
	for(i = 0;i<n2;i++)
	{
		printf("%d\n",*(p+i));
	}
	
	free(p);
	
	return 0;
 } 