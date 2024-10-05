import streamlit as st
st.title("食事　摂取カロリー")
cerbo_options = ["ご飯","パン","うどん"]
mainmeal_options = ["卵焼き","納豆","焼き魚(鮭)","ハンバーグ"]
submeal_options = ["サラダ","味噌汁"]
sidemenu_options = ["牛乳200ml","ヨーグルト1パック","みかん","りんご"]

cerbo = st.selectbox("主食の種類を選んでください:", cerbo_options)
mainmeal = st.selectbox("主菜の種類を選んでください", mainmeal_options)
submeal = st.selectbox("副菜の種類を選んでください")