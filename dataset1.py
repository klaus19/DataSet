import pandas as pd

#  create a dictionary of data that you want to include in your dataset
data = {
    'name': ['John', 'Jane', 'Mike', 'Emily'],
    'age': [25, 32, 45, 28],
    'gender': ['M', 'F', 'M', 'F']
}

# Create a new Pandas DataFrame using the pd.DataFrame() function and passing in the data dictionary.

df = pd.DataFrame(data)

# Print the first 5 rows
print(df.head())

# Print the number of rows and columns
print(df.shape)

# Save the DataFrame as a CSV file
df.to_csv("dataset1.csv",index=False)
