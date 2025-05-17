import json

COLLECTION_FILE = "data/user_card_collection.json"

def buy_with_coins(user_id, item_name):
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    user_data = collections.get(user_id, {"cards": {}, "last_draw_date": None, "coins": 0})
    shop_items = {
        "unlock_new_pool": 100,
        "upgrade_token": 50
    }
    if item_name not in shop_items:
        return {"error": "無此商品"}
    cost = shop_items[item_name]
    if user_data["coins"] < cost:
        return {"error": "金幣不足"}
    user_data["coins"] -= cost
    user_data.setdefault("inventory", []).append(item_name)
    collections[user_id] = user_data
    with open(COLLECTION_FILE, "w", encoding="utf-8") as f:
        json.dump(collections, f, ensure_ascii=False, indent=2)
    return {"success": f"已兌換 {item_name}", "remaining_coins": user_data["coins"]}