#include <stdio.h>
int main()
{
	int m1[50][50],r1,c1,i,j,k,r2,c2,m2[50][50],mat_res[50][50],mat_sub[50][50];
	printf("enter the no of rows and columns:");
	scanf("%d%d",&r1,&c1);
	for (i=0;i<r1;i++)
			{
		for(j=0;j<c1;j++)
		{
			scanf("%d",&m1[i][j]);
		}
	}
	printf("enter the no of rows and columns:");
	scanf("%d%d",&r2,&c2);
	for (i=0;i<r2;i++)
			{
		for(j=0;j<c2;j++)
		{
			scanf("%d",&m2[i][j]);
		}
	}
	if (c1==c2&&r1==r2)
	{
		for (i=0;i<r1;i++)
			{
		for(j=0;j<c2;j++)
		
		{
			mat_sub[i][j] = 0;
			mat_res[i][j]=0;
			{
			
			mat_res[i][j] = m1[i][j]+m2[i][j];
			
			mat_sub[i][j]=m1[i][j]-m2[i][j]; 
		}
	}
}
}
		else
	{
	
	printf("enter valid inputs");
}
	for (i=0;i<r1;i++)
	
			{
		for(j=0;j<c2;j++)
		
		{
			printf(" %d",mat_res[i][j]);
			
		}
		printf("\n");
	}
	for (i=0;i<r1;i++)
	
			{
		for(j=0;j<c2;j++)
		
		{
			printf(" %d",mat_sub[i][j]);
			
		}
		printf("\n");
	}
	return 0;
}								