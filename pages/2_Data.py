from managers import Database, Data_manager
import streamlit as st

# --Managers--

db = Database()
data_manager = Data_manager(db)

# --Properties--

table = data_manager.get_table()

# --UI--

st.title("모든 데이터 조회")
st.sidebar.markdown("All Data")
st.dataframe(table)

# --Logic--

db.close_connection()
