#!/usr/bin/env python
# coding: utf-8

# In[11]:


#DataFrame 생성 (1/3)

import pandas as pd

#세로 출력
data = {
    "종가" : [157000, 51300, 68800, 1440000],
    "PER" : [39.88, 8.52, 10.03, 228.38],
    "PBR" : [4.38, 1.45, 0.87, 2.16]
}

index = ['NAVER', "삼성전자", 'LG전자', '카카오']

df = pd.DataFrame(data, index)
print(df)


# In[15]:


#가로 출력
data = [
    [157000,39.88,4.38],
    [51300,8.52,1.45],
    [68800,10.03,0.87],
    [140000,228.38,2.16]
]

index = ['NAVER', "삼성전자", 'LG전자', '카카오']
columns = ['종가', 'PER', 'PBR']

df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)


# In[17]:


data = [    
    {"종가":157000,"PER":39.88,"PBR":4.38},    
    {"종가":51300,"PER":8.52,"PBR":1.45},    
    {"종가":68800,"PER":10.03,"PBR":0.87},    
    {"종가":140000,"PER": 228.38,"PBR":2.16}
]

index = ['NAVER', "삼성전자", 'LG전자', '카카오']

df = pd.DataFrame(data=data, index=index)
print(df)


# In[20]:


#연습 문제 
#1. 다음 2차원 데이터를 데이터프레임으로 생성하세요.

data = {
    '시가': [980, 200, 300],
    '고가': [900, 300, 500],
    '저가': [920, 180, 300],
    '종가': [930, 180, 400]
}

index = ['비트코인', '리플', '이더리움']
df = pd.DataFrame(data=data, index=index)
print(df)


# In[ ]:





# In[ ]:




