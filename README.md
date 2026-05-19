# 📊 Financial Market Analytics & Prediction Dashboard

An end-to-end **Financial Market Data Analytics System** built using **Python, Machine Learning, SQL, and Streamlit** to analyze stock market trends, predict stock prices, and evaluate portfolio risk through interactive visualizations.

---

# 🚀 Project Overview

This project collects historical stock market data from Yahoo Finance, performs data preprocessing and feature engineering, applies machine learning techniques for price prediction, and visualizes financial insights through an interactive Streamlit dashboard.

The dashboard enables users to:

- Analyze stock price trends
- View moving averages
- Predict stock prices using Machine Learning
- Compare stock correlations
- Evaluate portfolio risk and volatility

---

# 🧠 Features

## 📥 Data Collection
- Fetches historical stock data using Yahoo Finance API (`yfinance`)
- Supports multiple stocks:
  - Apple (AAPL)
  - Tesla (TSLA)
  - Microsoft (MSFT)
  - Google (GOOGL)

---

## 🧹 Data Preprocessing
- Handles missing values
- Converts date formats
- Cleans and structures financial time-series data

---

## ⚙️ Feature Engineering
- 10-Day Moving Average
- 50-Day Moving Average
- Daily Returns
- Volatility Metrics

---

## 🤖 Machine Learning
- Linear Regression model for stock price prediction
- Actual vs Predicted price visualization
- Time-series forecasting workflow

---

## 📊 Financial Analytics
- Stock trend analysis
- Portfolio correlation analysis
- Volatility/risk analysis
- Correlation heatmaps

---

## 🌐 Interactive Dashboard
Built using **Streamlit** with:
- Stock selector
- Date range filtering
- Interactive charts
- Correlation heatmaps
- Portfolio insights

---

# 🏗️ System Architecture

```text
Yahoo Finance API
        ↓
Data Collection
        ↓
Data Cleaning & Preprocessing
        ↓
Feature Engineering
        ↓
SQL Database Storage
        ↓
Machine Learning Prediction
        ↓
Financial Visualization
        ↓
Streamlit Dashboard
```

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Data Analysis
- Pandas
- NumPy

## Machine Learning
- Scikit-learn

## Visualization
- Matplotlib
- Seaborn

## Dashboard
- Streamlit

## Database
- SQLite
- SQLAlchemy

## Financial Data API
- yfinance

---

# 📂 Project Structure

```text
financial-market-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── store_to_sql.py
│   ├── model_training.py
│   └── visualization.py
│
├── dashboard.py
├── requirements.txt
└── README.md
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/financial-market-analytics.git
cd financial-market-analytics
```

---

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Dashboard

```bash
streamlit run dashboard.py
```

Open in browser:

```text
http://localhost:8501
```

---

# 📈 Dashboard Features

## 📊 Price Trend Analysis
Visualizes stock closing prices over time.

## 📉 Moving Averages
Displays:
- 10-Day Moving Average
- 50-Day Moving Average

Used for trend analysis and momentum detection.

---

## 🤖 ML Prediction Chart
Compares:
- Actual Stock Prices
- Predicted Stock Prices

---

## 🔥 Correlation Heatmap
Analyzes relationships between:
- AAPL
- TSLA
- MSFT
- GOOGL

Useful for portfolio diversification analysis.

---

## ⚠️ Portfolio Risk Metrics
Calculates annualized volatility to evaluate stock risk.

---

# 🎯 Applications

- Financial Market Analysis
- Portfolio Risk Management
- Investment Research
- FinTech Analytics Platforms
- Stock Trend Forecasting

---

# 👨‍💻 Author

**Agasthya N**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!
