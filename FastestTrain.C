#include <stdio.h>
#include <math.h>

int main(){
	int k,t,t0,t1,t2,v1,v2,d;
	float s1,s2;
	scanf("%d", &t);
	for(k=0;k<t;k++)
	{
	    scanf("%d%d%d%d%d%d",&t0,&t1,&t2,&v1,&v2,&d);
	   //printf("%d%d%d%d%d%d",t0,t1,t2,v1,v2,d);
	    if(t0>t1||t0>t2)
	    {
	        printf("-1");
	        continue;
	    }
	    s1=(float)d/(float)v1;
	    s2=(float)d/(float)v2;
	    s1=s1*60+t1;
	    s2=s2*60+t2;
	    //printf("%f %f",s1,s2);
	    if(s1<s2)
	    {
	        printf("%.0f",ceil(s1));
	    }
	    else
	    {
	        printf("%.0f",ceil(s2));
	    }
	}
	
	
}

