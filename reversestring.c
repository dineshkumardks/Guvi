#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
   char bec[100];
    clrscr();
   printf("Enter a string to reverse\n");
   gets(bec);
   strrev(bec);
   printf("Reverse of the string is \n%s\n", bec);
   getch();
   }
