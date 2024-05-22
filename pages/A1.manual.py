import streamlit as st
import json

def title():
    # トレーニングメニュー名の入力
    st.markdown("## マニュアル問題")

# jsonを生成する処理
def show_manual():
    # タイトルの設定
    st.title("json生成")

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

# 仕様書
def show_specification():
    # 仕様書ページの内容
    st.title("仕様書")
    st.write("""
    ### 構成

    - 以下の4つで構成されています。1~4を順番に実行することで、Reaxtionは動作しています。

    ```json
    Coding:{
      "name": "test", // トレーニングメニュー名
      "program": [
        {
          "order": 0, // 1.開く
        },
        {
          "order": 1, // 2.待つ
        },
        {
          "order": 2, // 3.次の点灯までの時間
        },
        {
          "order": 3, // 4.閉じる
        }
      ],
      "limit_time": "∞" // 制限時間
    }
    ```

    ### A. 順番に消す

    #### *1.開く*

    - ターゲットを点灯させる設定を行う。

    ```shell
    - numbers: ターゲット数または回数 (1~12, all)
    - random: ランダム設定 (0: off, 1: on)
    - colors: 色設定 (0: 赤, 1: 青, 2: 緑, 3: 黄, 4: 紫, 5: オレンジ)
    - onbeeper: 点灯音 (0: off, 1: on)
    - offbeeper: 反応音 (0: off, 1: on)
    - sensor: センサー設定 (0: センサー(近距離), 1: センサー(遠距離), 2: タッチ(敏感), 3: タッチ(鈍感))
    - flash: 点灯設定 (0: off, 1: on)
    ```

    #### *2.待つ*

    - ターゲットが点灯してから消灯するまでの時間を設定できる

    ```shell
    - logic: ロジック設定(時間設定の有効化) (0: off, 1: on)
    - timeout: タイムアウト設定 (✖️, 0.4~30秒)
    ```

    #### *3.次の点灯までの時間*

    - ユーザーが消したあと、次の点灯までの時間を設定する。
    - 最小値から最大値までのランダムな時間を設定することもできる。

    ```shell
    - delay1: 最短 (0, 3, 5, 10秒)
    - delay2: 最長 (0.1~10秒)
    ```

    #### *4.閉じる*

    - ターゲットを消灯させる設定を行う。

    ```
    - numbers: ターゲット数または回数 (1~12, all)
    - random: ランダム設定(???) (0: off, 1: on)
    ```

    ### 制限時間

    - トレーニングの制限時間を設定する。

    ```
    - limit_time: 制限時間 (∞, 10秒~10分)
    ```

    """)

title()
show_specification()
show_manual()