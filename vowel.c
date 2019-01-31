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
switch(alp)
{
case 'a':printf("\nVowel");
break;
case 'e':printf("\nVowel");
break;
case 'i':printf("\nVowel");
break;
case 'o':printf("\nVowel");
break;
case 'u':printf("\nVowel");
break;
case 'A':printf("\nVowel");
break;
case 'E':printf("\nVowel");
break;
case 'I':printf("\nVowel");
break;
case 'O':printf("\nVowel");
break;
case 'U':printf("\nVowel");
break;
default:printf("\nIt is  a consonant");
}
getch();
}
