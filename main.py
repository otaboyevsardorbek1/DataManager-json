import json
import os

def data_files_path(username):
    return f"data/private_{username}.json"

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def merge_and_update(username, new_data):
    filepath = data_files_path(username)
    old_data = load_json(filepath)

    if old_data is None:
        # Agar fayl yo'q bo'lsa, yangi ma'lumotni saqlaymiz
        save_json(filepath, new_data)
        return "Yangi ma'lumot saqlandi."

    changed = {}
    added = {}

    # Eski ma'lumotni yangilash uchun nusxa olamiz
    updated_data = old_data.copy()

    for key, new_value in new_data.items():
        if key in old_data:
            if old_data[key] != new_value:
                # Qiymat o'zgargan bo'lsa yangilaymiz va qayd qilamiz
                updated_data[key] = new_value
                changed[key] = {"old": old_data[key], "new": new_value}
        else:
            # Yangi kalit qo'shamiz
            updated_data[key] = new_value
            added[key] = new_value

    if not changed and not added:
        return "Ma'lumot o'zgarmagan."

    # Yangilangan ma'lumotni saqlaymiz
    save_json(filepath, updated_data)

    # O'zgartirish va qo'shishlarni ko'rsatamiz
    if changed:
        print("O'zgargan maydonlar:")
        for k, v in changed.items():
            print(f" - {k}: {v['old']} --> {v['new']}")
    if added:
        print("Yangi qo'shilgan maydonlar:")
        for k, v in added.items():
            print(f" - {k}: {v}")

    return "Ma'lumot yangilandi va saqlandi."

# Misol uchun ishlatish:
if __name__ == "__main__":
    new_api_data = {
        "login": "otaboyevsardorbek1",
        "avatar_url": "https://avatars.githubusercontent.com/u/127109664?v=4",
        "html_url": "https://github.com/otaboyevsardorbek1",
        "followers_url": "https://api.github.com/users/otaboyevsardorbek1/followers",
        "repos_url": "https://api.github.com/users/otaboyevsardorbek1/repos",
        "name": "Otaboyev Sardorbek",
        "company": "PRODEV-MCHJ",
        "blog": "https://t.me/otaboyev_sardorbek_blog_dev",
        "location": "Toshkent",
        "bio": "HTML, CSS, JS, PYTHON, MONGODB, MYSQL, SQLLITE3 AND DJANGO BEGINNER",
        "public_repos": 133,
        "followers": 5000000000000000000000,
        "following": 94,
        "created_at": "2023-03-06;17:31:03",
        "updated_at": "2025-05-27;17:40:30",
        "twitter": "@otaboyevsardorbek"
    }

    username = new_api_data["login"]
    result = merge_and_update(username, new_api_data)
    print(result)
