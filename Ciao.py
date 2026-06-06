import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', np.nan, 'London'],
    'Occupation': ['Engineer', 'Designer', 'Artist', 'Doctor']
}

df = pd.DataFrame(data)
df['City'] = df['City'].fillna('Unknown')

Names = df['Name']

print(df)
print(Names)

grouped = df.groupby(['City','Occupation'])['Age'].sum()
print(grouped)
