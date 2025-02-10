from managers import Database, Specific_manager
import streamlit as st

# --Managers--

db = Database()
specific_manager = Specific_manager(db)

# --Properties--

countries_list = specific_manager.get_countries()
mbti_list = specific_manager.get_mbti()

# --UI--

st.title("특정 나라의 MBTI 비율 확인")
st.sidebar.markdown("Check out MBTI of countries!")

country = st.selectbox("나라", countries_list)
mbti = st.selectbox("MBTI 유형", mbti_list)

is_tapped_check_button = st.button("확인")

# --Logic--

if is_tapped_check_button:
    if country and mbti:
        try:
           data = specific_manager.get_specific_data(country=country, mbti=mbti)
           st.success(data)
        except Exception as e:
            st.error("시스템 에러가 발생했습니다.")
            st.error(f'error message: {str(e)}')

db.close_connection()
