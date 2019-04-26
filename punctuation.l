%{
int punc=0;
%}


%%
[,-.?!;:"'/~]    {punc++;}  
\n 		{return 0;}
%%

int yywrap(){}
int main()
{
yylex();
printf("\nTotal number of punctuation are  %d\n",punc);
return 0;
}

