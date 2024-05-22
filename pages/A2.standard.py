import streamlit as st
import json

# タイトル
def title():
    # トレーニングメニュー名の入力
    st.title("スタンダート")

# json生成
def show_json():
    # モードの設定（固定）
    mode = "Standard"

    # トレーニングメニュー名の入力
    st.markdown("## A.トレーニングメニュー名")
    training_name = st.text_input("トレーニングメニュー名 *")

    # 数値の選択肢を定義
    number_options = list(range(10))
    delay_options = ["0.1", "0.3", "0.5", "0.8", "1", "1.5", "2", "3", "4", "5", "6", "8", "10"]
    timeout_options = ["✖️", "0.4", "0.6", "0.8", "1", "1.2", "1.5", "2", "3", "4", "5", "6", "7", "8", "9", "10", "20", "30"]
    boolean_options = [True, False]
    color_options = list(range(33))  # 0から32までの選択肢

    # 設定項目の選択
    st.markdown("## B.設定項目")
    color_num_index = st.selectbox("色(color_num_index)", options=number_options, key="color_num_index")
    target_num_index = st.selectbox("ターゲット数(target_num_index)", options=number_options, key="target_num_index")
    delay_index = st.selectbox("次の点灯までの時間(最短)(delay_index)", options=delay_options, key="delay_index")
    delay2_index = st.selectbox("次の点灯までの時間(最長)(delay2_index)", options=delay_options, key="delay2_index")
    timeout_index = st.selectbox("タイムアウト(timeout_index)", options=timeout_options, key="timeout_index")
    onbeeper_index = st.selectbox("消灯音(onbeeper_index)", options=boolean_options, format_func=lambda x: "on" if x else "off", key="onbeeper_index")
    offbeeper_index = st.selectbox("反応音(offbeeper_index)", options=boolean_options, format_func=lambda x: "on" if x else "off", key="offbeeper_index")
    flash_index = st.selectbox("センサー(flash_index)", options=boolean_options, format_func=lambda x: "on" if x else "off", key="flash_index")
    sense_index = st.selectbox("点滅(sense_index)", options=number_options, key="sense_index")
    train_time_index = st.selectbox("xxx(train_time_index)", options=number_options, key="train_time_index")
    colors = st.selectbox("使用する色？(colors)", options=color_options, key="colors")
    start_delay_index = st.selectbox("スタート遅延(start_delay_index)", options=delay_options, key="start_delay_index")
    ending_index = st.selectbox("xxx(ending_index)", options=number_options, key="ending_index")
    cycles_index = st.selectbox("xxx(cycles_index)", options=number_options, key="cycles_index")
    show_graphic = st.selectbox("xxx(show_graphic)", options=boolean_options, format_func=lambda x: "True" if x else "False", key="show_graphic")

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

        if valid_input:
            # 入力データをJSON形式に変換
            data = {
                "mode": mode,
                "name": training_name,
                "prefer": {
                    "color_num_index": color_num_index,
                    "target_num_index": target_num_index,
                    "delay_index": delay_index,
                    "delay2_index": delay2_index,
                    "timeout_index": timeout_index,
                    "onbeeper_index": onbeeper_index,
                    "offbeeper_index": offbeeper_index,
                    "flash_index": flash_index,
                    "sense_index": sense_index,
                    "train_time_index": train_time_index,
                    "colors": colors,
                    "start_delay_index": start_delay_index,
                    "ending_index": ending_index,
                    "cycles_index": cycles_index,
                    "show_graphic": show_graphic
                }
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

    ```json
    "mode": "Standard",
    "name": "スタンダート",
    "prefer": {
      "color_num_index": 0, // 色の数
      "target_num_index": 0, // ターゲット数
      "delay_index": 2, // 次の点灯までの時間(最短)
      "delay2_index": 2, // 次の点灯までの時間(最長)
      "timeout_index": 0, // タイムアウト
      "onbeeper_index": 1, // 消灯音
      "offbeeper_index": 0, // 反応音
      "flash_index": 0, // センサー
      "sense_index": 0, // 点滅
      "train_time_index": 3, // トレーニング時間
      "colors": 32, // 使用する色
      "start_delay_index": 1, // スタート遅延
      "ending_index": 0, // 終了
      "cycles_index": 3, // サイクル
      "show_graphic": false // グラフィック表示
      }
    }
    ```

    """)


title()
show_specification()
show_json()