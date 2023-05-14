#!/usr/bin/env python
# coding: utf-8

# In[45]:


get_ipython().system('pip install -U pyupbit')


# In[51]:


import pyupbit

df = pyupbit.get_ohlcv('KRW-BTC') #pyupbit.의 속성인 get-ohlcv('원하는 코인의 이름')으로 사용하고 코인의 정보을 가져올수있다.


# In[52]:


df.head() # 앞의 5개의 정보만을 보여줌


# In[53]:


#컬럼 추가

df['range']=df['high']-df['low'] #상위와 하위의 정보을 서로 빼서 새로운 정보을 만드는것임
df.head()


# In[54]:


29238000.0-28530000.0


# In[41]:


#컬럼 삭제

#df.drop('컬럼명', axis=1(어떠한 축인지 알려주는 역할을 가짐))

#value 삭제

df.drop('value', axis=1)
#새로운 객체을 만들어서 value라는 값을 지우고 출력하는것이다.


# In[55]:


df
#예전에 만들어던 객체에는 value라늑 값이 그대로 있는것을 볼수있다.


# In[56]:


#기존의 객체가 삭제할 값을 적용하고 싶다면
df.drop('open', axis=1, inplace=True)


# In[57]:


df


# In[60]:


#시계열 데이터와 인덱스

import pandas as pd

date = ['2021-04-09']
index = pd.to_datetime(data)

print(type(date)) #[]으로 했기 때문에 리스트이고
print(type(index)) # list이기 때문에 DatetimeIndex로 타입이 바뀐다.


# In[59]:


date = "2021-04-09"
index = pd.to_datetime(data)

print(type(date)) #""으로 했기 때문에 리스트이고
print(type(index)) # str이기 때문에 Timestamp로 타입이 바뀐다.


# In[65]:


#로우 추가

date = '2022-10-05 9:00:00'
dt = pd.to_datetime(date)


# In[68]:


df.loc[dt]=[100,110,100,100,100,100] #있는 정보의 수을 맞추어야 한다.
df


# In[70]:


df.tail()


# In[71]:


df.index[-1] #마지막의 수을 출력할때는 -1이라고 한다.


# In[73]:


df.drop(df.index[-1], axis=0, inplace=True)


# In[74]:


df


# In[75]:


df.tail


# In[ ]:




