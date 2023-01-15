import streamlit as st
import pandas as pd
import numpy as np

st.title("streamlit 基礎")
st.write("Hello World!")

# データフレームの準備
df = pd.DataFrame({
    "1列目": [1, 2, 3, 4, 5],
    "2列目": [10, 20, 30, 40, 50]
})

# 動的なテーブル
# st.dataframe(df)

# 引数を使用した動的テーブル
# st.dataframe(
#     df.style.highlight_max(axis=0), 
#     width = 100,
#     height=150
#     )

# 静的なテーブル.
# st.table(df)

# 10行3列のデータフレームを準備
df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=["a", "b", "c"]
)

# 折れ線グラフ
st.line_chart(df)

# 面グラフ
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)

# プロットする乱数をデータフレームで用意
df_map = pd.DataFrame(
    np.random.rand(100,2) / [10, 10] + [35.69, 139.70],
    columns = ["latitude", "longitude"]
)

# マップをプロット
st.map(df_map)

# Pillow 画像の読み込み
from PIL import Image

# 画像の読み込み
# img = Image.open("iris.jpg")
# st.image(img,caption = "Iris", use_column_width=True)

# チェックボックス
if st.checkbox("show Image"):
    img = Image.open("iris.jpg")
    st.image(img,caption = "Iris", use_column_width=True)

# セレクトボックス
option = st.selectbox(
    "好きな数字を入力してください。",
    list(range(1, 11))
)

# テキスト入力による値の動的変更
text = st.text_input("あなたの好きなスポーツを教えてください")
"あなたの好きなスポーツ：", text

# スライダーによる値の動的変更
condition = st.slider("あなたの今の調子は？", 0, 100, 25)
"コンディション:", condition

"あなたの好きな数字は", option, "です。"
"""
# unchiunchi
## unchiunchi
### unchiunchi
#### unchiunchi
- unchiunchi
- unchiunchi
1. unchiunchi
2. unchiunchi
3. unchiunchi

> unchiunchi

`Hello, unchi!`
"""