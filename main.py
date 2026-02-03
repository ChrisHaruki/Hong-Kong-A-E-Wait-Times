from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Sample hospital data with two-tier wait times
hospitals_data = {
    'hk': [
        {'name_en': 'Queen Mary Hospital', 'name_tc': '瑪麗醫院', 'wait_urgent': 45, 'wait_semi': 1.5},
        {'name_en': 'Pamela Youde Nethersole Eastern Hospital', 'name_tc': '東區尤德夫人那打素醫院', 'wait_urgent': 90, 'wait_semi': 3.0},
        {'name_en': 'Ruttonjee Hospital', 'name_tc': '律敦治醫院', 'wait_urgent': 30, 'wait_semi': 1.0},
        {'name_en': 'Grantham Hospital', 'name_tc': '葛量洪醫院', 'wait_urgent': 60, 'wait_semi': 2.0}
    ],
    'kowloon': [
        {'name_en': 'Queen Elizabeth Hospital', 'name_tc': '伊利沙伯醫院', 'wait_urgent': 120, 'wait_semi': 4.0},
        {'name_en': 'Kwong Wah Hospital', 'name_tc': '廣華醫院', 'wait_urgent': 75, 'wait_semi': 2.5},
        {'name_en': 'United Christian Hospital', 'name_tc': '基督教聯合醫院', 'wait_urgent': 55, 'wait_semi': 1.8},
        {'name_en': 'Caritas Medical Centre', 'name_tc': '明愛醫院', 'wait_urgent': 40, 'wait_semi': 1.3},
        {'name_en': 'Princess Margaret Hospital', 'name_tc': '瑪嘉烈醫院', 'wait_urgent': 85, 'wait_semi': 2.8}
    ],
    'nt': [
        {'name_en': 'Prince of Wales Hospital', 'name_tc': '威爾斯親王醫院', 'wait_urgent': 95, 'wait_semi': 3.2},
        {'name_en': 'North District Hospital', 'name_tc': '北區醫院', 'wait_urgent': 50, 'wait_semi': 1.7},
        {'name_en': 'Tuen Mun Hospital', 'name_tc': '屯門醫院', 'wait_urgent': 110, 'wait_semi': 3.7},
        {'name_en': 'Pok Oi Hospital', 'name_tc': '博愛醫院', 'wait_urgent': 65, 'wait_semi': 2.2},
        {'name_en': 'Tin Shui Wai Hospital', 'name_tc': '天水圍醫院', 'wait_urgent': 35, 'wait_semi': 1.2}
    ]
}

def sort_hospitals_by_wait(hospitals):
    """Sort hospitals by urgent wait time (Tier 3)"""
    return sorted(hospitals, key=lambda h: h['wait_urgent'])

@app.route('/')
def index():
    lang = request.args.get('lang', 'zh')
    
    # Translations
    translations = {
        'zh': {
            'title': '香港急症室等候時間',
            'update_label': '更新時間',
            'urgent_label': '緊急（第3類）',
            'urgent_desc': '發燒、嘔吐、中度疼痛',
            'semi_urgent_label': '次緊急/非緊急（第4-5類）',
            'semi_urgent_desc': '傷風感冒、皮疹、小傷口',
            'urgent_short': '第3類',
            'semi_urgent_short': '第4-5類',
            'minute_label': '分鐘',
            'hour_label': '小時',
            'regions': {
                'hk': '香港島',
                'kowloon': '九龍',
                'nt': '新界'
            }
        },
        'en': {
            'title': 'HK A&E Wait Times',
            'update_label': 'Last updated',
            'urgent_label': 'Urgent (Tier 3)',
            'urgent_desc': 'Fever, vomiting, moderate pain',
            'semi_urgent_label': 'Semi-urgent/Non-urgent (Tier 4-5)',
            'semi_urgent_desc': 'Cold/flu, rash, minor wounds',
            'urgent_short': 'Tier 3',
            'semi_urgent_short': 'Tier 4-5',
            'minute_label': 'min',
            'hour_label': 'hr',
            'regions': {
                'hk': 'Hong Kong Island',
                'kowloon': 'Kowloon',
                'nt': 'New Territories'
            }
        }
    }
    
    t = translations.get(lang, translations['zh'])
    
    # Prepare regions data with sorted hospitals
    regions = {}
    for region_key, hospitals in hospitals_data.items():
        sorted_hospitals = sort_hospitals_by_wait(hospitals)
        regions[region_key] = {
            'name': t['regions'][region_key],
            'hospitals': [
                {
                    'name': h[f'name_{lang}' if lang == 'en' else 'name_tc'],
                    'wait_urgent': h['wait_urgent'],
                    'wait_semi': h['wait_semi']
                }
                for h in sorted_hospitals
            ]
        }
    
    # Update time
    update_time = datetime.now().strftime('%-d/%-m/%Y %-I:%M%p' if lang == 'en' else '%-d/%-m/%Y %p%-I:%M')
    
    return render_template(
        'index.html',
        lang=lang,
        title=t['title'],
        update_label=t['update_label'],
        update_time=update_time,
        urgent_label=t['urgent_label'],
        urgent_desc=t['urgent_desc'],
        semi_urgent_label=t['semi_urgent_label'],
        semi_urgent_desc=t['semi_urgent_desc'],
        urgent_short=t['urgent_short'],
        semi_urgent_short=t['semi_urgent_short'],
        minute_label=t['minute_label'],
        hour_label=t['hour_label'],
        regions=regions
    )

if __name__ == '__main__':
    app.run(debug=True)
