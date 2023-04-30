#!/usr/bin/env python
# coding: utf-8

# In[1]:


#파이썬에는 리스트 튜플 디셔너리 타입이 있다.

#1 리스트 [1, 2, 3] 변경 가능

#2 튜플 (1, 2 ,3) 변경 불가

#3 딕셔너리 {어떠한것: 어떠한것에 지정할 변수} 변수말로 지정한 
#변수가 어떠한 역할을 하는지 알려줌

#4 NdArray
#numpy 안에 ndarray라는 타입이 있다
#ndarry 타입의 배열은 배열에 직접적으로 곱을 하여도
#리스트와 같이 반복되지 않는다.

#Pandas 기본 자료구조
#Pandas는 파이썬 안에 있는 데이터 분석을 위한 라이브러리이다.
#Prandas는 numpy을 기반으로 만들어었다.

#Prandas에 기본 자료구조에는
#1 Series 1차원 데이터을 위한 자료구조
#2 DataFrame 2차원 데이테을 위한 자료구조
#나닌다.

#임포트 방식
#1 from pandas import Series, DataFrame
#pandas라는 라이브러리에서 자료구조 Series와 DataFrame함수을 가져오겠다는 뜻이다.

# Series() DataFrame()으로 표현

#2 import pandas as pd
#pradas라는 라이브러리을 pd로 축약하겠다는 뜻이다.

# pd.Series() pd.DataFrame()표현



# In[4]:


#Series 객체 생성

import pandas as pd

arr = [1,2,3,4]
a = pd.Series(arr)
print(a)

#출력 인덱스을 왼쪽에 출력하고
#지정한 정보을 오른쪽에 출력한다.
#내부적을 표현되지는 않지만 행번호라는것도 있다.


# In[5]:


#인덱스 지정하기

data = [100,200,300]
index = ["월","화","수"]

#인덱스 지정하는 방법
#위와 같은 방식을 인덱스을 지정할 수있다.

s = Series(arr ,index)
#Series[출력할 값,인덱스로 지정할 값]
print(s)

#명시적인 인덱스을 알고있다면 인덱스을 쓰는것이 편하고
#알고있지 않다면 행 번호을 쓰는것이 편하다

#행 번호는 딕셔너리의 키와 같이 것으로 인덱스와 같이 지원하는것이
#Pandas의 특징이라 할수있다.


# In[6]:


#Series 속성

#속성 지정하기
#Series자료구조로 바꾼정보을 저정한 변수의 이름.Series 속성

print(s.index) #인덱스을 알려주는 속성

#지정한 변수을 알려주는 속성이다.
print(s.values) 
print(s.array) 


# In[7]:


#연습문제
#Series타입으로 만들기

#import pandas as pd

values = [500,800,200]
index = ["메로나","누가바","빠빠코"]

s = pd.Series(values, index)
print(s)


# In[ ]:




