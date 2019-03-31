
# coding: utf-8

# 

# # SF Salaries analysis
#  We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle!

# ** Import pandas as pd.**

# In[1]:

import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:

sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[3]:

sal.head(10)


# ** Use the .info() method to find out how many entries there are.**

# In[4]:

sal.info() # 148654 Entries


# **What is the average BasePay ?**

# In[5]:

sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[6]:

sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[7]:

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[8]:

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[9]:

sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()] #['EmployeeName']
# or
# sal.loc[sal['TotalPayBenefits'].idxmax()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[10]:

sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()] #['EmployeeName']
# or
sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']

## ITS NEGATIVE!! VERY STRANGE


# In[ ]:




# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[11]:

sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[12]:

sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[13]:

sal['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[14]:

sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[15]:

def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False


# In[16]:

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[17]:

sal['title_len'] = sal['JobTitle'].apply(len)


# In[18]:

sal[['title_len','TotalPayBenefits']].corr() # No correlation.


# 

# In[ ]:



