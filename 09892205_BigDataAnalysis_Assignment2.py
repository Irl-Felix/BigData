#StudentNumber:09892205
#Name:Javio Felix
import pandas as pd
import numpy as np

#2. Load the data frame and set column state as the index.
df = pd.read_csv("SuperStoreSales.csv",index_col="State")
OriginalDataFrameUsage = df.memory_usage()
OriginalDataUsagesum = OriginalDataFrameUsage.sum()

#3. reduced memory usages of DataFrame by changing data types of columns.
df = df.astype({'Row ID': 'int8','Postal Code': 'int8','Quantity': 'int8'})
df = df.astype({'Sales': 'float16','Discount': 'float16','Profit': 'float16'})
NewDataUsage = df.memory_usage()
NewDataUsagesum = NewDataUsage.sum()
print("Before Reduced Memory")
print(OriginalDataUsagesum)
print("After Reduced Memory")
print(NewDataUsagesum)
print()

#[4]. selecting the smallest of the largest to find the 5 lowest profits Product Name from the top 1000 sales of products.
print(df.nlargest(1000,"Sales").nsmallest(5,"Profit"))
print()

#[5]. select the “City” column as a Series with the indexing operator.
CitySeries = df['City']
print(CitySeries)

#using the .iloc[] indexer.
print(CitySeries.iloc[10])

#using the .loc[] indexer.
filt = df["City"] == "Los Angeles"
print(CitySeries.loc[filt][10])
print()

[6]#DataFrame rows with the .iloc[] and .loc[] indexers.
#using the .iloc[] indexer.
print(df.iloc[[99]])

#using the .loc[] indexer.
print(df.loc[df['Row ID'] == 100])
print()

# [7]. Please select the DataFrame rows and columns simultaneously. Please select
#using .loc[]
print(df.loc[:,["Category","Sub-Category","Sales","Profit"]])

#using .iloc[]
print(df.iloc[:,[13,14,16,19]])
print()

#[8] Find the number of profits that are more than 2000 dollars.
print(df.loc[df["Profit"]>2000])

number_of_profits = df['Profit'] > 2000
print("The number of Profits are more than 2000 are :")
print(number_of_profits.sum())
print()

#[9] Please use the data analysis method of translating SQL Where Clauses to find the products that meeting with 
#four criteria. (1) state is California. (2) Category is Technology (3) Sales are greater than 4000 dollars. 
#(4) Profits are greater than 5000 dollars.
"""
SELECT 
 State,
 Category,
 Sales,
 Profit
FROM
 SuperStoreSales
WHERE
 State = 'Califonia'
 AND
 Category = 'Technology'
 AND
 Sales > 4000
 AND
 Profit > 5000;
 """

print(df.query("State == 'California' and Category == 'Technology' and Sales > 4000 and Profit > 5000 "))
print()

#Second Way to display SQL statements
df2 = pd.read_csv("SuperStoreSales.csv")
states = ['California']
cat = ['Technology']
states_criteria = df2.State.isin(states)
cat_criteria = df2.Category.isin(cat)
sales_criteria = (df2.Sales > 4000)
profit_criteria = (df2.Profit > 5000)
criteria_all = (states_criteria & cat_criteria & sales_criteria & profit_criteria)
select_columns = ['State', 'Category','Sales','Profit']
print(df2.loc[criteria_all, select_columns])
print()

