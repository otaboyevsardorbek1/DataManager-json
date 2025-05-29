import json
import os

class DataManager:
    data_dir = os.path.join(os.getcwd(), 'data')

    @classmethod
    def file_path(cls, path: str) -> str:
        if not os.path.exists(cls.data_dir):
            os.makedirs(cls.data_dir)
        return os.path.join(cls.data_dir, path)

    @classmethod
    def data_files_path(cls, username: str) -> str:
        return cls.file_path(f"private_{username}.json")

    @classmethod
    def load_json(cls, filepath: str):
        if not os.path.exists(filepath):
            return None
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def save_json(cls, filepath: str, data: dict):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def merge_and_update(cls, username: str, new_data: dict) -> str:
        filepath = cls.data_files_path(username)
        old_data = cls.load_json(filepath)

        if old_data is None:
            cls.save_json(filepath, new_data)
            return "Yangi ma'lumot saqlandi."

        changed = {}
        added = {}
        removed = {}

        updated_data = old_data.copy()

        # O'zgargan va yangi kalitlarni tekshirish
        for key, new_value in new_data.items():
            if key in old_data:
                if old_data[key] != new_value:
                    updated_data[key] = new_value
                    changed[key] = {"old": old_data[key], "new": new_value}
            else:
                updated_data[key] = new_value
                added[key] = new_value

        # O'chirilgan kalitlar
        for key in list(updated_data.keys()):
            if key not in new_data:
                removed[key] = updated_data.pop(key)

        if not changed and not added and not removed:
            return "Ma'lumot o'zgarmagan."

        cls.save_json(filepath, updated_data)

        if changed:
            print("O'zgargan maydonlar:")
            for k, v in changed.items():
                print(f" - {k}: {v['old']} --> {v['new']}")
        if added:
            print("Yangi qo'shilgan maydonlar:")
            for k, v in added.items():
                print(f" - {k}: {v}")
        if removed:
            print("O'chirilgan maydonlar:")
            for k, v in removed.items():
                print(f" - {k}: {v}")

        return "Ma'lumot yangilandi va saqlandi."


if __name__ == "__main__":
    new_api_data = {
        "login": "otaboyevsardorbek1",
        "test":90,
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

    username = new_api_data["login"]
    result = DataManager.merge_and_update(username, new_api_data)
    print(result)
