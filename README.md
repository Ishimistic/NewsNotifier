# 📰 News Notifier

News Notifier is a Windows desktop application that delivers current news headlines directly to users through Windows notifications. The application fetches news from various RSS feeds using a fallback mechanism and displays the top stories as toast notifications.
## 📌 Features
- Fetches news from multiple configurable RSS sources.
- Uses a fallback mechanism to ensure reliability.
- Displays Windows toast notifications for the top 10 news items.
- Shows source attribution for each headline.
- Displays notifications sequentially with a 10-second interval.

## 🛠️ Installation

### 1️⃣ Ensure you have Python 3.6+ installed on your Windows system.

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/news-notifier.git
cd news-notifier
```

### 3️⃣ Install Dependencies
```sh
pip install requests winotify
```

### 4️⃣ Run the Application
```sh
python newsNotifier.py
```

## ⚙️ Configuration
Edit the `RSS_FEED_URLS` list in `topnews.py` to customize your news sources. The application will try each source in order until one succeeds.

## 📡 Requirements
- Windows 10 or newer
- Python 3.6+
- Internet connection

## 📦 Dependencies
- `requests`
- `winotify`
- `xml.etree.ElementTree` (standard library)
- `time` (standard library)

## 📜 License
This project is open-source and available under the **MIT License**.

---
🔗 **Author:** [Your Name](https://github.com/yourusername)
