
# coding: utf-8

# In[1]:

print("season name")
month=input("enter month name")
if month in ("january", "febraury", "march"):
    print("winter")
elif month in ( "april","may", "june"):
    print("spring")
elif month in ("july", "august","september"):
    print("summer")
elif month in ("october", "november","december"):
    print("autumn")


# In[31]:

print ("season with digits")
x=int(input("enter a month number "))
if (x>=1 and x<=3):
    print("it's winter")
elif (x>=4 and x<=6):
    print("it's spring")
elif (x>=7 and x<=9):
    print("it's summer")
elif (x>=10 and x<=12):
    print("it's autumn")
else:
    print("please input valid month")


# In[29]:

print("leap year program")
year= int(input("enter year"))
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# In[7]:

print("seperate number and strings")
string=input("enter string")
d=l=0
for c in string:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print ("letter are",l)
print ("digits are",d)


# In[33]:

print("print reverse string")
s="Hello world"
for i in s:
    print(i)
s[-1::-1]


# In[ ]:



