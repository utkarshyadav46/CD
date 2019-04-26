%{
int count =0;
%}


%%
[0-9] {printf("%s is a digit \n",yytext);
	count++;}
.    {printf("%s in a non digit \n",yytext);}
\n   {return 0;}

%%

int yywrap(){}
int main()
{
yylex();
printf("Total number of non digit are  %d\n\n",count);
return 0;
}

