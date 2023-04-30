#!/usr/bin/env python
# coding: utf-8

# In[1]:


#행번호을 가지고 인덱싱하는법

#iloc[행번호]속성

import pandas as pd
data = [100,200,300]
index = ["월","화","수"]
s = pd.Series(data, index)
print(s.iloc[0])
#지정한 행번호을 가지고 데이터을 출력하는 속성이다.
print(s.iloc[2])

print(s.iloc[-1])
#-1은 마지막 데이터을 뜻하는 숫자이다.


# In[3]:


#인덱스을 가지고 인덱싱하는법

#loc[인덱스]속성

print(s.loc["화"])
print(s.loc["월"])

print(s["화"])
print(s[2])
#기본적으로 []에 
#인덱스 또는 행번호을 입력한다면 그에 해당하는 정보을 가져올수있다.





# In[6]:


#행번호을 사용한 슬아이싱(범위)
#연속적인 여러개의 값을 출력함

print(s.iloc[0:2])
#끝 불포함(행 번호)
print(s.loc["월":"수"])
#끝 포함(인덱스)


# In[7]:


# 여러값 인덱싱
#연속적이지 않은 여러개의 값의 출력함

target = [0, 2]
target1 = ["월", "수"]
#이것은 범위처럼 어디에서 어디까지가 아니라 지정한 값만 출력함

print(s.iloc[target])
print(s.loc[target1])


# In[ ]:




