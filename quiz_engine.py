import random

# 模擬簡易的心理測驗題庫（可改為實際 JSON 載入）
QUIZ_QUESTIONS = [
    {"q": "你喜歡與人交談還是獨處？", "options": ["交談", "獨處"]},
    {"q": "你做決定偏向感覺還是邏輯？", "options": ["感覺", "邏輯"]},
    {"q": "你喜歡計畫未來還是隨性應變？", "options": ["計畫", "隨性"]},
]

# 根據使用者答案模擬出一個人格標籤
def analyze_personality(answers: list) -> str:
    if not answers or len(answers) != 3:
        return "未知型人格"

    score = 0
    if answers[0] == "獨處":
        score += 1
    if answers[1] == "邏輯":
        score += 1
    if answers[2] == "計畫":
        score += 1

    if score == 3:
        return "冷靜邏輯型"
    elif score == 2:
        return "觀察型"
    elif score == 1:
        return "感受型"
    else:
        return "外向感性型"

# 產生對應人格標籤的抽卡偏好（簡化）
def get_card_bias(personality_type: str) -> list:
    if "邏輯" in personality_type:
        return ["C003"]
    elif "觀察" in personality_type:
        return ["C001"]
    elif "感受" in personality_type:
        return ["C004"]
    elif "外向" in personality_type:
        return ["C002"]
    else:
        return []