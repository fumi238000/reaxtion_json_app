# ベースイメージとしてPythonを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なライブラリをインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# Streamlitのデフォルトポートを開放
EXPOSE 8501

# コンテナ起動時に実行するコマンド
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]
