import streamlit as st

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


# セッションステートの初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーからの入力
if prompt := st.chat_input("メッセージを入力してください"):
    # ユーザーのメッセージをセッションステートに追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ここにAIとのやり取りの処理を記述
    # 例: OpenAIのAPIを使って応答を生成
    response = "こんにちは！Streamlitチャットボットです。"

    # AIの応答をセッションステートに追加
    st.session_state.messages.append({"role": "assistant", "content": response})
