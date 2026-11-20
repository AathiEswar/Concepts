#include<stdio.h>
#include<math.h>
int main()
{
	int a,b,x[1000][1000],y[1000][1000],z[1000][1000],q=0,w=0,e=0;
	long long int n,k;
	scanf("%d",&n);
	scanf("%d",&k);
	
	for(a= 1;a<=n;a++)
	{
		for(b = 1;b<n;b++)
		{
			if(a == b)
			{
				;
			}
			else
			{
			
			
			x[a][b] = a&b;
		}
		}
	}
		for(a= 1;a<=n;a++)
	{
		for(b = 1;b<n;b++)
		{
			if (x[a][b]> q&& x[a][b]<k)
			{
				q = x[a][b];
			}
			
		}
	}
	
	
	for(a= 1;a<=n;a++)
	{
		for(b = 1;b<n;b++)
		{
			if(a == b)
			{
				;
			}
			else
			{
			
			
			y[a][b] = a|b;
		}
		}
	}
		for(a= 1;a<=n;a++)
	{
		for(b = 1;b<n;b++)
		{
			if (y[a][b]> w && y[a][b]<k)
			{
				w = y[a][b];
			}
			
		}
	}
	
	
	for(a= 1;a<=n;a++)
	{
		for(b = 1;b<n;b++)
		{
			if(a == b)
			{
				;
			}
			else
			{
			
			
			z[a][b] = a^b;
		}
		}
	}
		for(a= 1;a<=n;a++)
	{
		for(b = 1;b<n;b++)
		{
			if (z[a][b]> e && z[a][b]<k)
			{
				e = z[a][b];
			}
			
		}
	}
	printf("%d\n",q);
	
	printf("%d\n",w);
	
	printf("%d",e);
	return 0;
}
