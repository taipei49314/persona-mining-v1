import streamlit as st
import os

def display_card(card: dict):
    name = card.get("name", "未知卡片")
    rarity = card.get("rarity", "R")
    image_path = card.get("image_path", "assets/cards/default.png")
    description = card.get("description", "")
    glow = card.get("glow", False)

    # 稀有度對應顏色與特效
    border_colors = {
        "R": "#A0A0A0",
        "SR": "#3B82F6",
        "SSR": "#9333EA",
        "UR": "#FFD700"
    }
    shadow_glow = {
        "R": "0px 0px 5px #A0A0A0",
        "SR": "0px 0px 10px #3B82F6",
        "SSR": "0px 0px 15px #9333EA",
        "UR": "0px 0px 20px #FFD700"
    }

    border_color = border_colors.get(rarity, "#999999")
    shadow = shadow_glow.get(rarity, "0px 0px 5px #888888")

    card_html = f'''
        <div style="border: 4px solid {border_color}; 
                    border-radius: 20px;
                    padding: 10px;
                    width: 260px;
                    text-align: center;
                    margin: auto;
                    box-shadow: {shadow};
                    background-color: #1c1c1c;
                    color: white;">
            <img src="data:image/png;base64,{_image_base64(image_path)}" 
                 style="width: 100%; border-radius: 12px;">
            <h4>{name}</h4>
            <p>{description}</p>
            <p><b>稀有度：</b> {rarity}</p>
        </div>
    '''

    st.markdown(card_html, unsafe_allow_html=True)

def _image_base64(image_path):
    import base64
    if not os.path.exists(image_path):
        image_path = "assets/cards/default.png"
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()