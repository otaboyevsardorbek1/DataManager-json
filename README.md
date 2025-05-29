# 🔐 JSON-Based User Data Manager

This project provides a lightweight, file-based JSON management system for storing and updating user-specific API data — typically retrieved from external services like GitHub. It allows you to merge new data with previously stored data, tracking and reporting changes clearly.

> ✅ Designed for developers who need to cache, track, and sync API user data in a local or server environment.

---

## 📌 Features

- 🔄 **Merge & Update** user data with difference detection.
- 🆕 **Track new fields** added in the latest data.
- ✏️ **Track changes** in existing fields (old → new).
- 📂 **Automatic file creation** if not exists.
- 💡 **Pretty-print** JSON output.
- 🚀 Lightweight & dependency-free (pure Python).

---

## 📂 Project Structure

.
├── data/
└── private_<username>.json # Stored user-specific data files
├── main.py # Core logic and execution
└── README.md # Documentation

---

## ⚙️ How It Works

1. New API data (e.g., from GitHub) is passed to the `merge_and_update()` function.
2. It loads the previously stored JSON data for the given user (by GitHub `login`).
3. Compares old vs. new:
   - Updates changed values.
   - Adds new keys.
   - Keeps unchanged values as-is.
4. Reports what changed (or notes if nothing changed).
5. Saves updated data back to the file.

---

## 🧠 Code Breakdown

▶️ Usage Example
Run the script with:
python main.py
Example input data (GitHub-like API response):
{
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
Console Output:
O'zgargan maydonlar:
 - followers: 200 → 5000000000000000000000
 - updated_at: 2024-10-01 → 2025-05-27
Yangi qo'shilgan maydonlar:
 - twitter: @otaboyevsardorbek
Ma'lumot yangilandi va saqlandi.
📦 Installation
No third-party packages required! Just run using Python 3.7+:
git clone https://github.com/yourusername/json-user-data-manager.git
cd json-user-data-manager
python main.py
git clone https://github.com/yourusername/json-user-data-manager.git
cd json-user-data-manager
python main.py
