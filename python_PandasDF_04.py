import pandas as pd
import numpy as np

##04-01 indexing by scalar based label
#DataFrame.at

df = pd.DataFrame([[1,2], [3,4]], index=['row1', 'row2'], columns=['col1', 'col2'])
print(df)

result = df.at['row1', 'col2']
print(result)

df.at['row2', 'col1'] = 'change'
print(df)

##04-02 data based label 
#DataFrame.loc
df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3'])
print(df)

#indexing
result = df.loc['row1'] #series
print(result)

result = df.loc[['row1', 'row3']] #data frame
print(result)

result = df.loc['row2', 'col2']
print(result)

result = df.loc['row1':'row3','col2']
print(result)

bool = [False, True, False]
result = df.loc[bool]
print(result)

result = df.loc[df['col3'] > 5]
print(result)

result = df.loc[df['col3'] > 5, ['col2']]
print(result)

result = df.loc[lambda df: df['col2'] == 5]
print(result)

#replace
df.loc[['row1','row3'],['col3']] = 'A'
print(df)

df.loc[['row1']] = 'A1'
print(df)

df.loc[:, ['col3']] = 'A2'
print(df)

df.loc[['row1'],['col2']] = 2
df.loc[df['col2'] > 3] = 'A3'
print(df)

##04-03 ini scarla
#DataFrame.iat
df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3'])
print(df)

#start from 0
result = df.iat[1,2]
print(result)

df.iat[1,2] = 'A'
print(df)

##04-04 iloc
#DataFrame.iloc
df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3'])
print(df)

result = df.iloc[0] #series
print(result)

result = df.iloc[[0,2]] #DataFrame
print(result)

result = df.iloc[1:2]
print(result)

bool_list = [True, False, True]
result = df.iloc[bool_list]
print(result)

result = df.iloc[lambda x: x.index == 'row3']
print(result)

##04-05 n row indexing
#DataFrame.head(n=5)

data = np.random.randint(10,size=(10,10))
df = pd.DataFrame(data=data)
print(df)

#n>0 from top
print(df.head(3))

#n<0 except from bottom
print(df.head(-3))

##04-06 n row indexing from bottom
#DataFrame.tail(n=5)
print(df.tail(3))
print(df.tail(-3))

##04-07 Multi indexing
index_tuples = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
values = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]
index = pd.MultiIndex.from_tuples(index_tuples) # 인덱스 설정
df = pd.DataFrame(values, columns=['col1', 'col2', 'col3'], index = index)
print(df)

#index one row -> single index
result = df.loc['row2']
print(result)

result = df.loc[('row2', 'val2')] #input tuple output series
print(result)

result = df.loc[[('row2', 'val2')]] #output dataframe
print(result)

result = df.loc[('row2', 'val2'),'col3']
print(result)

result = df.loc[('row1','val2') : ('row3','val2')]
print(result)