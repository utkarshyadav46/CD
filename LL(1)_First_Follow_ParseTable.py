#!/usr/bin/env python
# coding: utf-8

# In[61]:


import re #importing regular expression library
gra = []
lines = []
productions = []
LR = False
LF = False


# In[62]:


#opening file and reading lines of the file
with open("grammar1.txt","r") as f: 
    for _ in f.readlines():
        gra.append(_.split('\n')[0])

print("\n\tGrammar is in grammar1.txt file\n")
# In[63]:


#grabbing set of alphabets and terminals from the grammar
alphabets = set()
terminals = set()
start = gra[0][0]
end = gra[-1][0]
for line in gra:
    alphabets.update(re.findall('[A-Z]',line))
    terminals.update(re.findall('[a-z0-9*+()=]',line))


# In[64]:


alphabets


# In[65]:


terminals.add('$')
terminals


# In[66]:


#preprocessing the grammar
for line in gra:
    lines.append(re.split('[ /]',line))


# In[67]:


for line in lines:
    pro = line[0].split('->')[0]
    for _ in line:
        if line.index(_) == 0:
            productions.append([pro + '->' + line[0].split('->')[1]])
        else:
            productions.append([pro + '->' + _])


# In[68]:


#Getting grammar in the required data structure
for p in productions:
    productions[productions.index(p)] = p[0].split('->')


# In[69]:


productions1 = productions.copy()
productions


# In[70]:


#Detecting Left Recursion in the grammar
for p in productions:
    if ((p[0]==p[1][0]) and (p[0] in alphabets)):
        LR = True
        break


# In[71]:


LR


# In[72]:


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


# In[73]:


first(start)


# In[74]:


print("\n\n\t\tFirst Set\n\n",first_)


# In[75]:


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


# In[76]:


follow(start)


# In[77]:


print("\n\n\t\tFollow Set\n\n",follow_)


# In[78]:


#Parsing table
pt = {}
for a in alphabets:
    for t in terminals:
        pt[(a,t)] = set()


# In[79]:


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


# In[80]:


print("\n\n\t\tParse Table\n\n",pt)


# In[ ]:




