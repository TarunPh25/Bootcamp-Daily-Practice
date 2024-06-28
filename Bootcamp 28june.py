#Introduction to Pandas and DataFrames
'''Pandas is a powerful data manipulation and analysis library for Python. It provides data structures and functions needed to manipulate structured data seamlessly. One of the primary data structures in pandas is the DataFrame, a 2-dimensional labeled data structure with columns of potentially different types.

A DataFrame can be thought of as a table or a spreadsheet in which you can store and manipulate data easily.

DataFrame Creation:

Creating a DataFrame in pandas is straightforward. You can create it from various data structures like lists, dictionaries, or even from files (like CSV, Excel). Here's an example of creating a DataFrame from a dictionary.
'''
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 65000, 85000, 90000]
}
df = pd.DataFrame(data)
df
#Data Inspection:
#Once you have created a DataFrame, inspecting it to understand its structure and content is crucial. Pandas provides several methods for this purpose:
- `head()`: Displays the first few rows of the DataFrame.
- `info()`: Provides a concise summary of the DataFrame, including the number of non-null entries and data types.
- `describe()`: Generates descriptive statistics for numeric columns.

df.head()
df.info()
df.describe()

#Data Exploration:Data exploration involves examining the data to uncover patterns, anomalies, and insights. Here are some common operations:
- `sort_values()`: Sorts the DataFrame by specified columns.
- Filtering: Selects rows based on certain conditions.
- `groupby()`: Groups data based on specified columns and applies aggregate functions.

#Let's see these operations in action.
df_sorted = df.sort_values(by='Salary', ascending=False)
df_sorted

df_filtered = df[df['Age'] > 25]
df_filtered

df_grouped = df.groupby('City').mean()
df_grouped


#Data Visualization: Visualizing data helps in better understanding and interpreting the information. Matplotlib is a popular library for creating static, interactive, and animated visualizations in Python. Here's an example of creating a bar chart to visualize the salary of individuals.
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary of Individuals')
plt.show()

