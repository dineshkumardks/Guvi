#include<stdio.h>
#include<conio.h>
int main()
{
int num;
scanf("%d",&num);
if(num>0)
{
printf(" positive");
}
else if(num<0)
{
printf("negative");
}
else
{
printf("The num is equal to 0");
}
return 0;
}
