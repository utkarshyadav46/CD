%{
#include<stdio.h>
int count=0
%}



%%
[aeiou] { printf("%s is a vowel\n",yytext);
	count++;}

"\n" {return 0;}

%%


int yywrap(){}
int main()
{
yylex();
printf("\n%d Total number of vowels are :",count);
return 0;

}
