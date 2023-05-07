#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

#series 값 추가

data = [100, 200, 300]
index = ["월", "화", "수"]
#방법1
s= pd.Series(data, index)

#방법2
#s = pd.Series(data=데이터 정보을 담은 변수이름 index=인덱스 정보을 담은 변수이름)

s.loc["목"] = 400 #값 추가
print(s)


# In[6]:


#series 값 삭제
s1 = s.drop("목")
print(s1)
print(s) #원복은 그대로 있는것이 특징이다.
#(변경한 값이 리턴된 새로운 객체을 가지고 있다.)
s2 = s.drop(["월","화"]) #어려개을 삭제할때는 배열 처럼 삭제함
print(s2)


# In[9]:


#series값 수정
s.iloc[0] = 1000 #행번호을 이용하여 수정
s.loc["수"] = 3000 #인덱스을 이용하여 수정
print(s)
#새로운 객체을 만들지 않고 원복을 수정함


# In[ ]:




