#include<bits/stdc++.h>
using namespace std;
int var=1,addr=100;
void fun(string str)
{
	int pos,l,i,j;
	
	if(str.find("if")!=-1 || str.find("else if")!=-1 || str.find("else")!=-1)
	{
			cout<<addr<<"\t"<<str<<"goto"<<addr+3<<endl;
			addr++;
			cout<<addr<<"\tfalse"<<endl;
			addr++;
			cout<<addr<<"\tgoto"<<addr+2<<endl;
			addr++;
			cout<<addr<<"\tfalse"<<endl;
			addr++;
	}
	
	else if(str.find("=")!=-1 && str.find("+")==-1 &&  str.find("-")==-1 &&  str.find("*")==-1  &&  str.find("/")==-1) 
	{
		pos=str.find("=");
		string sub=str.substr(pos+1,(str.length())-2-pos);
		cout<<"t_"<<var<<"="<<sub<<endl;
		sub=str.substr(0,pos);
		cout<<sub<<"="<<"t_"<<var++<<endl;
	}
	else
	{
	   string exp=str,exp1="";
	   char power=exp[0];
	   //cout<<"power"<<power<<endl;
	   l=exp.length();
	   pos=str.find("=");
	   for(i=pos+1;i<l;i++)
	   {
	   	
	   	if(exp[i]=='+' || exp[i]=='-')
	   	{
	   		if(exp[i+2]=='/' || exp[i+2]=='*')
	   		{
	   			reverse(exp.begin()+2,exp.end());
	   			j=l-i-1;
	   			exp1=exp1+exp.substr(pos+1,j);
	   			reverse(exp1.begin(),exp1.end());
	   			cout<<"t_"<<var<<"="<<exp1<<endl;
	   			cout<<"t_"<<++var<<"="<<exp[j+pos+2]<<exp[j+pos+1]<<"t_"<<var<<endl;
	   			break;
	   				
	   		}
	   		else
	   		{
	   		//	cout<<"substring "<<exp.substr(pos+1,i-1)<<endl;
	   			exp1=exp1+exp.substr(pos+1,i);
	   		//	cout<<"dddddddd"<<exp1<<endl<<endl;
	   			cout<<"t_"<<var<<"="<<exp1<<endl;
	   			cout<<"t_"<<++var<<"="<<"t_"<<var<<exp[i+2]<<exp[i+3]<<endl;
	   			break;
	   		}
	   }
	   else if(exp[i]=='/'||exp[i]=='*')
		{
			exp1=exp1+exp.substr(pos+1,i);
	   			cout<<"t_"<<var<<"="<<exp1<<endl;
	   			cout<<"t_"<<++var<<"="<<"t_"<<var<<exp[i+2]<<exp[i+3]<<endl;
	   			
			break;
		}
	   
	}

cout<<str[0]<<"="<<"t_"<<var++<<endl;


}
}






int main()
{
	ifstream fp("input.txt");
	string str;
	cout<<"\nThe Code in the 3 Address Code Form Will look like This:\n";
	while(getline(fp,str))
	{
		if(str.find("#")!=-1 || str.find("{")!=-1 || str.find("}")!=-1 || str.find("using")!=-1 || str.find("return")!=-1 || str.find("main()")!=-1 || str.find("printf")!=-1 || str.find("scanf")!=-1 || str.find("//")!=-1 || (str.find("int")!=-1 && str.find("=")==-1)) 
		continue;
		else if(str.find("/*")!=-1)
		{
			while(getline(fp,str))
			{
				if(str.find("*/")!=-1)
				break;
			
			}
		
		}
		else
		fun(str);
	}
	fp.close();

}
