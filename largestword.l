%{
#include<stdio.h>
int len=0;
%}


%%
[a-zA-Z]+ {
if(yyleng>len)
{
len=yyleng;
}
}
%%
yywrap(){}
int main(int argc[],char **argv[])
{
 yyin=fopen("input.txt","r");
 yylex(); 
 printf("largest: %d",len);
 printf("\n");
 return 0;
}

