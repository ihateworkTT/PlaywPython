import pandas as pd
import numpy as np

data = {'A': [1,2], 'B': [3,4]}
df = pd.DataFrame(data = data)
print(df)

a = np.array([[1,2],[3,4]])
df = pd.DataFrame(data=a, index = ['row1', 'row2'], columns = ['col1', 'col2'])
print(df)