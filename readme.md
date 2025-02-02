# 🚀 Mesh Rename Bot

**Mesh Rename Bot** is a powerful Telegram bot designed for **auto-renaming files** using **custom filters**. With some advanced features like **permanent thumbnails, multiple upload modes, queue management, and more**. Also, supports 7 different languages.

This bot is aimed to be **the best rename bot around**! 🏆✨

---

## ⚠️ Beta Release Notice
- The bot is **still in beta**. Your feedback is valuable!  
- **Report any bugs, issues, or feature requests** by filing an issue.  
- The bot will **guide you** through setting up filters easily! 😊

---

## 🛠 Features
✅ **Auto Rename** files based on **custom filters**  
✅ **Permanent Thumbnail Support**  
✅ **3 Different Upload Modes** (Same Format, Forced Document, Streamable Media)  
✅ **2 Different Rename Modes** (With and Without Command)
✅ **Queue System** to maintain consistent renaming speed ⚡  
✅ **PostgreSQL Support** (Mongo Planned)  
✅ **Track User Activity** 📊  
✅ **Force Join** (Require users to join a specific channel before use)  
✅ **Multi-language Support** 🌎  
✅ **Admin Controls** to manage bot users  
✅ **7 Different** languages supported (en, es, ar, hi, ko, zh, ru) 

---

## ☁️ Deploy to Heroku  
Deploy your own instance of the bot on Heroku with one click!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yash-dk/Mesh-RenameBot)

---

## 🔍 Filters Explained
**Filters** can be managed using the `/filters` command.

### 🏷 **Addition Filter**
➕ Adds **specific text** to the **beginning or end** of the file name.  

### ❌ **Remove Filter**
🚫 Removes **specific text** from the file name **if present**.  

### 🔄 **Replace Filter**
🔁 Replaces **a specific text** with a **new text**.

---

## ⚙️ Configuration Variables
Modify the `config.py` file inside `MeshRenameBot` to **update settings & commands**.

| Variable Name       | Description |
|--------------------|-------------|
| `DB_URI` | **Database URL** (PostgreSQL) |
| `API_HASH` | **Telegram API HASH** |
| `API_ID` | **Telegram API ID** |
| `BOT_TOKEN` | **Bot Token** (from @BotFather) |
| `COMPLETED_STR` | **Completed Symbol Marker** |
| `REMAINING_STR` | **Remaining Symbol Marker** |
| `MAX_QUEUE_SIZE` | **Maximum concurrent rename tasks** (default: 5) |
| `SLEEP_SECS` | **Sleep time before editing messages** (default: 10 sec) |
| `IS_PRIVATE` | **Set bot to private mode** |
| `AUTH_USERS` | **List of allowed users** (works only when `IS_PRIVATE` is enabled) |
| `OWNER_ID` | **Owner's Telegram User ID** |
| `FORCEJOIN` | **Public group/channel username or invite link** (leave blank to disable) |
| `FORCEJOIN_ID` | **Chat ID for `FORCEJOIN`** |
| `TRACE_CHANNEL` | **Tracking Channel ID** (set `0` to disable tracking) |
| `SAVE_FILE_TO_TRACE_CHANNEL` | **Save user file to tracking channel** |
| `DEFAULT_LOCALE` | **Default Lnaguage of Bot** (values can be en, es, ar, hi, ko, zh, ru) |

---

## 📜 Commands List
Use these commands to interact with the bot:

| Command | Description |
|---------|-------------|
| `/start` | ✅ **Check if the bot is running** |
| `/rename` | ✍️ **Rename a file** (`/rename filename.extension`) |
| `/filters` | ⚙️ **Manage rename filters** |
| `/setthumb` | 📷 **Set a permanent thumbnail** (Reply to an image) |
| `/getthumb` | 📸 **Retrieve the current thumbnail** |
| `/clrthumb` | ❌ **Clear the set thumbnail** |
| `/mode` | 🔄 **Change upload and/or rename mode** (Same Format, Document, General Media) |
| `/queue` | 📊 **View rename queue status** |
| `/setcaption` | 📝 **Set a caption for the renamed files** |
| `/setlang` | 🌐 **Change the bot's language.** |


### 🔄 Upload Modes:
- **Same format as sent** (Document remains Document, Video remains Video)
- **Force to Document** (All uploads as files)
- **General Media** (Streamable Video/Audio)

---

## 🖥 VPS Deployment Guide
For self-hosted deployment on a **VPS**, follow these steps:

### 1️⃣ Install Dependencies  
```bash
sudo apt update && sudo apt install ffmpeg python3-pip
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/yash-dk/Mesh-RenameBot.git
cd Mesh-RenameBot
```

### 3️⃣ Install Python Packages
```bash
pip3 install -r requirements.txt
```

### 4️⃣ Run the Bot
```bash
python3 -m MeshRenameBot
```

## 🎖 Credits
[Me](https://github.com/yash-dk)

[Dan for Pyrogram](https://github.com/pyrogram/pyrogram)

