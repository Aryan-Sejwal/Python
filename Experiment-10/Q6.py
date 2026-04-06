import pandas as pd
import numpy as np
data = {
    "A":[1,2,np.nan,4],
    "B":[5,np.nan,7,8]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n",df)
df.fillna(df.mean(), inplace=True)
print("Updated DataFrame:\n",df)