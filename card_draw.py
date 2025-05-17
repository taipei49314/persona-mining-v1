import json
import random
import os
from datetime import datetime, date

CARD_POOL_FILE = "data/card_pool.json"
DRAW_LOG_FILE = "logs/draw_log.json"
COLLECTION_FILE = "data/user_card_collection.json"

def load_card_pool():
    with open(CARD_POOL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def draw_card(user_id, bias=None):
    card_pool = load_card_pool()
    choices = [card for card in card_pool]
    weights = [card["weight"] for card in card_pool]
    if bias:
        for card in card_pool:
            if card['id'] in bias:
                card['weight'] += 20
    selected = random.choices(choices, weights=weights, k=1)[0]
    record_draw(user_id, selected)
    return selected

def record_draw(user_id, card):
    log = {
        "user_id": user_id,
        "timestamp": datetime.now().isoformat(),
        "card_id": card["id"],
        "card_name": card["name"],
        "rarity": card["rarity"]
    }
    with open(DRAW_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")

def is_free_draw_available(user_id):
    today_str = date.today().isoformat()
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    user_data = collections.get(user_id, {})
    last_draw_date = user_data.get("last_draw_date")
    return last_draw_date != today_str

def check_and_upgrade_card(user_data, card_id):
    card_data = user_data["cards"][card_id]
    if card_data["count"] >= 3:
        card_data["level"] = card_data.get("level", 1) + 1
        card_data["count"] = 0
        return f"{card_data['name']} 已升級至 Lv.{card_data['level']}"
    return None

def update_user_collection_with_upgrade(user_id, card):
    today_str = date.today().isoformat()
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    user_data = collections.get(user_id, {"cards": {}, "last_draw_date": None, "coins": 0})
    card_id = card["id"]
    if card_id in user_data["cards"]:
        user_data["cards"][card_id]["count"] += 1
        user_data["coins"] += 10
        upgrade_msg = check_and_upgrade_card(user_data, card_id)
    else:
        user_data["cards"][card_id] = {
            "name": card["name"],
            "rarity": card["rarity"],
            "count": 1
        }
        upgrade_msg = None
    user_data["last_draw_date"] = today_str
    collections[user_id] = user_data
    with open(COLLECTION_FILE, "w", encoding="utf-8") as f:
        json.dump(collections, f, ensure_ascii=False, indent=2)
    return upgrade_msg

def daily_free_draw_with_upgrade(user_id, bias=None):
    if not is_free_draw_available(user_id):
        return {"error": "今日已使用過免費抽卡。"}
    card = draw_card(user_id, bias)
    upgrade_msg = update_user_collection_with_upgrade(user_id, card)
    return {"card": card, "upgrade": upgrade_msg}