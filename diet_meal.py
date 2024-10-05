import streamlit as st
st.title("食事　摂取カロリー")
cerbo_options = ["ご飯","パン","うどん"]
mainmeal_options = ["唐揚げ","とんかつ","ハンバーグ","焼き鳥","生姜焼き"]
sidemeal_options = ["サラダ","漬物","カプレーゼ"]

cerbo = st.selectbox("主食の種類を選んでください:", cerbo_options)
mainmeal = st.selectbox("主菜の種類を選んでください", mainmeal_options)
sidemeal = st.selectbox("副菜の種類を選んでください")