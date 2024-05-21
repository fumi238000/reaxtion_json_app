import streamlit as st
import json

# タイトルの設定
st.title("REAXTIONトレーニングメニュー作成画面")

# トレーニングメニュー名の入力
training_name = st.text_input("トレーニングメニュー名 *")

# トレーニングメニュー名のバリデーション
if len(training_name) == 0:
    st.error("トレーニングメニュー名は必須です")
elif len(training_name) > 50:
    st.error("トレーニングメニュー名は50文字以内で入力してください")

# プログラムの入力
program = []
program_titles = ["1.開く", "2.待つ", "3.次の点灯まで", "4.閉じる"]
numbers_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "all"]
timeout_options = ["✖️", "0.4", "0.6", "0.8", "1", "1.2", "1.5", "2", "3", "4", "5", "6", "7", "8", "9", "10", "20", "30"]
delay1_options = ["0", "3", "5", "10"]
delay2_options = ["0.1", "0.3", "0.5", "0.8", "1", "1.5", "2", "3", "4", "5", "6", "8", "10"]
limit_time_options = ["∞", "10s", "15s", "30s", "45s", "1min.", "2min.", "3min.", "5min.", "10min."]
colors_options = {
    0: "赤",
    1: "青",
    2: "緑",
    3: "黄",
    4: "紫",
    5: "オレンジ"
}

valid_input = len(training_name) > 0 and len(training_name) <= 50

for i in range(4):
    st.markdown(f"<div style='border: 2px solid #000; padding: 10px; margin: 10px 0;'>", unsafe_allow_html=True)
    st.subheader(program_titles[i])
    order = i
    
    if i == 0 or i == 3:
        numbers = st.selectbox(f"ターゲット数または回数 (key: numbers)", options=numbers_options, key=f"numbers_{i}")
    
    if i == 0:
        random = st.selectbox(f"ランダム設定 (key: random)", options=[0, 1], format_func=lambda x: "off" if x == 0 else "on", key=f"random_{i}", index=1)
        colors = st.multiselect(
            f"色設定 (key: colors) *", 
            options=list(colors_options.keys()), 
            format_func=lambda x: colors_options[x], 
            key=f"colors_{i}",
            default=list(colors_options.keys())
        )
        if len(colors) == 0:
            st.error("色は必ず1つ以上選択してください")
            valid_input = False
        onbeeper = st.selectbox(f"点灯音 (key: onbeeper)", options=[0, 1], format_func=lambda x: "off" if x == 0 else "on", key=f"onbeeper_{i}", index=1)
        offbeeper = st.selectbox(f"反応音 (key: offbeeper)", options=[0, 1], format_func=lambda x: "off" if x == 0 else "on", key=f"offbeeper_{i}", index=1)
        sensor = st.selectbox(f"センサー設定 (key: sensor)", options=[0, 1, 2, 3], format_func=lambda x: ["センサー(近距離)", "センサー(遠距離)", "タッチ(敏感)", "タッチ(鈍感)"][x], key=f"sensor_{i}")
        flash = st.selectbox(f"点灯設定 (key: flash)", options=[0, 1], format_func=lambda x: "off" if x == 0 else "on", key=f"flash_{i}", index=1)
        
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
        timeout = st.selectbox(f"タイムアウト設定 (key: timeout)", options=timeout_options, key=f"timeout_{i}")
        
        program.append({
            "order": order,
            "logic": logic,
            "timeout": timeout
        })
    
    elif i == 2:
        delay1 = st.selectbox(f"最短 (key: delay1)", options=delay1_options, key=f"delay1_{i}")
        delay2 = st.selectbox(f"最長 (key: delay2)", options=delay2_options, key=f"delay2_{i}")
        
        program.append({
            "order": order,
            "delay1": delay1,
            "delay2": delay2
        })
    
    elif i == 3:
        random = st.selectbox(f"ランダム設定 (key: random)", options=[0, 1], format_func=lambda x: "off" if x == 0 else "on", key=f"random_{i}", index=1)
        
        program.append({
            "order": order,
            "numbers": numbers,
            "random": random
        })
    st.markdown("</div>", unsafe_allow_html=True)

# 制限時間の設定
limit_time = st.selectbox("制限時間 (key: limit_time)", options=limit_time_options, key="limit_time")

# 変換ボタンの設定
if st.button("変換") and valid_input:
    # 入力データをJSON形式に変換
    data = {
        "name": training_name,
        "program": program,
        "limit_time": limit_time
    }
    json_data = json.dumps(data, ensure_ascii=False, indent=2)

    # 結果を表示
    st.subheader("変換結果")
    st.code(f'Coding:{json_data}', language="json")
