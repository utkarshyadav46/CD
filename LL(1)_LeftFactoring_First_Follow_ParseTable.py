#!/usr/bin/env python
# coding: utf-8

# In[126]:


import re #importing regular expression library
gra = []
lines = []
productions = []
LR = False
LF = False


# In[127]:


#opening file and reading lines of the file
with open("grammar.txt","r") as f: 
    for _ in f.readlines():
        gra.append(_.split('\n')[0])
gra

print("\n\tGrammar is in grammar.txt file\n")
# In[128]:


#grabbing set of alphabets and terminals from the grammar
alphabets = set()
terminals = set()
start = gra[0][0]
end = gra[-1][0]
for line in gra:
    alphabets.update(re.findall('[A-Z]',line))
    terminals.update(re.findall('[a-z0-9*+()=]',line))


# In[129]:


alphabets


# In[130]:


terminals.add('$')
terminals


# In[131]:


#Collection of available substitute variables if required
all_alpha = set(re.findall('[A-Z]','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
all_alpha = all_alpha - alphabets


# In[132]:


#preprocessing the grammar
for line in gra:
    lines.append(re.split('[ /]',line))
lines


# In[133]:


for line in lines:
    pro = line[0].split('->')[0]
    for _ in line:
        if line.index(_) == 0:
            productions.append([pro + '->' + line[0].split('->')[1]])
        else:
            productions.append([pro + '->' + _])


# In[134]:


#Getting grammar in the required data structure
for p in productions:
    productions[productions.index(p)] = p[0].split('->')


# In[135]:


productions1 = productions.copy()
productions


# In[136]:


#Detecting Left Recursion in the grammar
for p in productions:
    if ((p[0]==p[1][0]) and (p[0] in alphabets)):
        LR = True
        break


# In[137]:


LR


# In[138]:


#Solving for Left factoring
for a in alphabets: #for all alphabets
    m = -1         #getting max length RHS production of a particular variable
    for p in productions:
        if p[0]==a and len(p[1])>m:
            m = len(p[1])
            com = p[1]
    
    rhs = []  #Maintaing RHS list
    comman = set()
    for p in productions:
        if p[0]==a:
            rhs.append(p[1])
    
    while m>0:  #finding set of comman prefix substrings
        for r1 in rhs:
            substr = r1[:m-1]
            for r2 in rhs:
                if substr in r2:
                    comman.add(substr)
        m = m -1
    comman.remove('') #Removing null in that comman set of strings

    if bool(comman): #If comman elements exists except NULL then only we process for Left Factoring
        m=-1
        for i in comman:
            if len(i)>m:
                m = len(i)
                c = i
        for r in rhs: #Removing productions that doesn't contain substring as prefix
            if c not in r:
                del rhs[rhs.index(r)] 

        imp = []
        for r in rhs: 
            if c!='': #if comman element  is not null
                for _ in r.split(c):
                    if len(_)!=0:   #length not zero after split then only append
                        imp.append(_)

        var = list(all_alpha)[0] #Grabbing an extra variable from the set
        all_alpha = all_alpha - set(var)
        pro = []
        pro.append([a,c+var])
        for i in imp:       #Generating the required productions
            pro.append([var,i])

        n = len(productions)
        while n>0 and bool(productions1): #Deleting the unnecessary productions
            for p in productions1:
                if p[0]==a and p[1] in rhs:
                    del productions1[productions1.index(p)]
                    break
            n = n - 1
        productions1.extend(pro)


# In[139]:


for p in productions1:
    if p[0] not in alphabets:
        alphabets.add(p[0])


# In[140]:


productions = productions1


# In[141]:

print("\n\t\tAfter Left Factoring\n\n")
print("\n\n\t\tAlphabets in Grammar\n\n",alphabets)
print("\n\n\t\tTerminals in Grammar\n\n",terminals)
print("\n\n\t\tProductions after Left Factoring in Grammar\n\n",productions)


# In[142]:


#Finding First Set
first_ = {} #First set
def first(st):
    try:
        first_[st] = set() #creating an empty set for all the incoming alphabets
        for p in productions:
            if p[0]==st and (p[1][0] in terminals): #If found terminal adding to set
                first_[st].add(p[1][0])
            elif p[0]==st and (p[1][0] in alphabets):#If found alphabet calling its first again and collecting its first set
                first(p[1][0])
                first_[st] = first_[st].union(first_[p[1][0]])
        for a in alphabets: #for all the alphabets remained
            if a not in first_:
                first(a)
    except RecursionError:
        pass


# In[143]:


first(start)


# In[144]:


print("\n\n\t\tFirst Set\n\n",first_)


# In[145]:


#Finding Follow Set
follow_ = {}

for a in alphabets:
    follow_[a] = set() #creating an empty set for all the incoming alphabets

def follow(st):
    try:
        if st==start:
            follow_[st].add('$') #appending $ to start alphabet

        for p in productions:
            if st in p[1]:
                if p[1][-1] == st: #if found at last appending follow set of the LHS variable
                    follow_[st] = follow_[st].union(follow_[p[0]])
                else:
                    if (p[1][p[1].index(st)+1] in terminals): #if found terminal appending to list
                        follow_[st].add(p[1][p[1].index(st)+1])
                    if (p[1][p[1].index(st)+1] in alphabets): #if found terminal appending first set of it
                        follow_[st] = follow_[st].union(first_[p[1][p[1].index(st)+1]])
        for a in alphabets: #Calling alphabets that are not yet called
            if len(follow_[a])==0:
                follow(a)
    except RecursionError:
        pass


# In[146]:


follow(start)


# In[147]:


print("\n\n\t\tFollow Set\n\n",follow_)



# In[148]:


#Parsing table
pt = {}
for a in alphabets:
    for t in terminals:
        pt[(a,t)] = set()


# In[149]:


possible = True
for p in productions:
    if p[1][0] in terminals:
        if len(pt[(p[0],p[1][0])])==0:
            pt[(p[0],p[1][0])] = p[0]+' -> '+p[1]
        else:
            possible = False
            #print("LL1 parser can't be constructed for this Grammar")
    elif p[1][0] in alphabets:
        for i in first_[p[1][0]]:
            if len(pt[(p[0],i)])==0:
                pt[(p[0],i)] = p[0]+' -> '+p[1]
            else:
                possible = False
                #print("LL1 parser can't be constructed for this Grammar")
if not possible:
    print("LL1 parser can't be constructed for this Grammar")


# In[150]:


print("\n\n\t\tParse Table\n\n",pt)



# In[ ]:




