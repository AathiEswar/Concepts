#include<stdio.h>
int main()
{
	int c,k,i,n,t,a;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&n,&k);
		c=0;
		for(i = 0;i<n;i++)
		{
			scanf("%d",&a);
			if(a<=0)
			{
				c++;
			}
		}
			if(c<k)
			{
				printf("YES");
			}
			else
			{
				printf("NO");
			}
			printf("\n");
		}

	return 0;
}