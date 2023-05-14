#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Series 1차원
#DataFrame 2차원

#DataFrame도 Series와 같이 행번호라는것있다
#DataFrame은 Series와 다르게 열번호라는것도 있다.

import pandas as pd

data=[
    [157000, 39.88, 4.38],
    [51300, 8.52, 1.45],
    [68800, 10.03, 0.87],
    [140000, 228.38, 2.16]
]

index = ['NAVER', '삼성전자', 'LG전자', '카카오'] #행번호 보이지 않음
columns = ['종가', 'PER', 'PBR'] #열번호 보이지 않음
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)


# In[5]:


#칼럼 선택

#칼럼이란 데이터의 열을 의미한다.

#칼럼은 1차원 데이터이기 때문에 Series로 저장된다.

print(df['종가'])
print()

print(df['PER'])
print()

print(df['PBR'])



# In[6]:


#멀티 컴럼 선택

#2차원 데이터이기 때문에 DataFrame으로 저장이된다.

#여러개의 정보을 가져올떄는 배열의 형식으로 가져와야한다.
df[['PER','PBR']]



# In[10]:


#로우 선택(1/2)

#[] = 컬럼

#가로의 정보 가져오기


#속성
#loc 인덱스로 정보 가져오기

#iloc 행번호로 정보 가져오기

print(df.iloc[1]) #행번호
print()

print(df.loc['삼성전자']) #인덱스




# In[11]:


#멀티 로우 선택

print(df.iloc[[1,2]])
print()

print(df.loc[['삼성전자', 'LG전자']])


# In[15]:


#로우 슬라이싱

#슬라이싱이란 시작에서 끝까지의 정보을 가져오는것을 뜻함

print(df.iloc[0:2]) #0에서 1까지의 행번호의 정보을 가져옴
# 주의 마지막의 정보는 가져오지 않음
print()

print(df.loc['NAVER': '삼성전자']) #지정한 정보의 마지막을 가져옴



# In[ ]:




