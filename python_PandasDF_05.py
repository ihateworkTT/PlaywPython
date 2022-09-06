import pandas as pd
import numpy as np

##05-01
#pandas.DataFrame.gt(other, axis='columns', level=None) >
#pandas.DataFrame.lt(other, axis='columns', level=None) <
#pandas.DataFrame.ge(other, axis='columns', level=None) >=
#pandas.DataFrame.le(other, axis='columns', level=None) <=
#pandas.DataFrame.eq(other, axis='columns', level=None) ==
#pandas.DataFrame.ne(other, axis='columns', level=None) !=

col = ['col1','col2','col3']
row = ['A','B','C']
df = pd.DataFrame(data=[[10,20,10],[80,30,60],[20,10,70]],index=row,columns=col)
print(df)

#compare with scalar
print(df.eq(10))
print(df.ne(20)) #ne = not equal

#compare with series
s1 = pd.Series([10,30], index=['col1','col3'])
print(df.gt(s1)) #gt = greater than

s2 = pd.Series([10], index=['col4'])
print(df.lt(s2)) #lt = less than

#by axis
print(df.le([10,20,30], axis='columns')) #le = less equal
print(df.le([10,20,30], axis='index'))

#compare with dataframe
df2 = pd.DataFrame([[50],[50],[50]], index = row, columns = ['col1'])
print(df2)

print(df.ge(df2)) #ge = greater equal


#multi index
row_mul = [['U','U','U','D','D','D'],['A','B','C','A','B','C']]
df_mul = pd.DataFrame(data=[[10,20,10],[80,30,60],[20,10,70],[30,70,60],[10,90,40],[50,30,80]],index=row_mul,columns=col)
print(df_mul)

print(df.ge(df_mul, level=1))

##05-02 select dtype
#DataFrame.select_dtypes(include=None, exclude=None)

col1 = [1, 2, 3, 4, 5]
col2 = ['one', 'two', 'three', 'four', 'five']
col3 = [1.5, 2.5, 3.5, 4.5, 5.5]
col4 = [True, False, False, True, True]
df = pd.DataFrame({"col1": col1, "col2": col2, "col3": col3, "col4": col4})
print(df)
print(df.dtypes)

#select type 
#include
result = df.select_dtypes(include = ['float','bool'])
print(result)

#exclude
result = df.select_dtypes(exclude = ['int64'])
print(result)

#both
result = df.select_dtypes(include = ['float', 'object'], exclude = ['int64'])
print(result)

##05-03 
#DataFrame.clip(lower = None, upper=None, axis=None, inplace=False, args, kwargs)
col  = ['col1','col2','col3']
row  = ['row1','row2','row3']
data = [[-7,3,9],[6,-8,1],[-3,0,7]]
df = pd.DataFrame(data, row, col)
print(df)

#set upper and lower limit
print(df.clip(-4, 5))

#using series
s = pd.Series(data=[1,2,3], index=row)
print(df.clip(-s,s,axis=0))

##05-04 lable filter
#DataFrame.filter(items=None, like=None, regex=None, axis=None)

col  = ['alpha','beta','gamma','delta','epsilon']
row  = ['sigma','omega','lambda']
data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)

#using item
print(df.filter(items=['alpha','delta']))
print(df.filter(items=['omega'], axis=0))

#using like (including string)
print(df.filter(like='ta'))

#using regex (regular expression)
print(df.filter(regex = '[mn]')) #including m or n
print(df.filter(regex='^g')) #start with g
print(df.filter(regex='a$')) #end with a

##05-05 extract sample
#DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)

col  = ['col1','col2','col3']
row  = ['row1','row2','row3','row4','row5']
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.sample(n=2)) #extract 2 rows randomly
print(df.sample(10, replace = True)) #allow repeated sampling
print(df.sample(frac=0.4)) #set sampling fraction 0.4 = 40%

s = pd.Series(data = [10,10,3,3,1], index=row)
print(df.sample(n=2, weights=s)) #weight

print(df.sample(n=5, random_state=2)) #make same sampling several times
print(df.sample(n=3, ignore_index=True)) #replace index with number