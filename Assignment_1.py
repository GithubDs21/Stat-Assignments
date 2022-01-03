#!/usr/bin/env python
# coding: utf-8
# Question 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
              between 2000 and 3200 (both included). The numbers obtained should be printed
              in a comma-separated sequence on a single line.
# In[1]:


al=[]
for x in range(2000, 3201):
    if (x%7==0) and (x*5!=0):
        al.append(str(x))
print (','.join(al))


# In[ ]:




# Question 2:  Write a Python program to accept the user's first and last name and then getting them printed 
               in the the reverse order with a space between first name and last name
# In[2]:


fn="Suryakant"
ln="Mhaske"
print(ln+" "+fn)


# In[ ]:





# In[ ]:




# Question 3: Write a Python program to find the volume of a sphere with diameter 12 cm.
              Formula: V=4/3 * π * r3
# In[3]:


pi=22/7
r=12.0
V=4.0/3.0*22/7*(12**3)


# In[5]:


print('volume of the sphere: ',V)


# In[ ]:




