/*Roy and Alfi reside in two different cities, Roy in city A and Alfi in city B. Roy wishes to meet her in city B.

There are two trains available from city A to city B. Roy is on his way to station A (Railway station of city A). It will take T0 time (in minutes) for Roy to reach station A. The two trains departs in T1 and T2 minutes respectively. Average velocities (in km/hr) of trains are V1 and V2 respectively. We know the distance D (in km) between city A and city B. Roy wants to know the minimum time (in minutes) to reach city B, if he chooses train optimally.

If its not possible to reach city B, print "-1" instead (without quotes).

Note: If the minimum time is not integral, round the value to the least integer greater than minimum time.

Input:

First line will contain integer T, number of test cases.

Second line will contain integers **T0,T1,T2,V1,V2,D  ** (their meanings are mentioned in problem statement)

Output:

Print the integral result, minimum time (in minutes) to reach city B in a new line.

*/


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

