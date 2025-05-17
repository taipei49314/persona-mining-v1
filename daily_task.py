import json
from datetime import date

COLLECTION_FILE = "data/user_card_collection.json"

def init_daily_tasks():
    return {
        "login": False,
        "quiz": False,
        "profile_view": False,
        "bonus_unlocked": False
    }

def get_daily_tasks(user_id):
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    user_data = collections.get(user_id, {})
    today_str = date.today().isoformat()
    if user_data.get("daily_tasks_date") != today_str:
        user_data["daily_tasks"] = init_daily_tasks()
        user_data["daily_tasks_date"] = today_str
        collections[user_id] = user_data
        with open(COLLECTION_FILE, "w", encoding="utf-8") as f:
            json.dump(collections, f, ensure_ascii=False, indent=2)
    return user_data["daily_tasks"]

def complete_task(user_id, task_name):
    with open(COLLECTION_FILE, "r", encoding="utf-8") as f:
        collections = json.load(f)
    user_data = collections.get(user_id, {})
    today_str = date.today().isoformat()
    if user_data.get("daily_tasks_date") != today_str:
        user_data["daily_tasks"] = init_daily_tasks()
        user_data["daily_tasks_date"] = today_str
    if not user_data["daily_tasks"].get(task_name):
        user_data["daily_tasks"][task_name] = True
        user_data["coins"] = user_data.get("coins", 0) + 10
    if all([
        user_data["daily_tasks"].get("login"),
        user_data["daily_tasks"].get("quiz"),
        user_data["daily_tasks"].get("profile_view")
    ]):
        user_data["daily_tasks"]["bonus_unlocked"] = True
    collections[user_id] = user_data
    with open(COLLECTION_FILE, "w", encoding="utf-8") as f:
        json.dump(collections, f, ensure_ascii=False, indent=2)
    return user_data["daily_tasks"]