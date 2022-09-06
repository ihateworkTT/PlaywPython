import pandas as pd
import numpy as np

##03-01 apply
#DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)

#make example data
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data, row, col)

#fun, if possible, by column
print(df.apply(np.sqrt))
print(df.apply(np.sum))

#axis = 0, index (row)
#axis = 1, columns
print(df.apply(np.prod, axis=0))
print(df.apply(np.prod, axis=1))

#result type
print(df.apply(lambda x: [1,2,3]))

print(df.apply(lambda x: [1,2,3], axis=1, result_type='expand'))
print(df.apply(lambda x: [1,2,3], axis=1, result_type='reduce'))
print(df.apply(lambda x: [1,2,3], axis=1, result_type='broadcast'))

##03-02 applymap
#DataFrame.apply(func, na_action=None, **kwargs)
data = [[1,2,3],[4,5,6],[7,pd.NA,9]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

print(df.applymap(lambda x: x**2, na_action='ignore'))

##03-03 pipe
#DataFrame.pipe(func, args, kwargs)
#sample data
org_data = pd.DataFrame({'info':['삼성전자/3/70000','SK하이닉스/2/100000']})
print(org_data)

#devide stock name, quantity, price
def code_name(data):
    result=pd.DataFrame(columns=['name','count','price']) 
    df = pd.DataFrame(list(data['info'].str.split('/'))) # '/ ' 로 구분하여 문자열을 나누어 리스트에 넣음
    result['name'] = df[0] # 여기엔 첫번째 값인 이름이 입력
    result['count']= df[1] # 여기엔 두번째 값인 수량이 입력
    result['price']= df[2] # 여기엔 세번째 값인 가격이 입력
    result = result.astype({'count':int,'price':int}) # count와 price를 int로 바꿈(기존str)
    return result
a = code_name(org_data)
print(a)

#add unit
def value_cal(data,unit=''):
    result = pd.DataFrame(columns=['name','value']) 
    result['name'] =data['name'] # 이름은 기존거를 가져옴
    result['value']=data['count']*data['price'] # value는 count * price를 입력함
    result = result.astype({'value':str}) # value를 str로 변경(단위를 붙이기 위함)
    result['value']=result['value']+unit # 단위를 붙임
    return(result)
a1 = value_cal(a, '원')
print(a1)

#without pipe
print(value_cal(code_name(org_data),'Won'))

#with pipe
print(org_data.pipe(code_name).pipe(value_cal, 'Won'))


##03-04 aggregate, agg
#DataFrame.aggregate(func=None, axis=0, args, kwargs)
#DataFrame.agg(func=None, axis=0, args, kwargs)

df = pd.DataFrame([[1,4,7],[2,5,8],[3,6,9]])
print(df)

#fun -> np
ex1 = df.agg(np.prod)
print(ex1)

# fun -> str
ex2 = df.agg('prod')
print(ex2)

#def 
ex3 = df.agg([lambda x: min(x) * max(x)])
print(ex3)

#column name = function name
def func_sub(input):
	return max(input) - min(input)
ex4 = df.agg([func_sub, 'sum', 'mean'])
print(ex4)

#set name
func_sub.__name__='my function'
ex5 = df.agg([func_sub, 'sum'])
print(ex5)

#apply multiple function by list or dictionary
ex6 = df.agg(['min','max','sum','prod'])
print(ex6)
ex7 = df.agg({2:'sum', 0:'max', 1:'min'})
print(ex7)
ex8 = df.agg({0:['sum','prod'], 1:['min','max'], 2:'mean'})
print(ex8)

#axis
ex2_1 = df.agg('prod',axis=0)
ex2_2 = df.agg('prod',axis=1)
print(ex2_1, '\n', '-'*10, '\n', ex2_2)

##03-05 transform
#DataFrame.transform(func, axis=0, args, kwargs)
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data=[[10,40,70],[20,50,80],[30,60,90]],index=row,columns=col)
print(df)

#by form of function
ex1 = df.transform(np.sqrt)
print(ex1)

ex2 = df.transform('sqrt')
print(ex2)

ex3 = df.transform(lambda a: np.sqrt(a))
print(ex3)

ex4 = df.transform(['exp', 'sqrt'])
print(ex4)

ex5 = df.transform({'col2':'exp', 'col1':'sqrt'})
print(ex5)

##03-06 string
#DataFrame.eval(expr, inplace=False, kwargs)
data = [[1,2,3],[4,5,6],[7,8,9]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data = data, index = row, columns= col)
print(df)

print(df.eval('col4 = col1*col2 - col3'))

#original copy is?
print(df.eval('col4 = col1*col2 - col3', inplace=True))
print(df)