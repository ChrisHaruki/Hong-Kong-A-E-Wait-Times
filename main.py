from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

HOSPITAL_NAMES_TC = {
    "Alice Ho Miu Ling Nethersole Hospital": "雅麗氏何妙齡那打素醫院",
    "Caritas Medical Centre": "明愛醫院",
    "Kwong Wah Hospital": "廣華醫院",
    "North District Hospital": "北區醫院",
    "North Lantau Hospital": "北大嶼山醫院",
    "Pamela Youde Nethersole Eastern Hospital": "東區尤德夫人那打素醫院",
    "Pok Oi Hospital": "博愛醫院",
    "Prince of Wales Hospital": "威爾斯親王醫院",
    "Princess Margaret Hospital": "瑪嘉烈醫院",
    "Queen Elizabeth Hospital": "伊利沙伯醫院",
    "Queen Mary Hospital": "瑪麗醫院",
    "Ruttonjee Hospital": "律敦治醫院",
    "St John Hospital": "聖約翰醫院",
    "Tin Shui Wai Hospital": "天水圍醫院",
    "Tseung Kwan O Hospital": "將軍澳醫院",
    "Tuen Mun Hospital": "屯門醫院",
    "United Christian Hospital": "基督教聯合醫院",
    "Yan Chai Hospital": "仁濟醫院"
}

def parse_time_to_minutes(time_str):
    """Convert time string to minutes for sorting"""
    if not time_str or time_str == "0 minute" or time_str == "0 hour":
        return 0
    time_str = time_str.lower().replace("less than ", "")
    if "hour" in time_str:
        parts = time_str.replace("hours", "").replace("hour", "").strip().split()
        hours = float(parts[0])
        return int(hours * 60)
    elif "minute" in time_str:
        parts = time_str.replace("minutes", "").replace("minute", "").strip().split()
        return int(parts[0])
    return 0

def get_wait_color(minutes):
    """Return color based on wait time"""
    if minutes <= 20:
        return "#22c55e"  # green
    elif minutes <= 40:
        return "#eab308"  # yellow
    elif minutes <= 60:
        return "#f97316"  # orange
    else:
        return "#ef4444"  # red

@app.route("/")
def index():
    lang = request.args.get("lang", "zh")
    
    # Fetch live data
    try:
        r = requests.get("https://www.ha.org.hk/opendata/aed/aedwtdata2-en.json", timeout=10)
        data = r.json()
        hospitals = data.get("waitTime", [])
        update_time = data.get("updateTime", "N/A")
    except:
        hospitals = []
        update_time = "Error loading data"
    
    # Process hospital data
    for h in hospitals:
        h["t3_minutes"] = parse_time_to_minutes(h.get("t3p50", "0"))
        h["t45_minutes"] = parse_time_to_minutes(h.get("t45p50", "0"))
        h["t3_color"] = get_wait_color(h["t3_minutes"])
        h["t45_color"] = get_wait_color(h["t45_minutes"])
        
        # Add display names
        name_en = h.get("hospName", "Unknown")
        h["name_tc"] = HOSPITAL_NAMES_TC.get(name_en, name_en)
        h["name_en"] = name_en
    
    hospitals.sort(key=lambda x: x["t3_minutes"])
    
    # Translations
    translations = {
        "en": {
            "title": "Hong Kong A&E Wait Times",
            "updated": "Updated",
            "cat3_label": "Urgent (Cat 3)",
            "cat3_desc": "Fever, vomiting, moderate pain",
            "cat45_label": "Minor (Cat 4-5)",
            "cat45_desc": "Colds, rashes, small cuts",
            "median_label": "Median",
            "p95_label": "95% wait",
            "footer": "Live data from Hospital Authority. Category 3 most common for sick kids."
        },
        "zh": {
            "title": "香港急症室等候時間",
            "updated": "更新時間",
            "cat3_label": "緊急 (第3類)",
            "cat3_desc": "發燒、嘔吐、中度疼痛",
            "cat45_label": "次緊急/非緊急 (第4-5類)",
            "cat45_desc": "傷風感冒、皮疹、小傷口",
            "median_label": "中位數",
            "p95_label": "95%等候",
            "footer": "醫管局實時數據。第3類最常見於生病小朋友。"
        }
    }
    
    t = translations[lang]
    
    return render_template(
        "index.html",
        lang=lang,
        hospitals=hospitals,
        update_time=update_time,
        **t
    )

if __name__ == "__main__":
    app.run(debug=True)
