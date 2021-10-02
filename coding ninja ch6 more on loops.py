#!/usr/bin/env python
# coding: utf-8

# # For loop

# In[1]:


s="abcd"
for c in s:
    print(c)


# In[2]:


#print num from 1 to 0
n=int(input())
for i in range( 0,n,1):
    print(i)


# In[1]:


#printing numbers from n to 1
n=int(input())
for i in range (n,0,-1):
    print(i)


# In[3]:


#printing numbers multiple of 3 starting from a till b ..all numbers residing betwee them which are mulltiples of 3 should be printed
a=int(input("Enter the starting value"))
b=int(input("Enter the last value of the range"))

for i in range (a,b+1):   #since we want to go till b thus taking b+1 to reach b completely
    if(i%3==0):  #since we want to print only multiples of three thus by this we willl print only that numbers which are divisble by 3
        print(i) 
    
    
#But the problem with this solution is that this loop is executing 10 times is our range is 10 and will execute 1000 times if our range will be 1000 
#thus to make it feasible there's a solution below code


# In[4]:


a=int(input("Please enter the starting value of the desired range"))  #in dis solution we will firstly tske the first number starting from a side which is divisible by 3 and then 
b=int(input("Enter the ending value of the desired range"))  # we will print further in the range with the stride/jumping value 3 to get the numbers
if a%3==0:
    s=a
elif a%3==1:
    s=a+2  #since any number didived by 3 will remainder as zero,1 or 2 nothing else thus we will add 2 if we get remainder 1 to make the number od
else:
    s=a+1   #if the remainder after division by 3 come 2 then we will basically add 1 so that the number we want will be only one step further
for i in range(s,b+1,3):
    print(i)


# In[8]:


#checking the number is prime or not with for loop
n=int(input("Enter the number"))
flag=False                                               #Important note that..in the usage of for loop we dont need to increment the values 
for d in range (2,n-1):                                #such as we used to do in the while loops ..the for loop takes care of this 
    if (n%d==0):
        flag=True               #here we took d which goes from a to n-1 and to see thaht if d can divide n 
        #in simple language we ran d from 2 to n-1 thus to see whether d is divisible or not and then used the flag technique we used n while loops to check number is prime or not 
if flag:
    print("Number is not prime")
else:
    print("The number is prime")


# In[1]:


n=int(input())
for i in range(1,n+1):
    for s in range (n-i):         #for each row we need to first print spaces tus we are taking the range of s i.e spaces
        print(" ",end=" ")
    for j in range(i,2*i,1):
        print(j,end= "")
    for j in range (2*1-2,i-1,-1):
        print(j,end=" ")
    print()
    


# Create a list 

# In[1]:


sidd_list=[]
sidd_list=[1,2,3]
type(sidd_list)


# # Functions and default parameters

# all non default arguments should be declared first

# In[2]:


#here we will see the default arguments and its types
def f(a=0,b,c):                 #Note that here .. an error occurred becuase..in pythin we cant declare the default arguments first.
    return a+b+c   #we need to declare all the non-default arguments firstly and then the default arguments
f(1,2)


# In[5]:


def f1(a,b,c=2,d=0):
       return a+b+c+d
print(f1(2,3,4,5)) #thus here c will take the value 4 and the d will take 5 because we have declared them 
print(f1(2,3)) #here a willl be 2 b will be 3 and c will be defaultly 2 and the d will be 0
print(f1(2,3,5))#here we mixed up thus a will be 2 b will be 3 and c will be 5 but we didnt declared any for d thus it wil defaultly be 0 
"""no we here often get confused in the 3rd print that the 2 wil be assigned to which value...so the assigning 
takes place respectively..the first argument we are passing whilce calling the function will be assigned to the first argument defined in the function 
and this goes in order"""





#so now here we will see is there any way to declare a,b and d ...and we c to be default


# Line Separated input

# In[2]:


n=int(input("Enter the number of elements you want to enter"))
li=[]
for i in range(n):
    curr=int(input("Enter the elements you want to enter:- "))
    li.append(curr)
li


# In[5]:


#Now here want to take inputs in the list in thr form of space wise elements 
str=input("please enter the elements with spcae: ")
str_split=str.split(" ")
str_split


# Linear search

# In[2]:


n=int(input("Enter the number of elements :- "))
li=[int(x) for x in input().split()]
ele=int(input("Enter the element which needs to be checked:- ")) #ele is the element to be searched
isFound=False
for i in range (len(li)):
    if li[i]==ele:
        print(i,"The element is present and the index position is ")
        isFound=True
        break 
if isFound is False:
    print(-1)


# Linear search through functions

# In[3]:


def linear_search(li,ele):
    for i in range (len(li)):
        if li[i]==ele:
            return i 
    return -1
  #li is the list and ele is the element to be searched
li=[1,2,3,4,5]
index=linear_search(li,6)  #here we will search .. and we need to give the list in which we need to search and the element we want to search 
print(index)
#if the element is present it will retrun index and if not will return -1


# Mutable

# In[6]:


x=3
a=3
print(x)
id(x)


# In[8]:


id (x) #now since here as x and a were having same value thus their reeence were same too 


# In[10]:


a=4
id(a)  #now here as we see ..the reference has changed  tus these are immutable


# passing list through functions

# In[12]:


def increment(li):
    li[0]=li[0]+2
    
li=[1,2,3,4]
increment(li)
print(li)


# Reversing a list
# list = [1,2,3,4,5] and after reversed it must be 6,5,4,3,2,1
# 
# 

# In[1]:


def reverse_l(li):
 ##   length=len(li)
   ## for i in range (length//2)
 ##   li[1],li[length-i-1]=li[length-i-1],
    print(li[::-1]) #THIS IS THE SLICING OPERATOR W ICH WILL REDUCE ITS THE COMPLEXITY OF REVERSING THE STRING


# In[8]:


def binary_search(arr,ele):
    start=0
    end=len(arr)-1
    
    
    while(start<=end):
        mid=(start+end)//2
        if (arr[mid]==ele):
            print("Element has been found and its index is ",mid)
            return mid
        elif(arr[mid]<ele):  #since if the element will be greater than the mid thus it will be present in the right side 
            start=mid+1    #so the new start will obviously be the mid +1  just note that in this situation only the start position will be changes
        else: #here in this if the elemnt is lower than the mid thus it will be obviously in the left part where the start will be as usual but the end will no be changed to the mid -1
            end=mid-1
            
            
        
        
    return -1

    
    
    
arr=[1,3,8,9,11,13,70,89,98]
index=binary_search(arr,3)
print(index)


# selection sort 

# In[14]:


def selectionsort(arr):
    length=len(arr)
    for i in range(length -1):
        minIndex=i
        #calculating the index of minimum element for this iteration 
        for j in range(i+1,length):
            if (arr[j]<arr[minIndex]):
                minIndex=j
        arr[i],arr[minIndex] =arr[minIndex],arr[i]
arr=[4,6,8,9,2,3,1]
selectionsort(arr)
print(arr)
    


# Bubble sort 

# In[5]:


def bubbleSort(arr):  #i is for n-1 rounds 
    length=len(arr)      #j is for in each iteration u need to go till length -1-i position
    for  i in range(length-1):  #since we need to go for n-1 rouds we are talking of the rounds... not the sb rounds
        for j in range(length-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            


arr=[6,4,52,1,7,3]
bubbleSort(arr)
print(arr)


# In[ ]:




