import streamlit as st
from pages import manual, specification, settings
import os
from urllib.parse import urlencode

# URLパスを解析してページを決定
path = os.getenv("PATH_INFO", "/")
if path.startswith("/"):
    page = "仕様書"
elif path.startswith("/manual"):
    page = "マニュアル"
elif path.startswith("/allinonce"):
    page = "同時点灯"
elif path.startswith("/standard"):
    page = "スタンダート"
elif path.startswith("/multistandard"):
    page = "2人"
elif path.startswith("/specification"):
    page = "仕様書"
elif path.startswith("/settings"):
    page = "設定"


# ページの設定
# pages = {
#     "トレーニングメニュー作成": manual.show,
#     "仕様書": specification.show,
#     "設定": settings.show
# }

# サイドバーにページ選択のメニューを追加
# selection = st.sidebar.selectbox("ページ選択", list(pages.keys()), index=list(pages.keys()).index(page))

# URLのクエリパラメータを設定
params = st.experimental_get_query_params()
if params.get('page', [None])[0] != selection:
    params['page'] = selection
    st.experimental_set_query_params(**params)
    st.experimental_rerun()

# 選択されたページを表示
pages[selection]()
