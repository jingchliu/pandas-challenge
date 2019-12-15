#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[22]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[14]:


total=purchase_data["SN"].nunique()
total_df=pd.DataFrame({'Total Players':[purchase_data["SN"].nunique()]})
total_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[11]:


pd.options.display.float_format = '${:,.2f}'.format
item=purchase_data["Item ID"].nunique()
average=purchase_data["Price"].mean()
purchase=purchase_data["Purchase ID"].count()
revenue=purchase_data["Price"].sum()
summary1_df=pd.DataFrame({
    "Number of Unique Items":[item],
    "Average Price":[average],
    "Number of Purchases":[purchase],
    "Total Revenue":[revenue]
})
summary1_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[20]:


pd.options.display.float_format = '{:,.2f}%'.format
male_df=purchase_data.loc[purchase_data["Gender"]=="Male",:]
male_count=male_df["SN"].nunique()
male_percent=male_count/total*100
female_df=purchase_data.loc[purchase_data["Gender"]=="Female",:]
female_count=female_df["SN"].nunique()
female_percent=female_count/total*100
other=total-female_count-male_count
other_percent=other/total*100
summary2_df=pd.DataFrame({
    "":["Male","Female","Other / Non-Disclosed"],
    "Total Count":[male_count,female_count,other],
    "Percentage of Players":[male_percent,female_percent,other_percent]
})
summary2_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[33]:


filtered_df=purchase_data.groupby(["SN"])
filtered_df

# gender_info_df=purchase_data.groupby(["Gender"])
# average_gender=gender_info_df["Price"].mean()
# purchase_gender=gender_info_df["Purchase ID"].count()
# revenue_gender=gender_info_df["Price"].sum()
# avgpp_gender=revenue_gender/gender_info_df.count()
# gender_info_df
# summary3=pd.DataFrame({
#     "Total Count":[male_count,female_count,other],
#     "Percentage of Players":[male_percent,female_percent,other_percent]
# })
# summary3


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:





# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:




