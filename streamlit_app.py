import streamlit as st
import json

# タイトルの設定
st.title("REAXTIONトレーニングメニュー作成画面")

# トレーニングメニュー名の入力
training_name = st.text_input("トレーニングメニュー名")

# プログラムの入力
program = []
program_titles = ["1.点灯設定", "2.待機", "3.次の点灯までの時間", "4.閉じる"]
for i in range(4):
    st.markdown(f"<div style='border: 2px solid #000; padding: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
    st.subheader(program_titles[i])
    order = i
    numbers = st.number_input(f"ターゲット数または回数 (key: numbers)", min_value=1, max_value=3, step=1, key=f"numbers_{i}")
    
    if i == 0:
        random = st.selectbox(f"ランダム設定 (key: random)", options=[0, 1], format_func=lambda x: "オフ" if x == 0 else "オン", key=f"random_{i}")
        colors = st.selectbox(f"色設定 (key: colors)", options=list(range(6)), key=f"colors_{i}")
        onbeeper = st.selectbox(f"点灯音 (key: onbeeper)", options=[0, 1], format_func=lambda x: "オフ" if x == 0 else "オン", key=f"onbeeper_{i}")
        offbeeper = st.selectbox(f"反応音 (key: offbeeper)", options=[0, 1], format_func=lambda x: "オフ" if x == 0 else "オン", key=f"offbeeper_{i}")
        sensor = st.selectbox(f"センサー設定 (key: sensor)", options=[0, 1, 2, 3], format_func=lambda x: ["センサー(近距離)", "センサー(遠距離)", "タッチ(敏感)", "タッチ(鈍感)"][x], key=f"sensor_{i}")
        flash = st.selectbox(f"点灯設定 (key: flash)", options=[0, 1], format_func=lambda x: "オフ" if x == 0 else "オン", key=f"flash_{i}")
        
        program.append({
            "order": order,
            "numbers": numbers,
            "random": random,
            "colors": colors,
            "onbeeper": onbeeper,
            "offbeeper": offbeeper,
            "sensor": sensor,
            "flash": flash
        })
    
    elif i == 1:
        logic = st.number_input(f"ロジック設定 (key: logic)", min_value=0, key=f"logic_{i}")
        timeout = st.text_input(f"タイムアウト設定 (key: timeout)", key=f"timeout_{i}")
        
        program.append({
            "order": order,
            "numbers": numbers,
            "logic": logic,
            "timeout": timeout
        })
    
    elif i == 2:
        delay1 = st.text_input(f"スタート遅延 (key: delay1)", key=f"delay1_{i}")
        delay2 = st.text_input(f"次の点灯までの時間 (key: delay2)", key=f"delay2_{i}")
        
        program.append({
            "order": order,
            "delay1": delay1,
            "delay2": delay2
        })
    
    elif i == 3:
        random = st.selectbox(f"ランダム設定 (key: random)", options=[0, 1], format_func=lambda x: "オフ" if x == 0 else "オン", key=f"random_{i}")
        
        program.append({
            "order": order,
            "numbers": numbers,
            "random": random
        })
    st.markdown("</div>", unsafe_allow_html=True)

# 制限時間の設定
limit_time = st.text_input("制限時間 (key: limit_time)", value="∞")

# 変換ボタンの設定
if st.button("変換"):
    # 入力データをJSON形式に変換
    data = {
        "name": training_name,
        "program": program,
        "limit_time": limit_time
    }
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    
    # 結果を表示
    st.subheader("変換結果")
    st.code(json_data, language="json")
