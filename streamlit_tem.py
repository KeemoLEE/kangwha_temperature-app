#!/usr/bin/env python
# coding: utf-8

# In[21]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정 (matplotlib에서 한글 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 파일 불러오기 (CP949 인코딩 명시)
data = pd.read_csv('Kangwha.csv', encoding='cp949')
data.columns = data.columns.str.strip()  # 열 이름 공백 제거
data['날짜'] = pd.to_datetime(data['날짜'], errors='coerce')  # 날짜 형식으로 변환 (오류는 NaT 처리)
data = data.dropna(subset=['날짜'])  # 날짜가 없는 행 제거

# 열 이름 변경: '평균기온(°C)' -> '평균기온'
data.rename(columns={'평균기온(°C)': '평균기온'}, inplace=True)

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




