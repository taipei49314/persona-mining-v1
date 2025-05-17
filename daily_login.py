import streamlit as st
import json
import os
from datetime import datetime, timedelta

USER_DATA_FILE = "data/user_login_log.json"

def load_login_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_login_data(data):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_today():
    return datetime.today().strftime("%Y-%m-%d")

def show_login_reward(user_id):
    login_data = load_login_data()
    today = get_today()

    if user_id not in login_data:
        login_data[user_id] = {
            "last_login": "",
            "streak": 0,
            "total": 0
        }

    user_log = login_data[user_id]
    last_login = user_log["last_login"]

    # 判斷是否連續
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    if today == last_login:
        st.info(f"📆 今日已簽到 ✅（連續 {user_log['streak']} 天）")
    else:
        if last_login == yesterday:
            user_log["streak"] += 1
        else:
            user_log["streak"] = 1  # 中斷重算

        user_log["last_login"] = today
        user_log["total"] += 1
        save_login_data(login_data)

        st.success(f"🎉 簽到成功！目前連續 {user_log['streak']} 天")
        reward = "🎁 金幣 +5"
        if user_log["streak"] == 7:
            reward = "🌟 抽卡券 +1（連續 7 天）"
        elif user_log["streak"] == 30:
            reward = "💎 SSR 合成碎片 +30"
        st.balloons()
        st.write(f"獲得獎勵：{reward}")

    # 顯示摘要
    st.markdown("---")
    st.markdown(f"- 累計簽到：{user_log['total']} 天")
    st.markdown(f"- 目前連續：{user_log['streak']} 天")
    st.markdown(f"- 上次簽到：{user_log['last_login']}")