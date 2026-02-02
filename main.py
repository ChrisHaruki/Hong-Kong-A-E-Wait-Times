<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="utf-8">
    <title>香港急症室等候時間</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
            background: #f8f9fa;
            color: #111;
            margin: 0;
            padding: 1em;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 1.5em;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 1.5em;
        }
        .lang-switch {
            text-align: right;
            margin-bottom: 0.5em;
            font-size: 0.9rem;
        }
        .lang-switch a {
            color: #666;
            text-decoration: none;
            padding: 0.3em 0.6em;
            border-radius: 4px;
            transition: all 0.2s;
        }
        .lang-switch a:hover {
            background: #f0f0f0;
        }
        .lang-switch a.active {
            color: #dc2626;
            font-weight: bold;
        }
        h1 {
            font-size: 1.8rem;
            margin: 0.3em 0;
            color: #dc2626;
        }
        .update-time {
            color: #666;
            font-size: 0.9rem;
        }
        .legend {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1em;
            margin: 1.5em 0;
            padding: 1em;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .legend-item {
            font-size: 0.9rem;
        }
        .legend-title {
            font-weight: bold;
            color: #dc2626;
            margin-bottom: 0.2em;
        }
        .legend-desc {
            color: #666;
            font-size: 0.85rem;
        }
        .hospital-card {
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 1em;
            margin-bottom: 1em;
            transition: all 0.2s;
        }
        .hospital-card:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        .hospital-name {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5em;
            color: #111;
        }
        .wait-times {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1em;
        }
        .wait-box {
            padding: 0.8em;
            border-radius: 6px;
            background: #f8f9fa;
        }
        .wait-label {
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 0.3em;
        }
        .wait-value {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 0.2em;
        }
        .wait-p95 {
            font-size: 0.85rem;
            color: #666;
        }
        .footer {
            text-align: center;
            margin-top: 2em;
            padding-top: 1em;
            border-top: 1px solid #e5e7eb;
            color: #666;
            font-size: 0.9rem;
        }
        @media (max-width: 600px) {
            .legend {
                grid-template-columns: 1fr;
            }
            .wait-times {
                grid-template-columns: 1fr;
            }
            h1 {
                font-size: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="lang-switch">
            <a href="#" class="active">中文</a>
            <span style="color: #ddd;">|</span>
            <a href="#">EN</a>
        </div>
        
        <div class="header">
            <h1>香港急症室等候時間</h1>
            <div class="update-time">更新時間: 2/2/2026 12:30AM</div>
        </div>
        
        <div class="legend">
            <div class="legend-item">
                <div class="legend-title">緊急 (第3類)</div>
                <div class="legend-desc">發燒、嘔吐、中度疼痛</div>
            </div>
            <div class="legend-item">
                <div class="legend-title">次緊急/非緊急 (第4-5類)</div>
                <div class="legend-desc">傷風感冒、皮疹、小傷口</div>
            </div>
        </div>

        <!-- Sample Hospital Cards -->
        <div class="hospital-card">
            <div class="hospital-name">伊利沙伯醫院</div>
            <div class="wait-times">
                <div class="wait-box">
                    <div class="wait-label">緊急 (第3類)</div>
                    <div class="wait-value" style="color: #22c55e;">12 minutes</div>
                    <div class="wait-p95">95%等候: 22 minutes</div>
                </div>
                <div class="wait-box">
                    <div class="wait-label">次緊急/非緊急 (第4-5類)</div>
                    <div class="wait-value" style="color: #ef4444;">4 hours</div>
                    <div class="wait-p95">95%等候: 7 hours</div>
                </div>
            </div>
        </div>

        <div class="hospital-card">
            <div class="hospital-name">天水圍醫院</div>
            <div class="wait-times">
                <div class="wait-box">
                    <div class="wait-label">緊急 (第3類)</div>
                    <div class="wait-value" style="color: #22c55e;">15 minutes</div>
                    <div class="wait-p95">95%等候: 30 minutes</div>
                </div>
                <div class="wait-box">
                    <div class="wait-label">次緊急/非緊急 (第4-5類)</div>
                    <div class="wait-value" style="color: #ef4444;">2 hours</div>
                    <div class="wait-p95">95%等候: 5 hours</div>
                </div>
            </div>
        </div>

        <div class="hospital-card">
            <div class="hospital-name">瑪麗醫院</div>
            <div class="wait-times">
                <div class="wait-box">
                    <div class="wait-label">緊急 (第3類)</div>
                    <div class="wait-value" style="color: #eab308;">30 minutes</div>
                    <div class="wait-p95">95%等候: 54 minutes</div>
                </div>
                <div class="wait-box">
                    <div class="wait-label">次緊急/非緊急 (第4-5類)</div>
                    <div class="wait-value" style="color: #ef4444;">2 hours</div>
                    <div class="wait-p95">95%等候: 4 hours</div>
                </div>
            </div>
        </div>

        <div class="hospital-card">
            <div class="hospital-name">廣華醫院</div>
            <div class="wait-times">
                <div class="wait-box">
                    <div class="wait-label">緊急 (第3類)</div>
                    <div class="wait-value" style="color: #ef4444;">50 minutes</div>
                    <div class="wait-p95">95%等候: 120 minutes</div>
                </div>
                <div class="wait-box">
                    <div class="wait-label">次緊急/非緊急 (第4-5類)</div>
                    <div class="wait-value" style="color: #ef4444;">3.5 hours</div>
                    <div class="wait-p95">95%等候: 7 hours</div>
                </div>
            </div>
        </div>

        <div class="hospital-card">
            <div class="hospital-name">將軍澳醫院</div>
            <div class="wait-times">
                <div class="wait-box">
                    <div class="wait-label">緊急 (第3類)</div>
                    <div class="wait-value" style="color: #eab308;">26 minutes</div>
                    <div class="wait-p95">95%等候: 71 minutes</div>
                </div>
                <div class="wait-box">
                    <div class="wait-label">次緊急/非緊急 (第4-5類)</div>
                    <div class="wait-value" style="color: #ef4444;">7 hours</div>
                    <div class="wait-p95">95%等候: 9 hours</div>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>醫管局實時數據。第3類最常見於生病小朋友。</p>
            <small>data.gov.hk - Hospital Authority<br>Haruki Robotics Lab</small>
        </div>
    </div>
</body>
</html>
