# streamlit-sample

streamlitを軽かしたサンプル

## メモ
#### ヘッダーを消す方法
https://discuss.streamlit.io/t/removing-the-deploy-button/53621

```python
st.set_page_config(page_title="Page Title")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
```

