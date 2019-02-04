#include<stdio.h>
int main()
{
int j,k,l,m;
scanf("%d %d",&j,&k);
for(l=j;l<k;l++)
{
	int count=0;
	for(m=2;m<l;m++)
	{
	if(l%m==0)
	count++;
	}
	if(count==0)
	printf("%d ",l);
}
return 0;
}
