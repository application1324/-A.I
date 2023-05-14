#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

data = [
    ['3R', 1510, 7.36],
    ['3SOFT', 1790, 1.65],
    ['ACTS',1185,1.28]
]

index = ['037730', '036360', '005760']
columns = ['종목명', '현재가', '들락률']

df = pd.DataFrame(data=data, index=index, columns=columns)

print(df)


# In[5]:


# 특정 값 가져오기

# 036360 종복의 현재가를 출력하기

#특정한 값을 가져오기 위해 사용되는 속성

#df.iloc[행번호, 열번호]

#df.loc[인덱스, 컬럼명]

print(df.iloc[1,1])
print()

print(df.loc['036360', '현재가'])


# In[9]:


#영역 가져오기

#데이터프레임에서 특정 영역 접근

#특정한 영역을 가져오기 위한 속성

#df.iloc[행번호 리스트, 열번호 리스트] 
#df.loc[인덱스 리스트, 컬럼명 리스트]

print(df.iloc[[0,1],[0,1]])
print()
      
print(df.loc[['037730','036360'],['종목명','현재가']] )

#붙여있는 데이터을 가져올때는
# 아래와 같이 사용 가능

print(df.iloc[0:2,0:2])

#붙여있지 않은 정보을 가져올때는 

print(df.iloc[[0,1],[0,2]])

print(df.loc[['037730','036360'],['종목명','들락률']])




# In[ ]:




