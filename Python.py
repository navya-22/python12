#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=10
b=30

a+b


# In[3]:


x='hello goodmorning'
x


# In[4]:


a=10
b=20
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


# In[5]:


a=input("enter the first number")
b=input("enter the second number")
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


# In[6]:


a=int(input("enter the first number"))
b=int(input("enter the second number"))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


# In[8]:


a=int(input("enter a number for a:"))
if a%2==0:
    print("a is an even number")
else:
 print("a is an odd number")


# In[16]:


a=int(input("total amount:"))
if a>2500:
    print("you have discount of 10%")
    d=(a*10)/100
    print("discounted amount is",d)
    print("your bill amount is:",a-d)
else:
    print ("no discount")
    


# In[18]:


a=int(input("enter  the number:"))
if a>0:
    print("it is an positive number ")
else:
    print("it is an negative number")


# In[19]:


a=int(input("enter  the number:"))
if a>0:
    print("it is an positive number ")
elif a==0:
    print("it is neither positive nor negative")
else:
    print("it is an negative number")


# In[29]:


a=int(input("enter 1st value:"))
b=int(input("enter 2nd value: "))
c=input("enter a operator(+,-,*,/,%):")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
else:
 print("not an valued operator")


# In[30]:


a=int(input("enter 1st value:"))
b=int(input("enter 2nd value: "))
c=int(input("enter 3rd value:"))
if a>b & a>c:
    print("a is the largest value")
elif b>a & b>c:
    print("b is the largest value")
else :
    print("c is the largest value")
    


# In[36]:


import random
num=random.random()
num


# In[39]:


a=[10,20,30]

x=random.choice(a)
x


# In[44]:


a=["stone","paper","scissor"]
system=random.choice(a)
user=input("select stone or paper or scissor")
print(system)
print(user)
if system=="stone"  and user=="paper":
    print("user win")
elif system=="stone"  and user=="scissor":
    print("system win")
elif system=="paper" and user=="stone":
    print("system win")
elif system=="paper" and  user==" scissor":
    print("user win")
elif system=="scissor"  and user=="paper":
    print("system win")
elif system=="scissor" and user=="stone":
    print("uer win")
else:
    print("drow")
    


# In[56]:


a=int(input("enter 1st value:"))
b=int(input("enter 2nd value: "))
c=int(input("enter 3rd value:"))

if a>b:
        if a>c:
            print(a," is the largest")
        else :
            print(c," is the largest")
elif c>b :
    print (c," is the largest")
else :
    print(b," is the largest")


# In[57]:


for i in range(0,10):
    print(i)


# In[59]:


a=0
for i in range(0,10):

    a=a+i
print(a)


# In[61]:


for i in range(0,10):
    if i%2==0:
        print(i)


# In[62]:


for i in range(0,10):
    if i%2==1:
        print(i)


# In[63]:


for i in range(0,50,5):
    print(i)


# In[66]:


s=1
a=int(input("enter the number"))
for i in range(1,a+1):
    s=s*i
print(s)


# In[70]:


a= int(input("enter a number:"))
b=int(input("enter the limit:"))
for i in range(1,b+1):
    
    print(i,"*",a,"=",a*i)
    


# In[83]:


a=["depu","luttu","sinu","sana","thashi"]
for i in a:
    print(i)


# In[77]:


a=["depu","luttu","sinu","sana","thashi"]
print(len(a))


# In[78]:


a=["depu","luttu","sinu","sana","thashi","amal","hrithic","aseem","faheem","abhay"]
s=len(a)
for i in range(0,s):
    print(a[i])
    


# In[81]:


a=0
b=1
c=0
print(a)
print(b)
for i in range(0,10):
    c=a+b
    print(c)
    a=b
    b=c


# In[ ]:




