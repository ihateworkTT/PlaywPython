import pandas as pd
import numpy as np

##02-01 round
#DataFrame.round(decimals = 0, args, kwargs)

col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = np.random.rand(3,3)*1000
df = pd.DataFrame(data, row, col)
print(df)

#round, decimals = 0, 0 is default
print(df.round(0)) #or print(df.round())

#decimals > 0
print(df.round(1))
print(df.round(2))

#decimals < 0
print(df.round(-1))
print(df.round(-2))

##02-02 summarise
#DataFrame.sum(axis = None, skipna = None, level = None, numeric_only = None, min_count = 0, kwargs)

#make data 
data = [[1,2,3],[4,5,6],[7,np.NaN,9]]
df = pd.DataFrame(data, row, col)
print(df)

#aix = 0 sum by columns, aix =1 sum by rows, default is 0
print(df.sum(axis = 0))
print(df.sum(axis = 1))

#NOT ignore NaN
print(df.sum(skipna = False))

#min_count, 
print(df.sum(min_count = 3)) #needs minimum 3 , can't ignore NaN
print(df.sum(min_count = 2))

##02-03 prod, product
#DataFrame.prod(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)
#DataFrame.product(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)

#aix = 0 by column, aix =1 by raw, default is 0
print(df.prod(axis = 0))
print(df.prod(axis = 1))

#NOT ignore NaN
print(df.prod(skipna = False))

#min_count
print(df.prod(min_count=3))

##02-04 absolute value
#DataFrame.abs()

data = [[-1,2,-3.5],[4,-5.5,3+4j],[7,np.NaN,0]]
df = pd.DataFrame(data, row, col)
print(df)
print(df.abs())
print((3**2 + 4**2)**(1/2))

##02-05 Transpose
#DataFrame.transpose(args, copy = False)
#DataFrame.T(args, copy = False)

row = ['row1','row2','row3','row4']
data = [['A',1,2],['B',3,4],['C',5,6],['D',7,8]]
df = pd.DataFrame(data, row, col)
print(df)
print(df.transpose())

##02-06 Rank
#DataFrame.rand(axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)
data = [[5],[5],[pd.NA],[3],[-3.1],[5],[0.4],[6.7],[3]]
row = ['A★','B★','C','D☆','E','F★','G','H','I☆']
df = pd.DataFrame(data, row, columns=['Value'])
print(df)

#method
df['average'] = df['Value'].rank(method='average')
df['min'] = df['Value'].rank(method='min')
df['max'] = df['Value'].rank(method='max')
df['first'] = df['Value'].rank(method='first')
df['dense'] = df['Value'].rank(method='dense')
print(df)

#na option and percentage option
df = df.drop(['average', 'min','max','first','dense'], axis=1)
df['keep'] = df['Value'].rank(na_option='keep')
df['top'] = df['Value'].rank(na_option='top')
df['bottom'] = df['Value'].rank(na_option='bottom')
df['pct'] = df['Value'].rank(pct=True)
print(df)

##02-07 difference
#DataFrame.diff(periods=1, axis=0)
a = [1,2,3,4,5,6,7,8]
b = [1,2,4,8,16,32,64,128]
c = [8,7,6,5,4,3,2,1]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)

#axis = 0 by row, aix-1, by column
print(df.diff(axis=0))
print(df.diff(axis=1))

#periods
print(df.diff(periods=2))
print(df.diff(periods=3))

##02-08 percentile change
#DataFrame.pct_change(periods=1, fill_method='pad', limit=None, freq=None, kwargs)

a = [1,1,4,4,1,1]
b = [1,2,4,8,16,32]
c = [1,None,None,None,16,64]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)

#(next row - current row) / current row
print(df.pct_change())

#period
print(df.pct_change(periods = 2))
print(df.pct_change(periods = -1)) #periods <0, backward

#fill method, ffill -> front, bfill -> back
print(df.pct_change(fill_method='ffill'))
print(df.pct_change(fill_method='bfill'))

#limit, fill how many na value?
print(df.pct_change(limit=2))

##02-09 expending
#DataFrame.expanding(min_periods=1, center=None, axis=0, method='single')
import numba
data = {'col1':[1,2,3,4],'col2':[3,7,5,6]}
idx = ['row1','row2','row3','row4']
df = pd.DataFrame(data = data, index = idx)
print(df)

#cumulative 
print(df.expanding(min_periods=3).sum())

#axis = 1 by column
print(df.expanding(axis=1).sum())

#using numba library, by table
print(df.expanding(method='table').sum(engine='numba'))

##02-10 rolling
#DataFrame.rolling(window, min_periods=None, center=Flase, win_type=None, on=None, axis=0, closed=None, method='single')
period = pd.period_range(start='2022-01-13 00:00:00',end='2022-01-13 02:30:00',freq='30T')
data = {'col1':[1,2,3,4,5,6],'col2':period}
idx = ['row1','row2','row3','row4','row5','row6']
df = pd.DataFrame(data= data, index = idx)
print(df)

#window = set size
print(df.rolling(window=3).sum())

#closed
print(df.rolling(window=3, closed='left').sum())
print(df.rolling(window=3, closed='right').sum())
print(df.rolling(window=3, closed='both').sum())
print(df.rolling(window=3, closed='neither', min_periods=2).sum())

#centre
print(df.rolling(window=3, center=True).sum())

#win_type, weight
print(df.rolling(window=3, win_type='triang').sum())
print(df.rolling(window=3, win_type='gaussian').sum(std=3))

#on, ordered by time
print(df.rolling(window='60T', on='col2').sum())

##02-11 Group by
#DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=NoDefault.no_default, observed=False, dropna=True)
idx=['A','A','B','B','B','C','C','C','D','D','D','D','E','E','E']
col=['col1','col2','col3']
data = np.random.randint(0,9,(15,3))
df = pd.DataFrame(data=data, index=idx, columns=col).reset_index()
print(df)

print(df.groupby('index').mean())
print(df.groupby('index').count())

print(df.groupby('index').agg(['sum','mean','count']))

#avoid repeat index and column
def top(df, n=2, col='col1'):
	return df.sort_values(by=col)[-n:]
print(df.groupby('index').apply(top))
print(df.groupby('index', group_keys=False).apply(top))

#category
df_cat = pd.Categorical(df['index'], categories=['A','B','C','D','E','F'])
print(df_cat)
print(df['col1'].groupby(df_cat).count())
print(df['col1'].groupby(df_cat, observed=True).count())

#as_index=False -> remain oroginal index
print(df.groupby(['index'], as_index=False).sum())

#droup NA, decide how to deal with NA
df.loc[6,'index'] = np.NaN
print(df.groupby('index').sum()) #default = not include NA
print(df.groupby('index', dropna=False).sum()) 

#level
idx = [['idx1','idx1','idx2','idx2','idx2'],['row1','row2','row1','row2','row3']]
col = ['col1','col2','col2']
data = np.random.randint(0,9,(5,3))
df = pd.DataFrame(data=data, index = idx, columns = col).rename_axis(index=['lv0','lv1'])
print(df)
print(df.groupby(level=1).sum())
print(df.groupby(['lv1','lv0']).sum())

##02-12 exponentially weighted averages
#DataFrame.ewm(com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None, method='single')
data = {'val':[1,4,2,3,2,5,13,10,12,14,np.NaN,16,12,20,22]}
df = pd.DataFrame(data).reset_index()
print(df)

df2 = df.assign(ewm=df['val'].ewm(alpha=0.3).mean())

import matplotlib
import matplotlib.pyplot as plt
ax = df.plot(kind='bar',x='index',y='val')
ax2 = df2.plot(kind='line', x='index', y='ewm', color='red', ax=ax)
plt.show()

#alpha
df2 = df.assign(ewm_a_low=df['val'].ewm(alpha=0.1).mean())
df3 = df.assign(ewm_a_high=df['val'].ewm(alpha=0.7).mean())

ax = df.plot(kind='bar',x='index',y='val')
ax2 = df2.plot(kind='line', x='index', y='ewm_a_low', color='blue', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='ewm_a_high', color='red', ax=ax)
plt.show()

#span a=2/(span+1)
df2 = df.assign(span_4 = df['val'].ewm(span=4).mean())
df3 = df.assign(span_8 = df['val'].ewm(span=8).mean())

ax = df.plot(kind='bar',x='index',y='val')
ax2 = df2.plot(kind='line', x='index', y='span_4', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='span_8', color='green', ax=ax)
plt.show()

#com, a=1/(1+com) more come less a
df2 = df.assign(com_2 = df['val'].ewm(com=2).mean())
df3 = df.assign(com_10 = df['val'].ewm(com=10).mean())

ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='com_2', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='com_10', color='green', ax=ax)
plt.show()

#half life a = 1-e^(-ln(2)/halflife)
df2 = df.assign(harf_2 = df['val'].ewm(halflife=2).mean())
df3 = df.assign(harf_5 = df['val'].ewm(halflife=5).mean())

ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='harf_2', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='harf_5', color='green', ax=ax)
plt.show()

#adjust
df2 = df.assign(adj_T = df['val'].ewm(alpha=0.2, adjust=True).mean())
df3 = df.assign(adj_F = df['val'].ewm(alpha=0.2, adjust=False).mean())

ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='adj_T', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='adj_F', color='green', ax=ax)
plt.show()

#ignore NA or not
df2 = df.assign(ignore_NA_T = df['val'].ewm(alpha=0.2, ignore_na=True).mean())
df3 = df.assign(ignore_NA_F = df['val'].ewm(alpha=0.2, ignore_na=False).mean())

ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='ignore_NA_T', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='ignore_NA_F', color='green', ax=ax)
plt.show()

#method
import numba
print(df['val'].ewm(alpha=0.2, method='table').mean(engine='numba')) #not working? why?