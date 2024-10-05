import database_food

import streamlit as st
import time
# 運動の種類を選択するセレクトボックスを作成
exercise_options_names = [
    walking,running,cycling,yoga,trekking,dance,swimming,   
    strong_strength_training,weak_strength_training,weak_sports,strong_sports]
exercise_options =[
    "ウォーキング", "ランニング", "自転車", "ヨガ", "登山", "ダンス", "水泳",
    "筋トレ（高強度）", "筋トレ（低強度）", "スポーツ", "スポーツ（激しめ）"
]
# タイトルと運動の種類選択
st.title("運動のトラッキングアプリ")
exercise_name = st.selectbox("運動の種類を選んでください:", exercise_options)
for i in range(len(exercise_options)):
    if exercise_name == exercise_options[i]:
        exercise = exercise_options_names[i]
# 運動開始とストップのボタン
start_button = st.button("運動開始！")
stop_button = st.button("ストップ")
# 運動の開始時間を保持する変数
if "start_time" not in st.session_state:
    st.session_state.start_time = None
# 経過時間を表示する変数
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0
# 開始ボタンが押されたときの処理
if start_button:
    st.session_state.start_time = time.time()  # 現在の時間を取得して保存
    st.session_state.elapsed_time = 0          # 経過時間をリセット
    st.write(f"【{exercise_name}】が開始されました！")
# ストップボタンが押されたときの処理
if stop_button and st.session_state.start_time is not None:
    duration = time.time() - st.session_state.start_time
    result = diet.exerciseGo(you,you_user.weight,exercise.calorie,duration)
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.session_state.start_time = None  # ストップしたので開始時間をリセット
    st.write(f"【{exercise_name}】が終了しました。")
    st.write(f"経過時間: {int(st.session_state.elapsed_time // 3600):02}:{int((st.session_state.elapsed_time % 3600) // 60):02}:{int(st.session_state.elapsed_time % 60):02}")
    st.write(f"{int(result)}カロリー消費しました。")
# 運動中の経過時間を表示
if st.session_state.start_time is not None:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.write(f"現在の経過時間: {int(st.session_state.elapsed_time // 3600):02}:{int((st.session_state.elapsed_time % 3600) // 60):02}:{int(st.session_state.elapsed_time % 60):02}")