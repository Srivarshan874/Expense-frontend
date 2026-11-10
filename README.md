# SpendWise 💳 — Mobile Expense & Cash Flow Tracker

SpendWise is a responsive, feature-rich **Mobile App Expense Tracker** designed for fast expense logging, credit/debit tracking, ledger history, and rich **date-wise visualizations**.

It is built with **Modern Web Standards (PWA)**, featuring an interactive **Mobile Phone Frame preview** (iPhone 16 Pro mockup with Dynamic Island, status bar, and gesture indicator) alongside a full-screen desktop mode, offline LocalStorage persistence, and responsive touch controls.

---

## 🌟 Key Features

### 1. 💳 Credit & Debit Cash Flow Management
- **Debit (Outflow / Expenses)**: Visualized in vibrant rose (`#ef4444`) with category tags and transaction details.
- **Credit (Inflow / Income)**: Visualized in emerald green (`#10b981`) for salary, freelance gigs, dividends, and refunds.
- **Live Net Balance**: Automatically computes total cash flow position, net savings rate `%`, and monthly budget health.

### 2. 📅 Date-wise Expense Visualizations & Analytics
- **Daily Outflow Bar Charts**: Day-by-day expense bars with touch/hover tooltips, daily averages, and peak spend markers.
- **Credit vs. Debit Cash Flow Pillars**: Side-by-side grouped inflow vs. outflow comparison bars for any selected time window.
- **Interactive Calendar Heatmap**: Monthly calendar with color-coded transaction dots (🟢 Credit, 🔴 Debit). Tap any day to inspect that date's ledger and net total.
- **Category Spending Donut**: Clean SVG breakdown of where funds were spent (Food, Shopping, Housing, Transport, Utilities, etc.).
- **Quick Date Range Filters**: Last 7 Days, Last 30 Days, This Month, Last Month, and All Time.

### 3. 📜 Transaction History & Ledger
- **Date Grouping**: Transactions grouped under friendly date banners ("Today, Nov 10", "Yesterday, Nov 9", etc.) with daily net sum badges.
- **Live Search & Filter**: Real-time search across titles, notes, and payment methods.
- **Filter Tabs**: Quickly toggle between **All**, **Debits Only**, or **Credits Only**.
- **Category & Method Filters**: Filter by specific categories and payment types (Credit Card, UPI / Wallet, Cash, Bank Transfer).
- **Sort Options**: Newest first, Oldest first, Highest amount, Lowest amount.

### 4. ➕ Quick Add / Edit Modal & Fast Chips
- Segmented type toggle: **Debit (Expense)** vs **Credit (Income)**.
- Fast amount increment chips (`+10`, `+50`, `+100`, `+500`).
- Quick title suggestion chips ("Groceries", "Coffee", "Salary", "Uber", "Rent", "Dinner", "Netflix").
- Category grid with 15+ curated categories, distinctive emoji icons, and color tints.
- Date and time pickers with payment method dropdown.

### 5. 🎯 Budgets, Portability & Offline PWA
- **Monthly Budget Tracker**: Configurable monthly spending target with color-changing progress gauge.
- **Multi-Currency Support**: Switch on-the-fly between USD (`$`), INR (`₹`), EUR (`€`), GBP (`£`), JPY (`¥`), and CAD (`C$`).
- **Data Export & Import**:
  - Export ledger to **CSV** (for Excel / Google Sheets).
  - Export & restore complete **JSON backups**.
  - One-tap "Reset to Sample Data" or "Clear All".
- **Offline PWA**: Includes `manifest.json` and `sw.js` (Service Worker) so you can install it on your mobile device's home screen.

---

## 🚀 How to Run Locally

You can run SpendWise with Python or any local web server:

### Option 1: Python HTTP Server (Recommended)
```bash
cd ./expense-tracker-app
python3 server.py
```
Open **[http://localhost:5173](http://localhost:5173)** in your browser!

### Option 2: Directly Open in Browser
Double-click `index.html` or open it directly in Safari / Chrome:
```bash
open ./expense-tracker-app/index.html
```

---

## 📱 Installing on Mobile (iOS / Android)

1. Open the URL in Safari on your iPhone or Chrome on Android.
2. **On iPhone (iOS)**: Tap the **Share** button at the bottom of Safari, then tap **Add to Home Screen**.
3. **On Android**: Tap the three dots menu in Chrome, then tap **Install App** or **Add to Home Screen**.
4. SpendWise will launch full-screen as a standalone native app!

---

## 📂 Project Structure

```
expense-tracker-app/
├── index.html          # Core single-page application & mobile shell
├── manifest.json       # PWA manifest for mobile installation
├── sw.js               # Service Worker for offline caching
├── server.py           # Lightweight local server with CORS
├── package.json        # Project metadata and quick npm scripts
└── README.md           # Documentation and guide
```
