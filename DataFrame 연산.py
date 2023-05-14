#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U pyupbit')


# In[2]:


import pyupbit
df = pyupbit.get_ohlcv("KRW-BTC")

df['open']+100


# In[3]:


#데이터프레임 필터링

#boolean값을 가지고 있는 시리즈 객체이다.

조건 = df['close']> df['open']
조건




# In[4]:


df.head(n=2) #n=출력할 행의 수


# In[ ]:


#데이터 프레임 필터링2/2

#맞는 값만 가져오기

cond = df['close'] > ['open']
df[cond]


# In[ ]:


#컬럼 시프트1/2

#동일 컬럼의 값을 빼야할때

#컬럼 시프트 2/2

#동일한 시프트에서 값을 빼야할때 동일한 값을 가지고 있는 동일한 컬럼을 만든다.

#동일한 시프트을 만들때는 df['close_shift1'] = df['close'].shfit(값을 이동시킬 수)로 만든다.

df['close_shift1'] = df['close'].shfit(1)


# In[13]:


df.drop(['volume', 'value'], axis=1, inplace=True)


# In[14]:


df


# In[17]:


df['쉬프트'] = df['close'].shift(1)


# In[18]:


df.head(n=2)


# In[19]:


df['종가변화'] = df['close'] - df['쉬프트']


# In[20]:


df


# In[23]:


df['close'].shift(-1)


# In[24]:


df


# In[ ]:




