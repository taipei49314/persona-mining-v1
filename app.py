import streamlit as st
from login_module import login_interface, get_current_user
from card_draw import draw_card
from fragment_system import decompose_card, synthesize_ssr
from shop import display_shop, handle_purchase
from user_profile import get_user_profile, display_rankings
from quiz_engine import run_persona_quiz

st.set_page_config(page_title="Persona Mining V1", layout="wide")

# 登入流程
if "user_id" not in st.session_state:
    st.session_state.user_id = None

if not st.session_state.user_id:
    st.title("🧠 Persona Mining V1")
    st.session_state.user_id = login_interface()

# 登入成功後顯示主要畫面
if st.session_state.user_id:
    user_id = st.session_state.user_id
    st.sidebar.success(f"歡迎回來，{user_id}！")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎴 抽卡中心", "🪙 碎片／合成", "💳 商店", "🏆 排行榜", "🧠 心理測驗"])

    with tab1:
        st.header("🎴 抽卡中心")
        if st.button("抽一張卡"):
            card = draw_card(user_id)
            st.success(f"你抽到了 {card['name']} ({card['rarity']})")
            if "image" in card:
                st.image(card["image"], width=200)

    with tab2:
        st.header("🪙 碎片與合成系統")
        if st.button("分解重複卡"):
            result = decompose_card(user_id)
            st.info(result)
        if st.button("嘗試合成 SSR"):
            result = synthesize_ssr(user_id)
            st.success(result)

    with tab3:
        st.header("💳 商店兌換")
        display_shop(user_id)
        if st.button("立即購買"):
            feedback = handle_purchase(user_id)
            st.success(feedback)

    with tab4:
        st.header("🏆 排行榜 / 稱號")
        display_rankings()

    with tab5:
        st.header("🧠 重新分析人格")
        run_persona_quiz(user_id)