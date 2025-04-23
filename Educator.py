#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# In[2]:


# CSV 파일 불러오기 (CP949 인코딩 명시)
data = pd.read_csv('Kangwha.csv', encoding='cp949')

data


# In[3]:


# 생략가능
data.columns = data.columns.str.strip()  # 열 이름 공백 제거
print(data.columns)


# In[4]:


# 날짜가 없는 행 제거
data = data.dropna(subset=['날짜'])  # 날짜가 없는 행 제거
data


# In[5]:


# 각 컬럼의 데이터형태를 확인한다.(생략가능)
for column in data.columns:
    print(f"열 이름: {column}")
    print(f"데이터 타입: {data[column].dtype}")
    print(f"예시 데이터 (상위 5개):\n{data[column].head()}\n")


# In[6]:


data['날짜'] = pd.to_datetime(data['날짜'], errors='coerce')  # 날짜 형식으로 변환 (오류는 NaT 처리)
print(data['날짜'].dtype)


# ## Streamlit

# In[7]:


# Streamlit 앱 제목
st.title('인천 강화 기온 분석')
# 날짜 범위 슬라이더 설정
min_date = data['날짜'].min().date()
max_date = data['날짜'].max().date()

# 사용자로부터 날짜 범위 입력 받기
start_date, end_date = st.slider('기간을 선택하세요:',
                                  min_value=min_date,
                                  max_value=max_date,
                                  value=(min_date, max_date),
                                  format="YYYY-MM-DD")

# 선택된 기간의 데이터 필터링
filtered_data = data[(data['날짜'] >= pd.to_datetime(start_date)) &
                     (data['날짜'] <= pd.to_datetime(end_date))]
filtered_data

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(filtered_data['날짜'], filtered_data['평균기온'], label='평균기온')
ax.set_xlabel('날짜')
ax.set_ylabel('기온 (°C)')
ax.set_title('선택 기간의 평균 기온')
ax.legend()
ax.grid(True)

# Streamlit에 그래프 출력
st.pyplot(fig)

# 데이터 테이블 출력 옵션
if st.checkbox('데이터 테이블 보기'):
    st.dataframe(filtered_data)  # 필터된 데이터 표시


# In[ ]:





# In[ ]:





# ## 그래프 그리기(맷플롯립)

# In[ ]:




