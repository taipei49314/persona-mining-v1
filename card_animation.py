import streamlit as st
import time
from st_card_display import display_card

def card_draw_animation(card_data: dict):
    st.markdown("### 🎁 正在開啟卡包...")
    placeholder = st.empty()

    with placeholder.container():
        st.image("assets/animations/card_pack.png", caption="卡包即將打開...", use_column_width=True)
        time.sleep(1.5)

    placeholder.empty()
    st.markdown("### 🎉 你獲得了：")
    display_card(card_data)