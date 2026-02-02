# 🏥 Hong Kong A&E Wait Time Dashboard

A real-time emergency room wait time tracker for Hong Kong's 18 public hospitals. Clean, mobile-friendly interface that helps parents and patients find the fastest A&E during emergencies.


## 🎯 Why This Project?

When your child has a high fever at 2am, every minute counts. Hong Kong's official Hospital Authority website is clunky, requires multiple clicks, and isn't mobile-optimized. This dashboard solves that.

**Key Problems Solved:**
- ❌ Official site requires 5+ clicks to see all hospitals
- ❌ Not mobile-friendly during emergencies
- ❌ No clear visual indicators of wait times
- ❌ Confusing data presentation

**Our Solution:**
- ✅ All 18 hospitals on one screen
- ✅ Color-coded wait times (green = fast, red = slow)
- ✅ Sorted by Category 3 (most relevant for sick kids)
- ✅ Auto-refresh every 60 seconds
- ✅ Bilingual (繁體中文/English)
- ✅ Mobile-responsive design

## 📊 Features

### Real-Time Data
- Fetches live data from Hospital Authority's open data API
- Updates every 60 seconds automatically
- Shows last update timestamp

### Smart Sorting
- Hospitals sorted by **Category 3 median wait time**
- Category 3 = urgent cases (fever, vomiting, moderate pain)
- Most relevant for parents with sick children

### Color-Coded Wait Times
- 🟢 **Green** (≤20 min): Fast
- 🟡 **Yellow** (21-40 min): Moderate
- 🟠 **Orange** (41-60 min): Slow
- 🔴 **Red** (>60 min): Very slow

### Two Key Categories Displayed
1. **Category 3 (Urgent)**: Fever, vomiting, moderate injuries
2. **Category 4-5 (Semi-urgent/Non-urgent)**: Colds, rashes, minor cuts

### Dual Metrics
- **Median (50th percentile)**: Half of patients wait this long or less
- **95th percentile**: 95% of patients wait this long or less

### Bilingual Interface
- One-click toggle between 繁體中文 and English
- Hospital names in both languages

