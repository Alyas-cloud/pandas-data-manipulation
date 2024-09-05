import pandas as pd

# Sample data from the error message
data = {
    'SalesRep': ['Amy', 'Amy', 'Amy', 'Amy', 'Amy'],
    'Region': ['North', 'North', 'North', 'North', 'North'],
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [23040.0, 24131.0, 24646.0, 22047.0, 24971.0],
    'Units Sold': [239.0, 79.0, 71.0, 71.0, None]
}

df = pd.DataFrame(data)

# Display the first 5 rows of the DataFrame
print(df.head())

# Corrected filtering: Replace 'column_name' with actual column name, e.g., 'SalesRep'
filtered_df = df[df['SalesRep'] == 'Amy']

# Basic statistical summary of the data
print(df.describe())

# Selecting specific columns
selected_columns = df[['Sales', 'Units Sold']]

# Adding a new column based on existing columns
df['Total Sales'] = df['Sales'] * df['Units Sold']

# Grouping data and performing aggregation (e.g., by Region)
grouped_df = df.groupby('Region').agg({'Sales': 'mean', 'Units Sold': 'mean'})

# Saving the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)

# Print filtered DataFrame
print(filtered_df)
