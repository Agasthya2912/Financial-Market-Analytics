from sqlalchemy import create_engine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# correct database path
engine = create_engine("sqlite:///data/stocks.db")

# load data from SQL
df = pd.read_sql("SELECT * FROM apple_stock_data", engine)

# features
X = df[['Open','High','Low','Volume','MA_10','MA_50','Volatility']]
y = df['Close']

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)

print("Linear Regression RMSE:", mean_squared_error(y_test, pred_lr)**0.5)

# Random Forest
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)

print("Random Forest RMSE:", mean_squared_error(y_test, pred_rf)**0.5)