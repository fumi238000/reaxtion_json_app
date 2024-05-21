import streamlit as st
import json

def show():
    # タイトルの設定
    st.title("2人プレイ")

    # トレーニングメニュー名の入力
    st.markdown("## A.トレーニングメニュー名")
    training_name = st.text_input("トレーニングメニュー名 *")

    # B.ターゲット設定のタイトル
    st.markdown("## B.ターゲット設定")

    # プログラムの入力
    program = []
    program_titles = ["B-1. 開く", "B-2. 待つ", "B-3. 次の点灯までの時間", "B-4. 閉じる"]
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

    for i in range(4):
        st.markdown(f"<div style='border: 2px solid #000;'>", unsafe_allow_html=True)
        st.markdown(f"##### {program_titles[i]}")
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
            # TODO: 以下true or falseで設定すること
            # TODO: 以下文言を設定すること
            logic = st.number_input(f"ロジック設定 (key: logic)", min_value=0, key=f"logic_{i}")
            # TODO: falseの場合は、以下の設定が不要のため非表示とする
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

    # 制限時間のタイトルと設定
    st.subheader("C.制限時間の設定")
    limit_time = st.selectbox("制限時間 *", options=limit_time_options, key="limit_time")

    # 変換ボタンの設定
    if st.button("変換"):
        # バリデーションのチェック
        validation_errors = []
        valid_input = True

        if len(training_name) == 0:
            validation_errors.append("トレーニングメニュー名は必須です")
            valid_input = False
        elif len(training_name) > 50:
            validation_errors.append("トレーニングメニュー名は50文字以内で入力してください")
            valid_input = False

        if any('colors' in step and len(step['colors']) == 0 for step in program):
            validation_errors.append("色は必ず1つ以上選択してください")
            valid_input = False

        if valid_input:
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
        else:
            for error in validation_errors:
                st.error(error)

show()
