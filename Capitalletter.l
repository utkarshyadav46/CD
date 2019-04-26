
%{
int count = 0;
%}

%%
[A-Z] {printf("%s Capital Letter\n ",yytext); 
	count++; }
.     { printf("%s Non Capital Letter\n ",yytext);}
\n    { return 0;}
%%
int yywrap(){}
int main()
{
yylex();
printf("No.of capital Letter - %d\n",count);
return 0;
}



