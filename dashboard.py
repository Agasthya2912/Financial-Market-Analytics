import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(layout="wide")

st.title("📊 Financial Market Analytics Dashboard")

# -------------------------
# STOCK SELECTOR
# -------------------------

stocks = ["AAPL", "TSLA", "MSFT", "GOOGL"]

selected_stock = st.selectbox(
    "Select Stock",
    stocks
)

# -------------------------
# DATE RANGE
# -------------------------

start_date = st.date_input("Start Date", pd.to_datetime("2018-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-01-01"))

# -------------------------
# DOWNLOAD DATA
# -------------------------

data = yf.download(selected_stock, start=start_date, end=end_date)

# Moving averages
data["MA10"] = data["Close"].rolling(10).mean()
data["MA50"] = data["Close"].rolling(50).mean()

# =====================================================
# ROW 1
# Price Trend | Moving Averages
# =====================================================

col1, col2 = st.columns(2)

with col1:
    st.subheader("Price Trend")
    st.line_chart(data["Close"])

with col2:
    st.subheader("Moving Averages")

    fig_ma, ax_ma = plt.subplots(figsize=(6,3))

    ax_ma.plot(data["Close"], label="Close")
    ax_ma.plot(data["MA10"], label="10 Day MA")
    ax_ma.plot(data["MA50"], label="50 Day MA")

    ax_ma.legend()

    st.pyplot(fig_ma)

# =====================================================
# MACHINE LEARNING PREDICTION
# =====================================================

df = data.dropna()

X = df[["MA10","MA50"]]
y = df["Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

# =====================================================
# CORRELATION DATA
# =====================================================

tech_stocks = ["AAPL","TSLA","MSFT","GOOGL"]

multi_data = yf.download(
    tech_stocks,
    start=start_date,
    end=end_date
)["Close"]

returns = multi_data.pct_change().dropna()

corr_matrix = returns.corr()

# =====================================================
# ROW 2
# Prediction | Heatmap
# =====================================================

col3, col4 = st.columns(2)

with col3:

    st.subheader("ML Prediction (Actual vs Predicted)")

    fig_pred, ax_pred = plt.subplots(figsize=(6,3))

    ax_pred.plot(y_test.values,label="Actual")
    ax_pred.plot(predictions,label="Predicted")

    ax_pred.legend()

    st.pyplot(fig_pred)

with col4:

    st.subheader("Correlation Heatmap")

    fig_heat, ax_heat = plt.subplots(figsize=(5,4))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax_heat
    )

    st.pyplot(fig_heat)

# =====================================================
# PORTFOLIO RISK
# =====================================================

st.subheader("Portfolio Risk Metrics")

volatility = returns.std() * (252 ** 0.5)

risk_df = pd.DataFrame({
    "Stock": volatility.index,
    "Annualized Volatility": volatility.values
})

st.dataframe(risk_df)

fig_risk, ax_risk = plt.subplots(figsize=(6,3))

ax_risk.bar(volatility.index, volatility.values)

ax_risk.set_ylabel("Volatility")

st.pyplot(fig_risk)

# =====================================================
# INSIGHTS
# =====================================================

st.subheader("Portfolio Insights")

st.write("""
• Apple, Microsoft and Google show strong correlation  
• Tesla often has lower correlation with Big Tech  
• Lower correlation stocks improve diversification  
• Higher volatility means higher investment risk
""")