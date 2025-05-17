import streamlit as st
import time
from st_card_display import display_card

def ssr_fusion_animation(card_data: dict):
    st.markdown("### 🧩 正在合成 SSR 卡片...")
    placeholder = st.empty()

    with placeholder.container():
        st.image("assets/animations/fragments_fly.png", caption="碎片正在融合...", use_column_width=True)
        time.sleep(1.2)
        st.image("assets/animations/glow_center.png", caption="能量集中...", use_column_width=True)
        time.sleep(1.0)

    placeholder.empty()
    st.markdown("### 🌟 合成成功！你獲得了：")
    display_card(card_data)