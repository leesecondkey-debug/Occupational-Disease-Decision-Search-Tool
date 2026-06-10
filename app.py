import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# 1. 구글 드라이브에서 데이터를 가져오는 함수 (통합)
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?id=1ZOkkNtv4k-7Chh17I5iuysd2Eewk8ahx"
    return pd.read_csv(url, encoding='utf-8-sig')

# 2. 데이터 로드
try:
    df = load_data()
except Exception as e:
    st.error(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")
    st.stop()

# 3. 앱 화면 구성
st.title("업무상질병 판정서 검색기")

# 필터 옵션 구성 (중복 제거 및 정렬)
job_list = ["전체"] + sorted(df['Occupation'].dropna().unique().tolist())
disease_list = ["전체"] + sorted(df['Disease Name'].dropna().unique().tolist())
status_list = ["전체"] + sorted(df['Approval Status'].dropna().unique().tolist())

# 검색 필터 창
st.subheader("조건별 검색")
col1, col2, col3 = st.columns(3)

with col1:
    selected_job = st.selectbox("직종 선택:", job_list)
with col2:
    selected_disease = st.selectbox("질병 선택:", disease_list)
with col3:
    selected_status = st.selectbox("승인 상태 선택:", status_list)

# 실시간 필터링 로직
filtered_df = df.copy()

if selected_job != "전체":
    filtered_df = filtered_df[filtered_df['Occupation'] == selected_job]
if selected_disease != "전체":
    filtered_df = filtered_df[filtered_df['Disease Name'] == selected_disease]
if selected_status != "전체":
    filtered_df = filtered_df[filtered_df['Approval Status'] == selected_status]

# 결과 표시
st.write(f"### 📊 검색 결과: 총 {len(filtered_df)}건")
st.dataframe(filtered_df, use_container_width=True)

# 통계 기능
if len(filtered_df) > 0:
    st.write("---")
    st.subheader("선택한 조건의 직종별 통계")
    st.bar_chart(filtered_df['Occupation'].value_counts())
