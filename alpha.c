#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
char alp;
printf("\nEnter any alphabat...");
scanf("%c",&alp);
if( (alp>='a' && alp<='z') || (alp>='A' && alp<='Z'))
{
        printf("%c is an alphabet.",alp);
    else
        printf("%c is not an alphabet.",alp)
}
getch();
}
