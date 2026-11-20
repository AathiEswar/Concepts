#include<stdio.h>
#include<math.h>
#include<stdlib.h>



int main()
{ 
	int n,i,j,k,m;

	
	int a[100][100] ;
	
	printf("enter number:");
	scanf("%d",&n);

		k = (n*2)- 1;
	printf("%d\n",k);
	
	m = k;
	
	for(i = 0;i<k;i++)
	{
		for(j = 0;j<k;j++)
		{
			a[i][j]=0;
		}
	}
	
	for(i = 0;i<k;i++)
	{
		for(j = 0;j<k;j++)
		{
			
			
				
				if(i==0 || j == 0 || i == k-1 || j == k-1)
				{
				
				a[i][j]= n;
				
				}
				while(a[i][j] == 0)
				{
					
					
				}
				
				
			
		}
	}
	
	
	
	for(i = 0;i<k;i++)
	{
		for(j = 0;j<k;j++)
		{
			printf("%d",a[i][j]);
		
		}
		printf("\n");
		
	}
	
	
    return 0;
}