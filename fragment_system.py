import json

COLLECTION_FILE = "data/user_card_collection.json"

def get_user_data(user_id):
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        return json.load(f).get(user_id, {})

def save_user_data(user_id, data):
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    collections[user_id] = data
    with open(COLLECTION_FILE, "w", encoding="utf-8") as f:
        json.dump(collections, f, ensure_ascii=False, indent=2)

def decompose_card(user_id, card_id):
    user_data = get_user_data(user_id)
    card_data = user_data.get("cards", {}).get(card_id)
    if not card_data or card_data["count"] <= 0:
        return {"error": "卡片數量不足，無法分解"}

    rarity = card_data["rarity"]
    gain = {
        "R": 5,
        "SR": 10,
        "SSR": 20,
        "UR": 30
    }.get(rarity, 0)

    # 扣除卡片數量與新增碎片
    card_data["count"] -= 1
    user_data["fragments"] = user_data.get("fragments", 0) + gain

    save_user_data(user_id, user_data)
    return {"success": f"已分解 1 張 {card_data['name']}，獲得 {gain} 碎片"}

def synthesize_ssr(user_id):
    user_data = get_user_data(user_id)
    fragments = user_data.get("fragments", 0)
    if fragments < 100:
        return {"error": "碎片不足，需 100 片才能兌換 SSR 卡"}

    # 固定生成 SSR 卡（邏輯型）
    new_card_id = "C003"
    user_data["fragments"] -= 100
    card_data = user_data.setdefault("cards", {}).setdefault(new_card_id, {
        "name": "邏輯型人格 Lv.1",
        "rarity": "SSR",
        "count": 0
    })
    card_data["count"] += 1

    save_user_data(user_id, user_data)
    return {"success": "已使用 100 碎片兌換 1 張 SSR：邏輯型人格"}