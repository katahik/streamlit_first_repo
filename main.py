import time

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit fandamentals')

st.write('プログレスバー')
'Start'

# 空で用意しておく
latest_iteration = st.empty()
bar = st.progress(0)

# ここでプログレスバーに値をいれる
# for文がすべて終わったら下の処理にすすむ
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'done'

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# if st.checkbox('Show image'):
#     img = Image.open('streamlit.png')
#     st.image(img,caption='hoge',use_column_width=True)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

ex = st.expander('問い合わせ')
ex.write('問い合わせ内容を書く')

text = st.text_input('select')
# option = st.selectbox('select',list(range(1,11)))

'あなたの好きな数字は,',text,'です'


condition = st.slider('あなたはの調子は？', 0,100,50)
'コンディション',condition