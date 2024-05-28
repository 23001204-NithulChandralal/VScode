import pandas as pd

data = {
    "attempts": [1, 3, 2],
    "name": ["Ann", "James", "John"],
    "score": [12.5, 16.5, 4.5]
}

df1 = pd.DataFrame(data)

Filtered_DF = df1[df1['attempts'] > 1 & df1['score'] < 10]
print(Filtered_DF)