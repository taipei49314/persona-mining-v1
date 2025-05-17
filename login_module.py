import streamlit as st

def login_interface():
    st.sidebar.header("🔐 使用者登入")
    username = st.sidebar.text_input("請輸入使用者 ID", key="user_id_input")
    login = st.sidebar.button("登入", key="login_button")

    if login and username:
        st.session_state['user_id'] = username
        st.success(f"歡迎登入：{username}")
        st.experimental_rerun()

def get_current_user():
    return st.session_state.get('user_id', None)