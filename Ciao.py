import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Berlin'],
    'Occupation': ['Engineer', 'Designer', 'Artist', 'Doctor']
}

df = pd.DataFrame(data)

print(df)
