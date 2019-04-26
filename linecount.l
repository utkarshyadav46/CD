%{
int line =0, character=0,word=0;
%}


%%
.    {character++;}
[\n]  {line++;}
\n\n {return 0;}
%%

int yywrap(){}
int main()
{
yylex();
printf("Total number of character are  %d\n",character);
printf("Total number of Lines and words are  %d\t%d\n\n",line+1,word);
return 0;
}

