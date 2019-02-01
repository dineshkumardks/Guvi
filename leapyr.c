#include <stdio.h>
#include<Conio.h>
int main()
{
 int leap;
 scanf("%d",&leap);
 if((leap%4==0 && year%100!=0) || year%400==0)
	{
		printf("yes");
	}
	else
	{
		printf("no");
	}
 
		return 0;
}
