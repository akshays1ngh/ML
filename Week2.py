#!/usr/bin/env python
# coding: utf-8

# In[2]:


#LAB2


# In[4]:


n=int(input("Enter a number: "))


# In[5]:


def check(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
check(n)


# In[6]:


#lambda function

sum2=lambda arg1,arg2:arg1+arg2
prod=lambda arg1,arg2:arg1*arg2

print("Sum is: ",sum2(10,20))
print("Product is: ",prod(10,20))


# In[7]:


def printing(names):
    for x in names:
        print(x)

name={'Akshay','Yuvika'}
printing(name)


# In[8]:


def recur(n):
    if(n<0):
        return 0
    return n+recur(n-1)
sum=recur(5)
print(sum)


# In[9]:


import pandas as pd


# In[13]:


dict={
    "country": ["India","Japan","Brazil","Russia"],
    "capital": ["Delhi","Tokyo","Brasilia","Moscow"],
    "area":[1000,100,200,500],
    "population":[500,1000,1500,2000]
}
brics=pd.DataFrame(dict)
brics


# In[16]:


df=pd.read_csv('mtcars.csv')
df


# In[17]:


type(df)


# In[18]:


df.head(4)


# In[19]:


df["model"]


# In[20]:


df["gear"]


# In[21]:


type(df["model"])#series format data


# In[22]:


#to conver series data to DataFrame
df[["model"]]


# In[24]:


df[["model","gear"]]


# In[32]:


#For displaying all columns
df.columns


# In[33]:


#Displaying columns in the form of a list
data=list(df.columns.values)
data


# In[34]:


df.shape


# In[38]:


#Accessing the required columns only
req_col=data[:3]#this type of accessing can be only done in a list
df[req_col]


# In[40]:


#Accessing data in different ways
#Double bracket so displayed in the form of DataFrame

df.iloc[[1,2,3],[0,1]] #{3 rows,2 cols}


# In[41]:


#FILTERING PANDAS DATAFRAME


# In[ ]:


import numpy as np
df[np.logical_and(df['model'])]


# In[43]:


df['new_col']=10
df


# In[45]:


df['check']=df['disp'].apply(lambda val: "good" if disp>160.0 else "not good")


# In[47]:


df=pd.read_csv('mtcars.csv')
df


# In[48]:


#1. Find the car with best mpg.
maxmpg=df['mpg'].idxmax()
print(df.iat[maxmpg,0])
print(df['mpg'].max())


# In[49]:



#2. Find the car with worst mpg.
minmpg=df['mpg'].idxmin()
print(df.iat[minmpg,0])
print(df['mpg'].min())


# In[50]:


#3. Find the car with best horsepower.
besthp=df['hp'].idxmax()
print(df.iat[besthp,0])
print(df['hp'].max())


# In[51]:


#4. Find 5 summary number of displacement.
summary=df.describe()
print(summary)


# In[52]:


#5. Find the median horsepower.
medianhp=df['hp'].median()
print(medianhp)


# In[53]:


#6. Average mpg for manual vs mpg car.
am= df[df['am']==1]
avgam=am['mpg'].mean()
print("Average mpg for automatic cars: ",avgam)

manual= df[df['am']==0]
avgmanual=manual['mpg'].mean()
print("Average mpg for manual cars: ",avgmanual)


# In[56]:


import matplotlib.pyplot as plt
#7. Histogram of miles per gallon.
plt.hist(df['mpg'])
plt.title("miles per gallon")
plt.xlabel("Miles")
plt.ylabel("Gallons")
plt.show()


# In[57]:


import matplotlib.pyplot as plt
#8. Boxplot for mpg of each cylinder.
cyl4= df[df['cyl']==4]

plt.boxplot(cyl4['mpg'])
plt.title("mpg for 4 cyl")
plt.show()

cyl6= df[df['cyl']==6]

plt.boxplot(cyl6['mpg'])
plt.title("mpg for 6 cyl")
plt.show()

cyl8= df[df['cyl']==8]

plt.boxplot(cyl8['mpg'])
plt.title("mpg for 8 cyl")
plt.show()


# In[58]:


#9. crosstab displaying count of automatic vs. manual cars.
manualvsam=pd.crosstab(df.am, df.am)
print(manualvsam)


# In[59]:


#10. crosstab displaying count of “am vs cyl”.
amvscyl=pd.crosstab(df.am,df.cyl)
print(amvscyl)

