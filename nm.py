#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(0,5):
    print(i)
    for j in range(0,5):
        print("*")


# In[ ]:


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print('')


# In[ ]:


for i in range(0,5):
    for j in range(0,i+1):
        print(j,end="")
    print('')


# In[ ]:


i=1
while (i<10):
    print(i)
    i=i+1
   
        


# In[ ]:


i=1
while (i<10):
    if(i==6):
        break
    print(i)
    i=i+1


# In[ ]:


i=1
while (i<10):
    if(i==6):
        i=i+1
        continue
    else:
         print(i)
    


# In[ ]:





# In[ ]:





# In[ ]:


i=1
while (i<10):
    if(i==6):
        i=i+1
        continue
    else:
        print(i)  
        i=i+1


# In[ ]:


a=0
if(a>5):
print(a)


# In[ ]:


a=0
if(a>5):
    pass
print(a)


# In[ ]:


import random
u=0
s=0
x=0
while(x<=5):
    a=["stone","paper","scissor"]
    system=random.choice(a)
    user=input("select stone or paper or scissor")
    print(system)
    print(user)
    if system=="stone" and user=="paper":
        print("user win")
        u=u+1
        print(u)
    elif system=="stone" and user=="scissor":
        print("system win")
        s=s+1
        print(s)
    elif system=="paper" and user=="scissor":
        print("user win")
        u=u+1
        print(u)
    elif system=="paper" and user=="stone":
        print("system win")
        s=s+1
        print(s)
    elif system=="scissor" and user=="stone":
        print("user win")
        u=u+1
        print(u)
        
    elif system=="scissor" and user=="paper":
        print("system win")
        s=s+1
        print(s)
    elif user==system:
         print("draw")
    else:
        print("invalued")
    x=x+1   
    print("total point for user is",u)
    print("total point for system is ",s)


# In[ ]:


s=1
a=int(input("enter the number"))
for i in range(1,a+1):
    s=s*i
print(s)


# In[2]:


num=int(input("enter a number"))
fact=1
a=1
while(a<=num):
    fact=fact*a
    a+=1
print("fact of",num,"is",fact)
    


# In[3]:


a=0
b=1
c=0
num=int(input("enter a number:"))
print(a)
print(b)
while(0<num-2):
    c=a+b
    print(c)
    a=b
    b=c
    num=num-1
   


# In[11]:


a=1
while(True):
    if a==10:
        break
    print(a)
    a=a+1


# In[17]:


def sum():
    a=10
    b=20
    print(a+b)
sum()


# 

# In[19]:


def sub(a,b):
    x=a
    y=b
    print(x-y)


# In[20]:


sub(20,30)


# In[21]:


def sub(a,b):
    x=a
    y=b
    c=x-y
    return(c)


# In[22]:


z=sub(30,20)
print(z)


# In[43]:


def div(a,b):
    x=a
    y=b

    c=x/y
    return(c)   
    
def sub(a,b):
    x=a
    y=b
    c=x-y
     return(c)   
    


# In[44]:


z=div(10,2)
print(z)


# In[39]:


def add(a,b):
    x=a
    y=b
    c=x+y
    return(c)   
    
def multi(a,b):
    x=a
    y=b
    c=x*y
    return(c) 


# In[40]:


z=multi(1,3)
print(z)


# In[45]:


z=sub(10,2)
print(z)


# In[46]:


z=add(10,2)
print(z)


# In[58]:


def fact():
    s=1
    a=int(input("enter the number"))
    for i in range(1,a+1):
        s=s*i
    return(s)


# In[59]:


f=fact()
print(f)


# In[84]:


a=int(input("enter the number"))
def month(num):
    if num==1:
        print("jan")
    elif num==2:
        print("feb")
    elif num==3:
        print("march")
    elif num==4:
        print("apr")
    elif num==5:
        print("may")
    elif num==6:
        print("june")
    elif num==7:
        print("july")
    elif num==8:
        print("agu")
    elif num==9:
        print("sept")
    elif num==10:
        print("oct")
    elif num==11:
        print("nov")
    elif num==12:
        print("dec")
    else:
        print("invalued option")
month(a)


# In[85]:


import datetime
x=datetime.datetime.now()
print(x)


# In[97]:


def prime(a):
    i=1
    count=0
    for i in range(1,a):
        if a%i==0:
            count=count+1
    if count<2:
        print("number" ,a,"is prime")
    else:
        print("number",a, "is not a prime")


# In[98]:


prime(5)


# In[ ]:




