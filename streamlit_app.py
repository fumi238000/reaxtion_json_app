import streamlit as st
from pages import training_menu, specification

# ページの設定
pages = {
    "トレーニングメニュー作成": training_menu.show,
    "仕様書": specification.show
}

# サイドバーにページ選択のメニューを追加
page = st.sidebar.selectbox("ページ選択", list(pages.keys()))

# 選択されたページを表示
pages[page]()
