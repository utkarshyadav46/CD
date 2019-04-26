

%{
int vowel =0, character=0,word=0;
%}


%%
[aeiou]    {vowel++;}  
\n {return 0;}
%%

int yywrap(){}
int main()
{
yylex();
printf("Total number of vowels are  %d\n",vowel);
return 0;
}

