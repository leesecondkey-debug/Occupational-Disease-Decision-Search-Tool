import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("718mbdata.csv", encoding='utf-8-sig')

df = load_data()

st.title("업무상질병 판정서 검색기")

# 1. 필터 옵션 구성 (중복 제거 및 정렬)
job_list = ["전체"] + sorted(df['Occupation'].dropna().unique().tolist())
disease_list = ["전체"] + sorted(df['Disease Name'].dropna().unique().tolist())
status_list = ["전체"] + sorted(df['Approval Status'].dropna().unique().tolist())

# 2. 검색 필터 창 (첫 페이지 상단)
st.subheader("조건별 검색")
col1, col2, col3 = st.columns(3)

with col1:
    selected_job = st.selectbox("직종 선택:", job_list)
with col2:
    selected_disease = st.selectbox("질병 선택:", disease_list)
with col3:
    selected_status = st.selectbox("승인 상태 선택:", status_list)

# 3. 실시간 필터링 로직
filtered_df = df.copy()

if selected_job != "전체":
    filtered_df = filtered_df[filtered_df['Occupation'] == selected_job]
if selected_disease != "전체":
    filtered_df = filtered_df[filtered_df['Disease Name'] == selected_disease]
if selected_status != "전체":
    filtered_df = filtered_df[filtered_df['Approval Status'] == selected_status]

# 4. 결과 표시
st.write(f"### 📊 검색 결과: 총 {len(filtered_df)}건")
st.dataframe(filtered_df, use_container_width=True)

# 5. 통계 기능 (결과가 있을 때만)
if len(filtered_df) > 0:
    st.write("---")
    st.subheader("선택한 조건의 통계")
    st.bar_chart(filtered_df['Occupation'].value_counts())

    import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # 여기서 ID 부분에 공유해주신 ID를 넣었습니다.
    file_id = "1ZOkkNtv4k-7Chh17I5iuysd2Eewk8ahx"
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url, encoding='utf-8-sig')

# 앱 실행
df = load_data()
st.write("데이터가 성공적으로 로드되었습니다!")
st.dataframe(df) # 데이터프레임 보여주기
