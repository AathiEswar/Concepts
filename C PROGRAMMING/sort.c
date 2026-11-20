#include<stdio.h>
void main()
{
	int a[50],n,i,s,d,b[50],c[50];
	
	 scanf("%d",&n);
	 
	for(i = 0;i<n;i++)
	{
		scanf("%d",&a[i]);
		
		}	
	for(d=0;d<n;d++)
	{
	
	for(i=0;i<n-d-1;i++)
	{
	
	if (a[i]> a[i+1])
	{
		s=a[i];
		a[i]=a[i+1];
		a[i+1]=s;
	}
	
	
}
}

for(i = 0;i<n;i++)
{
	b[i] = 0;
	c[i] = 0;
	if (i<n/2)
		{
			b[i] = a[i];
		}
		else
		{
			c[i] = a[i];
		}
	

}

for(i = 0;i<n;i++)
{
	if(b[i]==0 || c[i] == 0)
	{
		;
	}
	else
	{
	
	if (i%2 != 0)
	{
		printf("%d",b[i/2]);
	}
	else{
		
		printf("%d",c[i]);
	}
}}

}

	