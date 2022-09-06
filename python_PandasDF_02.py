import pandas as pd
import numpy as np

##01-01 add, radd
#DataFrame.add(other, axis='columns', level=None, fill_value=None)
#DataFrame.radd(other, axis='columns', level=None, fill_value=None)

data = [[1,10,100], [2,20,200], [3,30,300]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data = data, index = row, columns = col)
print(df)

#df + scalar
result = df.add(1)
print(result)

result = df + 1
print(result)

data2 = [[3],[4],[5]]
df2 = pd.DataFrame(data = data2, index = row, columns = ['col1'])
print(df2)

#add object
result = df.add(df2)
print(result)

#use fill.value
result = df.add(df2, fill_value = 0)
print(result)

##01-02 sub, rsub
#DataFrame.sub(other, axis='columns', level=None, fill_value=None)
#DataFrame.rsub(other, axis='columns', level=None, fill_value=None)

#df - scalar
result = df.sub(1)
print(result)

result = df - 1
print(result)

#substract object
result = df.sub(df2)
print(result)

#use fill.value
result = df.sub(df2, fill_value = 0)
print(result)

##01-03 mul, rmul
#DataFrame.mul(other, axis='columns', level=None, fill_value=None)
#DataFrame.rmul(other, axis='columns', level=None, fill_value=None)

#df * scalar
result = df.mul(2)
print(result)

result = df * 2
print(result)

#multiply object
result = df.mul(df2)
print(result)

#use fill.value
result = df.mul(df2, fill_value = 1)
print(result)

##01-04 div, rdiv
#DataFrame.div(other, axis='columns', level=None, fill_value=None)
#DataFrame.rdiv(other, axis='columns', level=None, fill_value=None)

#df / scalar
result = df.div(2)
print(result)

result = df / 2
print(result)

#devide object
data2 = [[0],[2],[3]]
df2 = pd.DataFrame(data = data2, index = row, columns = ['col1'])
result = df.div(df2)
print(result)

#use fill.value
result = df.div(df2, fill_value = 1)
print(result)

##01-05 mod, rmod
#DataFrame.mod(other, axis='columns', level=None, fill_value=None)
#DataFrame.rmod(other, axis='columns', level=None, fill_value=None)

#df % scalar
data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data = data, index = row, columns = col)
print(df)

result = df.mod(7)
print(result)

result = df % 7
print(result)

#object
data2 = [[2],[3],[5]]
df2 = pd.DataFrame(data = data2, index = row, columns = ['col1'])

result = df.mod(df2)
print(result)

#use fill.value
result = df.mod(df2, fill_value = 1)
print(result)

##01-06 pow, rpow
#DataFrame.pow(other, axis='columns', level=None, fill_value=None)
#DataFrame.rpow(other, axis='columns', level=None, fill_value=None)

#df ** scalar
result = df.pow(3)
print(result)

result = df ** 3
print(result)

#object
data2 = [[0],[3],[5]]
df2 = pd.DataFrame(data = data2, index = row, columns = ['col1'])

result = df.pow(df2)
print(result)

#use fill.value
result = df.pow(df2, fill_value = 1)
print(result)

##01-07 matrix multiply, dot
#DataFrame.dot(other)
#make data frame
col = ['col1','col2']
row = ['row1','row2']
data1 = [[1,2],[3,4]]
data2 = [[5,6],[7,8]]
df1 = pd.DataFrame(data1)#, row, col)
df2 = pd.DataFrame(data2)#, row, col)
print(df1,'\n', df2)

#multiply matrix
df3 = df1.dot(df2)
print(df3)
print(1*5+2*7)
df4 = df2.dot(df1)
print(df4)
print(5*1+6*3)