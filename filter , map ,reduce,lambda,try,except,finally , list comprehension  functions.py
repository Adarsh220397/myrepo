#!/usr/bin/env python
# coding: utf-8

# In[7]:


#reduce

list_1=["adarsh","virat","sachin","anil"]

from functools import reduce
map_obj = reduce (lambda x,y: x + " plays after " + y ,list_1) #x,y - two iterations
print(map_obj)


# In[8]:


list_1=["adarsh","virat","sachin","anil"]

from functools import reduce
map_obj = reduce (lambda x,y,z: x + " plays after " + y +" hell no ",list_1) #x,y,z - 3 iterations cannot be done
print(map_obj


# In[ ]:


# lambda function -- annonymous function in python -- no name to define it

lambda a :



# In[30]:


def add_name(x,y):
    return x-y


# In[29]:


(lambda x,y : x-y)(12,43) #lambda funct is defined


# In[31]:


add_name(3,4)


# In[34]:


a=int(input())
b=int(input())
c=int(input())
(lambda x,y,z : z+x+y)(a,b,c)


# In[37]:


x = lambda a,b:a*b
print("Multi =",x(5,2))


# In[ ]:


# lambda inside a function as an argument

def table(n):
    return lambda a:a*n

n = int(input("Enter the no :"))
b = table(n)

#for i in range (1,5):
print(i,b(i))

table(6)


# In[46]:


lst = (10,20,30,40,50,60)  
square_list = list(map(lambda x:x**2,lst)) # the tuple contains all the items of the list for which the lambda function evaluates to true    
print(square_list)  


# In[3]:


lst = (10,22,37,41,100,123,29)  
oddlist = tuple(filter(lambda x:(x%2 != 0),lst)) # the tuple contains all the items of the tuple for which the lambda function evaluates to true    
print(oddlist)    


# In[19]:


#try,except,finally


a = 4
b = 0
# No exception Exception raised in try block
try:
    k = a//b # raises divide by zero exception.
    print(k)

finally:
         print("this is always ")


# In[15]:



# initializing number
a = 4
b = 0
  
# No exception Exception raised in try block
try:
    k = a//b # raises divide by zero exception.
    print(k)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")


# In[23]:



#assert
a=3
b=9
print ("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print (a / b)


# In[27]:


# del funct

a = 3
b = 6

print(a)
print(b)
  # check for a,b's existance
del a
del b

print(a)
print(b)
 # check again


# In[29]:



# global variable
a = 15
b = 10
  
# function to perform addition
def add():
    c = a + b
    print(c)
  
# calling a function
add()

add()
  


# In[8]:


# nonlocal keyword
def fun():
    var1 = 10
  
    def gun():
        # tell python explicitly that it
        # has to access var1 initialized
        # in fun on line 2
        # using the keyword nonlocal
        nonlocal var1
          
        var1 = var1 + 10
        print(var1)

    gun()


fun()


# In[10]:


j =1 
while(j<=5):
    j=j+1 
    print(j)


# In[12]:


j =1 
while(j<=3):
    j=j+1
print(j)


# 
# #### x, y, z = input("Enter a three value: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
# print()
# 

# In[14]:


x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()


# In[18]:


y= input().split()
print(x)
print(y)
print()


# In[20]:


a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print()


# In[23]:


x,y=input("Enter the values :").split()
print("My name is {} ,I am a {}. ".format(x,y))
print()


# In[27]:


x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)


# In[3]:


# taking multiple inputs at a time separated by comma
x,y = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)
print(y)
print()


#  x, y = [int(x) for x in input("Enter two value: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print()
#  

# In[17]:


# flush argument


import time
 
count_seconds = 5
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(0.5)
    else:
        print('Start')


# In[22]:


#file argument


import io

# declare a dummy file
du_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=du_file)

# get the value from dummy file
du_file.getvalue()


# In[31]:


print("geeks",end =' '),
print('geekforgeeks')


# In[34]:


x = [1,3,4,5,2]

for i in range(4):
    print(x[i],end =' ')


# In[36]:


x = [1,3,4,5,2]

for i in range(4):
    print(i,end =' ')


# In[37]:


x = [1,3,4,5,2]

for i in x:
    print(i,end =' ')


# In[40]:


a=[2,'dwdwd','2,2']
print(*a)


# In[ ]:




