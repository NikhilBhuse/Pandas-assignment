#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Q1. How do you load a CSV file into a Pandas DataFrame?


# Importing
import pandas as pd
# Read the csv file
df = pd.read_csv(r"E:\New folder\luup\data_sheet.csv")
# printing
print(df)


# In[87]:


# Q2. How do you check the data type of a column in a Pandas DataFrame?
import pandas as pd

df = pd.read_csv(r"E:\New folder\luup\data_sheet.csv")

print(df.dtypes)


# In[31]:


# Q3. How do you select rows from a Pandas DataFrame based on a condition?

# importing pandas
import pandas as pd

# Creating data frame

df = pd.DataFrame({"Flights" : ["Air india","Indigo","Indigo","Vistra","Go air","Spice jet"],
                    "Destination": ["Pune","Mumbai","Bhopal","Indore","Chennai","Gujrat"],
                    "Price" : [6700,7500,7000,5500,8000,4500],
})
print(df,"\n")

df.loc[(df["Price"]>=7000)]


# In[51]:


#Q4. How do you rename columns in a Pandas DataFrame?
import pandas as pd

df =  {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
# Convert the dictionary into DataFrame
change_pd = pd.DataFrame(df)
print(change_pd)

change_pd.rename(columns = {'Name' : 'name','Age':'age','Address':'address','Qualification':'Education'},inplace = True)
#Rename the column and print
print("\nAfter remane the columns:-\n",change_pd.columns)


# In[6]:


#Q5.How do you drop columns in a Pandas DataFrame?


import pandas as pd

df =  {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
#Convert the dictionary into DataFrame
df_1 = pd.DataFrame(df)
  

#Remove column name 'Age'
df_1.drop(['Age'], axis = 1)


# In[14]:


#Q6. How do you find the unique values in a column of a Pandas DataFrame?

import pandas as pd

data1 = {'Name':['Aditya', 'Achal','Jay' , 'Harsha',
                 'Vinay', 'Prathmesh', 'Smita', 'Karan'],
        'Age':[23, 28, 42, 32,
               34, 36, 21, 30],
        'Address':['Indore', 'Tamil Nadu', 'Mumbai', 'Pune',
                   'Patna', 'Kanpur', 'Jaipur', 'Ayodhya'],
        'Qualification':['B.E', 'M.Tech', 'Bsc', 'B.Com',
                         'Msc', 'Law', 'BA', 'ME']}
#Convert the dictionary into DataFrame
df = pd.DataFrame(data1)
#print the unique values in a column 
df['Name'].unique()


# In[65]:


#Q7. How do you find the number of missing values in each column of a Pandas DataFrame?


import pandas as pd
# Read the csv file
df = pd.read_csv(r"E:\New folder\luup\aditya_pandas.Csv")
print(df)


#checking the total number of missing values
df.isnull().sum()


# In[69]:


# Q8. How do you fill missing values in a Pandas DataFrame with a specific value?

import pandas as pd
# Read the csv file
df = pd.read_csv(r"E:\New folder\luup\aditya_pandas.Csv")
print(df)


#Fill missing values  with a specific value
df.fillna(45)


# In[30]:


# Q9. How do you concatenate two Pandas DataFrames?

import pandas as pd

#Creating first data frame

data_1 = pd.DataFrame({"Name" : ["Virat","Rohit","KL rahul","Sanju","Sikhar"],
                        "Team" : ["Royal Challengers Bangalore","Mumbai Indians","Lucknow Supergiants","Rajasthan Royal","Punjab Kings"]})
#Creating second data frame

data_2 = pd.DataFrame({"Salary" :["18 Cr","18 Cr","15.5 Cr","14 Cr","15 cr"],
    
                        "Matches Win":[8,9,7,10,6]})
# using a .concat() method
# inner join
frames = pd.concat([data_1, data_2],axis = 1, join = "inner")

frames


# In[27]:


# Q10. How do you merge two Pandas DataFrames on a specific column

import pandas as pd

#Creating first data frame

data_1 = pd.DataFrame({"Name" : ["Virat","Rohit","KL rahul","Sanju","Sikhar"],
                        "Team" : ["Royal Challengers Bangalore","Mumbai Indians","Lucknow Supergiants","Rajasthan Royal","Punjab Kings"]})
#Creating second data frame 
data_2 = pd.DataFrame({"Name" : ["Ms Dhoni","lyer","Mayank","Hardik","Pant"],
                       "Team" : ["Chennai Super Kings","Kolkata Knight Riders","Sunrisers Hyderabad","Gujarat Titans","Delhi Capitals"]})
# concatenation (merge the column data_1,data_2)
frame = [data_1,data_2]

result = pd.concat(frame)
result


# In[108]:


# Q11.How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?

#Imorting pandas
import pandas as pd

#create a data fram from csv file
df = pd.read_csv(r"E:\New folder\luup\aditya_pandas.Csv")
#aggregation for specific columns
df.aggregate({"Unquie id":["sum","min"],"Age":["sum","min"]})


# In[31]:


# Q12. How do you pivot a Pandas DataFrame?

#Imorting pandas
import pandas as pd
#Creating DataFram
data_1 = pd.DataFrame({"Name" : ["Virat","Rohit","KL rahul","Sanju","Sikhar"],
                        "Team" : ["Royal Challengers Bangalore","Mumbai Indians","Lucknow Supergiants","Rajasthan Royal","Punjab Kings"],
                      "Salary" :["18 Cr","18 Cr","15.5 Cr","14 Cr","15 cr"],
                       "Matches Win":["8","9","7","10","6"]})

data_1
#values can be an object or a list(pivot)
data_1.pivot("Name","Team","Salary")


# In[195]:


#Q13. How do you change the data type of a column in a Pandas DataFrame?

# imporing pandas
import pandas as pd
data_1 = pd.DataFrame({"Name" : ["Amit","Lucky","vijay","krishna","Arjun","Rakesh","Ayush","Atul","Vikas"],
                       "Role" : ["Developer","Manager","Programmer","Tester","Techaican","Driver","Hr","Team lead","Cricketer"],
                        "ID" : ["23","12","5","56","34","77","67","46","89"],
                       "Salary" : [50000,150000,56000,44000,38000,30000,42000,75000,100000],
                       "Bonus" : [12000.22,25000.04,3333.34,5400.09,4400.44,4567.99,546.00,5647.98,8765.00]})
print(data_1)

#space
print("\n")
#Print Data type
print(data_1.dtypes)
#using method to convert data type of column by using "astype"
data_1["Bonus"]=data_1["Bonus"].astype(int)
print("\n",data_1)
print("\n",data_1.dtypes)


# In[35]:


# Q14. How do you sort a Pandas DataFrame by a specific column?

#Imorting pandas
import pandas as pd
#Creating DataFram
data_1 = pd.DataFrame({"Name" : ["Virat","Rohit","KL rahul","Sanju","Sikhar"],
                        "Team" : ["Royal Challengers Bangalore","Mumbai Indians","Lucknow Supergiants","Rajasthan Royal","Punjab Kings"],
                      "Salary" :["18 Cr","18 Cr","15.5 Cr","14 Cr","15 cr"],
                       "Matches Win":["8","9","7","10","6"]})
# After sorting
print(data_1)

#space
print("\n")


#sort data frame
sorted_df = data_1.sort_values(by="Salary")
print(sorted_df)


# In[21]:


# Q15. How do you create a copy of a Pandas DataFrame?

# importing pandas
import pandas as pd
# Read the csv file
df = pd.read_csv(r"E:\New folder\luup\aditya_pandas.Csv")
print(df)

#space
print("\n")

#copy of a dataframe
df.copy()
print(df)


# In[28]:


# Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?

# importing pandas
import pandas as pd

# Creating data frame

df = pd.DataFrame({"Flights" : ["Air india","Indigo","Indigo","Vistra","Go air","Spice jet"],
                    "Destination": ["Pune","Mumbai","Mumbai","Indore","Chennai","Gujrat"],
                    "Price" : [6700,7500,7000,5500,8000,4500],
                   "No of passanger" : [76,80,92,85,66,99]
})
print(df,"\n")

df.loc[(df["Price"]>=7500)]


# In[15]:


# Q17. How do you calculate the mean of a column in a Pandas DataFrame?


#Importing pandas
import pandas as pd

# creating data frame
df = pd.DataFrame({"courses": ["Java","Big data", "C++"," Data Analysis","Machaine learning"],
            "Tranniner" : ["Piyush","Abhinav","Amit","Aman","Nimita"],
            "Fees" : [7500, 20000, 5500, 18000, 19000 ],
            "No.of student" : [52,98,58,78,88]
      
})
print(df)

#space
print("\n")

#calculate the mean of a column
print(df[['Fees','No.of student']].mean())


# In[55]:


#Q18.How do you calculate the standard deviation of a column in a Pandas DataFrame?

#Importing pandas
import pandas as pd

# creating data frame
df = pd.DataFrame({"courses": ["Java","Big data", "C++"," Data Analysis","Machaine learning"],
            "Tranniner" : ["Piyush","Abhinav","Amit","Aman","Nimita"],
            "Fees" : [7500, 20000, 5500, 18000, 19000 ],
            "No.of student" : [52,98,58,78,88]
      
})
print(df)
#space
print("\n")


#The standard deviation of a column
print(df[['Fees','No.of student']].std())


# In[63]:


#Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?


#Importing pandas
import pandas as pd

# creating data frame
df = pd.DataFrame({"courses": ["Java","Big data", "C++"," Data Analysis","Machaine learning"],
            "Tranniner" : ["Piyush","Abhinav","Amit","Aman","Nimita"],
            "Fees" : [7500, 20000, 5500, 18000, 19000 ],
            "No.of student" : [52,98,58,78,88]
      
})
print(df)
#space
print("\n")

# correlation between two columns (Fees and no of student)
print(df['Fees'].corr(df['No.of student']))


# In[36]:


# Q20. How do you select specific columns in a DataFrame using their labels?
#Importing pandas
import pandas as pd

# creating data frame
df = pd.DataFrame({"courses": ["Java","Big data", "C++"," Data Analysis","Machaine learning"],
            "Tranniner" : ["Piyush","Abhinav","Amit","Aman","Nimita"],
            "Fees" : [7500, 20000, 5500, 18000, 19000 ],
            "No.of student" : [52,98,58,78,88]
      
})
print(df)
#space
print("\n")
df = pd.DataFrame(df,
                  columns=['courses', 'Tranniner',
                           'Fees', 'No.of student'])
#specific columns in a DataFrame using their labels
df_1 = df["Fees"]
df_1


# In[24]:


# Q21. How do you select specific rows in a DataFrame using their indexes?

import pandas as pd
# Read the csv file
df = pd.read_csv(r"E:\New folder\luup\aditya_pandas.Csv", index_col ="Name")
print(df,"\n")

# select specific rows in a DataFrame using their indexes with help of loc method
data = df.loc[["Harsh","Priya"]]
data


# In[3]:


# Q22. How do you sort a DataFrame by a specific column?

import pandas as pd
# Read the csv file
df = pd.read_csv(r"E:\New folder\luup\aditya_pandas.Csv")
print(df,"\n")
# sort a specific column of name
data = df.sort_values(by = ["Name"])
data


# In[41]:


# Q23. How do you create a new column in a DataFrame based on the values of another column?

# importing pandas
import pandas as pd

# Creating data frame

df = pd.DataFrame({"Flights" : ["Air india","Indigo","Vistra","Go air","Spice jet"],
                    "Destination": ["Pune","Mumbai","Indore","Chennai","Gujrat"],
                    "Price" : [6700,7000,5500,8000,4500]
})
print(df)
# create a new column in a DataFrame based on the values of another column
# 10 % discount in new column
df["Discount"] = df["Price"] - (0.1* df["Price"])

df


# In[50]:


#Q24. How do you remove duplicates from a DataFrame?

# importing pandas
import pandas as pd

# Creating data frame

df = pd.DataFrame({"Flights" : ["Air india","Indigo","Indigo","Vistra","Go air","Spice jet"],
                    "Destination": ["Pune","Mumbai","Mumbai","Indore","Chennai","Gujrat"],
                    "Price" : [6700,7000,7000,5500,8000,4500]
})
print(df,"\n")
#we Check duplicates are present in data frame or not (bool: True/Flase)
print(df.duplicated())
# remove duplicates from a DataFrame in rows based on all columns

df.drop_duplicates()


# In[ ]:


# Q25. What is the difference between .loc and .iloc in Pandas?


# Ans
# loc() and iloc() are one of those methods. These are used in slicing data from the Pandas DataFrame. They help in the convenient selection of data from the DataFrame in Python.

# The main distinction between the two methods is:

# loc gets rows (and/or columns) with particular labels.

# iloc gets rows (and/or columns) at integer locations.


# In[ ]:




