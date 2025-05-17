import json

COLLECTION_FILE = "data/user_card_collection.json"

def get_user_profile(user_id):
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    return collections.get(user_id, {})