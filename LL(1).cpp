#include<stdio.h>
#include<ctype.h>
#include<iostream>
#include<fstream>
#inlcude"parser.cpp"
using namespace std;
char a[8][8];

struct firstable
{
    int n;
    char firT[5];
};

struct followtable
{
    int n;
    char folT[5];
};

struct followtable follow[5];

struct firstable first[5];

int col;
void findFirst(char,char);
void findFollow(char,char);
void followtable(char,char);
void firstable(char,char);

	int n;
int main()
{

	ifstream input;
	input.open("infirst.txt",ios::app);
	input>>n;
	cout<<n;
    int i,j,c=0,cnt=0;
    char ip;
    char b[8]; 
    printf("\n\t\t LL[1] parser \nFIRST AND FOLLOW SET in file are:\n");
    for(i=0;i<8;i++)
    {
    	input>>a[i];
    	//cout<<a[i]<<endl;
    }
    input.close();
    ofstream out;
	out.open("outfirst.txt",ios::app);
	for(i=0;i<n;i++)
    {   c=0;
    for(j=0;j<i+1;j++)
    {
        if(a[i][0] == b[j])
        {
            c=1;    
            break;
        }    
    }
    if(c !=1)
    {
      b[cnt] = a[i][0];
      cnt++;
    }               

    }
     printf("\n");
     out<<endl;

    for(i=0;i<cnt;i++)
    {   
	col=1;
    first[i].firT[0] = b[i];
    first[i].n=0;
    findFirst(b[i],i);
    }
    for(i=0;i<cnt;i++)
    {
    col=1;
    follow[i].folT[0] = b[i];
    follow[i].n=0;
    findFollow(b[i],i);
     }

    printf("\n");
    out<<endl;
   for(i=0;i<cnt;i++)
   {
    for(j=0;j<=first[i].n;j++)
    {
            if(j==0)
            {
                printf("First(%c) : {",first[i].firT[j]);
                out<<"First "<<first[i].firT[j]<<" :{ ";
            }
            else
            {   
            out<<first[i].firT[j]<<" ";
                printf(" %c",first[i].firT[j]);
            }
    }
    printf(" } ");
    out<<" } ";
    printf("\n");
    out<<endl;
    } 
     printf("\n");
     out<<endl;
   for(i=0;i<cnt;i++)
   {
    for(j=0;j<=follow[i].n;j++)
    {
            if(j==0)
            {
                printf("Follow(%c) : {",follow[i].folT[j]);
                out<<"Follow "<<follow[i].folT[j]<<": {";
            }
            else
            {   
                printf(" %c",follow[i].folT[j]);
                out<<" "<<follow[i].folT[j];
            }
    }
    printf(" } ");
out<<"}\n";
    printf("\n");
    } 
  
  
  }
void parser()
{
	for(int i=0;i<n;i++)
	{
		
	}
}
void findFirst(char ip,char pos)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(ip == a[i][0])
        {
            if(isupper(a[i][3]))
            {
                findFirst(a[i][3],pos);
            }
            else
        {

        first[pos].firT[col]=a[i][3];
        first[pos].n++;
        col++;
            }
        }
    }
}
void findFollow(char ip,char row)
{   int i,j;
    if(row==0 && col==1)
    {
        follow[row].folT[col]= '$';
        col++;
        follow[row].n++;
    }
    for(i=0;i<n;i++)
    {
        for(j=3;j<n-1;j++)
        {
            if(a[i][j] == ip)
            {
                if(a[i][j+1] == '\0')
                {
                    if(a[i][j] != a[i][0])
                    {
                        followtable(a[i][0],row);
                    }
                }
                else if(isupper(a[i][j+1]))
                {   if(a[i][j+1] != a[i][0])
                    {
                        firstable(a[i][j+1],row);                                     

                }
                }
                else
                {
                    follow[row].folT[col] = a[i][j+1];  
                    col++;
                    follow[row].n++;            


                }   
            }
        }
    }   
}
void followtable(char ip,char row)
{   int i,j;
    for(i=0;i<5;i++)
    {
        if(ip == follow[i].folT[0])
        {
            for(j=1;j<=follow[i].n;j++)
            {
                follow[row].folT[col] = follow[i].folT[j];
                col++;
                follow[row].n++;
            }
        }
    }   
}
void firstable(char ip,char row)
{   
        int i,j;
    for(i=0;i<5;i++)
    {
        if(ip == first[i].firT[0])
        {
            for(j=1;j<=first[i].n;j++)
            {
                if(first[i].firT[j] != '0')
                {
                    follow[row].folT[col] = first[i].firT[j];
                    follow[row].n++;
                    col++;                  
                }
                else
                {
                    followtable(ip,row);
                }
            }
        }
    }

}


