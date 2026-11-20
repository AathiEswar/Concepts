#include<stdio.h>

int main()
{
    int x1,x2,v1,v2,i=0,d1,d2,n = 1000;
    int count = 0;
    
    scanf("%d",&x1);
    scanf("%d",&v1);
    scanf("%d",&x2);
    scanf("%d",&v2);
    int d11 = x1;
    int d22 = x2;
    
    for(i = 0;i<n;i++)
    {
        d1 = d11+(v1*i);
        d2 = d22+(v2*i);
        if(d1== d2)
        {
            count = 0;
            break;
            
            }
            }

    
    if(count>0)
    {
        printf("NO");
    }
    else if(x1<x2 && v1<v2)
    {
        printf("NO");
    }
    else{
        printf("YES");
    }
            return 0;
    
    }
    
        