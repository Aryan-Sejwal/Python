import pandas as pd
data = {
"Name":["A","B","C","D","E"],
"Marks":[80,75,90,85,70]
}
df = pd.DataFrame(data)
print(df.head(3))