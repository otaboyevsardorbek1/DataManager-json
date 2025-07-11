import os
import json
from typing import Any, Dict, List, Optional

class DataManager:
    data_dir = os.path.join(os.getcwd(), 'data')
    db_file = os.path.join(data_dir, "users.json")  # Barcha foydalanuvchilar shu faylda

    @classmethod
    def ensure_dir(cls):
        os.makedirs(cls.data_dir, exist_ok=True)
    
    @classmethod
    def load_all(cls) -> List[Dict[str, Any]]:
        cls.ensure_dir()
        if not os.path.exists(cls.db_file):
            return []
        with open(cls.db_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    print("Xatolik: users.json json massiv emas!")
                    return []
            except Exception as e:
                print(f"Faylni o'qishda xatolik: {e}")
                return []

    @classmethod
    def save_all(cls, user_list: List[Dict[str, Any]]):
        cls.ensure_dir()
        with open(cls.db_file, "w", encoding="utf-8") as f:
            json.dump(user_list, f, ensure_ascii=False, indent=4)

    @classmethod
    def upsert_user(cls, new_user: Dict[str, Any]) -> str:
        user_list = cls.load_all()
        login = new_user.get("login")
        if not login:
            return "login maydoni talab qilinadi!"

        # Avvaldan mavjud foydalanuvchi bormi?
        found = False
        for idx, user in enumerate(user_list):
            if user.get("login") == login:
                found = True
                changes, added, removed = {}, {}, {}
                old_user = user.copy()
                # Yangilash va farqlarni aniqlash
                for k, v in new_user.items():
                    if k in old_user:
                        if old_user[k] != v:
                            user_list[idx][k] = v
                            changes[k] = {"old": old_user[k], "new": v}
                    else:
                        user_list[idx][k] = v
                        added[k] = v
                for k in list(old_user.keys()):
                    if k not in new_user:
                        removed[k] = old_user[k]
                        user_list[idx].pop(k)
                if not changes and not added and not removed:
                    return "Ma'lumot o'zgarmagan."
                cls.save_all(user_list)
                msg = "Ma'lumot yangilandi va saqlandi.\n"
                if changes:
                    msg += "O'zgargan: " + ", ".join([f"{k}: {v['old']} -> {v['new']}" for k, v in changes.items()]) + "\n"
                if added:
                    msg += "Yangi: " + ", ".join([f"{k}: {v}" for k, v in added.items()]) + "\n"
                if removed:
                    msg += "O'chirilgan: " + ", ".join([f"{k}: {v}" for k, v in removed.items()]) + "\n"
                return msg.strip()
        # Yangi foydalanuvchi
        user_list.append(new_user)
        cls.save_all(user_list)
        return "Yangi foydalanuvchi saqlandi."

    @classmethod
    def find_user(cls, login: str) -> Optional[Dict[str, Any]]:
        user_list = cls.load_all()
        for user in user_list:
            if user.get("login") == login:
                return user
        return None

# --- Misol uchun foydalanish ---
if __name__ == "__main__":
    new_api_data = {
        "login": "otaboyevsardorbek1",
        "test": 90,
        "avatar_url": "https://avatars.githubusercontent.com/u/127109664?v=4",
        "html_url": "https://github.com/otaboyevsardorbek1",
        "followers_url": "https://api.github.com/users/otaboyevsardorbek1/followers",
        "repos_url": "https://api.github.com/users/otaboyevsardorbek1/repos",
        "name": "Otaboyev Sardorbek",
        "company": "PRODEV-MCHJ",
        "blog": "https://t.me/otaboyev_sardorbek_blog_dev",
        "location": "Toshkent",
        "bio": "HTML, CSS, JS, PYTHON, MONGODB, MYSQL, SQLLITE3 AND DJANGO BEGINNER",
        "public_repos": 3,
        "followers": 59090,
        "following": 94,
        "created_at": "2023-03-06;17:31:03",
        "updated_at": "2025-05-27;17:40:30",
    }

    natija = DataManager.upsert_user(new_api_data)
    print(natija)

    # Agar foydalanuvchini ko‘rmoqchi bo‘lsangiz:
    # user = DataManager.find_user("otaboyevsardorbek1")
    # print(user)
