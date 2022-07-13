#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name :")
print("We will start learning about histogram and read, clean, and understand the Titanic dataset, and plot a histogram for showing the age group who has the highest death rate and who has the highest survival rate")
print("We will also derive in which class people died the most.")


# In[2]:


#predefine code for image
from IPython.display import Image
Image(filename='titanic.jpg') 
#predefine code end


# In[3]:


#import the required packages 
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file.
df = pd.read_csv("Titanic.csv")
df


# # Activity 1 - Plotting histogram showing the passenger of different age groups who survived
# 

# In[4]:



#Remove the rows from the data set where there are NaN values
df = df.dropna()

#Find out the passengers from the Titanic who survived in Titanic.
passengers_survived = df.loc[df['Survived'] == 1]
passengers_survived



# In[5]:


#Plot a histogram showing the passenger of titanic from different age groups who survived.
plt.figure(figsize=(7,7))
plt.hist(passengers_survived["Age"], bins=10)
plt.title("Number of survival as per age group")
plt.ylabel("count")
plt.xlabel("age")
plt.show()


# Conclusion: So from the Histogram we, can conclude that, most passengers who survived were in the age group of 20-40.

# # Activity 2 - Plotting histogram showing the passenger of different age groups who died.
# 

# In[7]:


#Find out the passengers from the Titanic who died.
passengers_died = df.loc[df['Survived']==0]
passengers_died


# In[8]:


#Plotting histogram showing the passenger of different age groups who died
plt.figure(figsize=(7,7))
plt.hist(passengers_died["Age"],bins=10)
plt.title("Number of deaths per age group")
plt.ylabel("count")
plt.xlabel("age")
plt.show


# Conslusion: 

# # Activity 3 - Find the total number of passengers who were travelling and total number of passengers who died from class1, class 2, and class 3. 

# In[8]:


#predefine code for image
Image(filename='titanic_classes.png') 
#predefine code end


# In[9]:


#Find the total number of passengers from class 1
total_class1=df.loc[df['Pclass']==1]['Pclass'].count()
total_class1


# In[10]:


#Find the total number of passengers who survived from class 1
survived=df.loc[df['Survived']==1]&df()


# In[11]:


#Find the total number of passengers from class 2


# In[12]:


#Find the total number of passengers who survived from class 2


# In[13]:


#Find the total number of passengers from class 3


# In[14]:


#Find the total number of passengers who survived from class 3


# In[15]:


#Plot a stacked bar graph for showing highest numbers of deaths was in which class


# Conclusion: 

# In[ ]:




