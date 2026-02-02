from flask import Flask, request
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
    
    # Sort by Category 3 median wait time (most relevant for parents)
    for h in hospitals:
        h["t3_minutes"] = parse_time_to_minutes(h.get("t3p50", "0"))
        h["t45_minutes"] = parse_time_to_minutes(h.get("t45p50", "0"))
    
    hospitals.sort(key=lambda x: x["t3_minutes"])
    
    # Translations
    if lang == "en":
        title = "Hong Kong A&E Wait Times"
        updated = "Updated"
        cat3_label = "Urgent (Cat 3)"
        cat3_desc = "Fever, vomiting, moderate pain"
        cat45_label = "Minor (Cat 4-5)"
        cat45_desc = "Colds, rashes, small cuts"
        median_label = "Median"
        p95_label = "95% wait"
        footer = "Live data from Hospital Authority. Category 3 most common for sick kids."
    else:
        title = "香港急症室等候時間"
        updated = "更新時間"
        cat3_label = "緊急 (第3類)"
        cat3_desc = "發燒、嘔吐、中度疼痛"
        cat45_label = "次緊急/非緊急 (第4-5類)"
        cat45_desc = "傷風感冒、皮疹、小傷口"
        median_label = "中位數"
        p95_label = "95%等候"
        footer = "醫管局實時數據。第3類最常見於生病小朋友。"

    html = f"""
    <!DOCTYPE html>
    <html lang="{'en' if lang == 'en' else 'zh-Hant'}">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="refresh" content="60">
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
                background: #f8f9fa;
                color: #111;
                margin: 0;
                padding: 1em;
                line-height: 1.6;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background: white;
                padding: 1.5em;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: center;
                margin-bottom: 1.5em;
            }}
            .lang-switch {{
                text-align: right;
                margin-bottom: 0.5em;
                font-size: 0.9rem;
            }}
            .lang-switch a {{
                color: #666;
                text-decoration: none;
                padding: 0.3em 0.6em;
                border-radius: 4px;
                transition: all 0.2s;
            }}
            .lang-switch a:hover {{
                background: #f0f0f0;
            }}
            .lang-switch a.active {{
                color: #dc2626;
                font-weight: bold;
            }}
            h1 {{
                font-size: 1.8rem;
                margin: 0.3em 0;
                color: #dc2626;
            }}
            .update-time {{
                color: #666;
                font-size: 0.9rem;
            }}
            .legend {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1em;
                margin: 1.5em 0;
                padding: 1em;
                background: #f8f9fa;
                border-radius: 8px;
            }}
            .legend-item {{
                font-size: 0.9rem;
            }}
            .legend-title {{
                font-weight: bold;
                color: #dc2626;
                margin-bottom: 0.2em;
            }}
            .legend-desc {{
                color: #666;
                font-size: 0.85rem;
            }}
            .hospital-card {{
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 1em;
                margin-bottom: 1em;
                transition: all 0.2s;
            }}
            .hospital-card:hover {{
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                transform: translateY(-2px);
            }}
            .hospital-name {{
                font-size: 1.2rem;
                font-weight: bold;
                margin-bottom: 0.5em;
                color: #111;
            }}
            .wait-times {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1em;
            }}
            .wait-box {{
                padding: 0.8em;
                border-radius: 6px;
                background: #f8f9fa;
            }}
            .wait-label {{
                font-size: 0.85rem;
                color: #666;
                margin-bottom: 0.3em;
            }}
            .wait-value {{
                font-size: 1.3rem;
                font-weight: bold;
                margin-bottom: 0.2em;
            }}
            .wait-p95 {{
                font-size: 0.85rem;
                color: #666;
            }}
            .footer {{
                text-align: center;
                margin-top: 2em;
                padding-top: 1em;
                border-top: 1px solid #e5e7eb;
                color: #666;
                font-size: 0.9rem;
            }}
            @media (max-width: 600px) {{
                .legend {{
                    grid-template-columns: 1fr;
                }}
                .wait-times {{
                    grid-template-columns: 1fr;
                }}
                h1 {{
                    font-size: 1.5rem;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="lang-switch">
                <a href="?lang=zh" class="{'active' if lang == 'zh' else ''}">中文</a>
                <span style="color: #ddd;">|</span>
                <a href="?lang=en" class="{'active' if lang == 'en' else ''}">EN</a>
            </div>
            
            <div class="header">
                <h1>{title}</h1>
                <div class="update-time">{updated}: {update_time}</div>
            </div>
            
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-title">{cat3_label}</div>
                    <div class="legend-desc">{cat3_desc}</div>
                </div>
                <div class="legend-item">
                    <div class="legend-title">{cat45_label}</div>
                    <div class="legend-desc">{cat45_desc}</div>
                </div>
            </div>
    """
    
    for h in hospitals:
        name_en = h.get("hospName", "Unknown")
        name_tc = HOSPITAL_NAMES_TC.get(name_en, name_en)
        
        t3p50 = h.get("t3p50", "N/A")
        t3p95 = h.get("t3p95", "N/A")
        t45p50 = h.get("t45p50", "N/A")
        t45p95 = h.get("t45p95", "N/A")
        
        t3_color = get_wait_color(h["t3_minutes"])
        t45_color = get_wait_color(h["t45_minutes"])
        
        display_name = name_tc if lang == "zh" else name_en
        
        html += f"""
            <div class="hospital-card">
                <div class="hospital-name">{display_name}</div>
                <div class="wait-times">
                    <div class="wait-box">
                        <div class="wait-label">{cat3_label}</div>
                        <div class="wait-value" style="color: {t3_color};">{t3p50}</div>
                        <div class="wait-p95">{p95_label}: {t3p95}</div>
                    </div>
                    <div class="wait-box">
                        <div class="wait-label">{cat45_label}</div>
                        <div class="wait-value" style="color: {t45_color};">{t45p50}</div>
                        <div class="wait-p95">{p95_label}: {t45p95}</div>
                    </div>
                </div>
            </div>
        """
    
    html += f"""
            <div class="footer">
                <p>{footer}</p>
                <small>data.gov.hk - Hospital Authority<br>Haruki Robotics Lab</small>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html

if __name__ == "__main__":
    app.run(debug=True)
