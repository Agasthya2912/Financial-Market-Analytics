import pandas as pd
from sqlalchemy import create_engine
import os

# ensure data folder exists
os.makedirs("data", exist_ok=True)

# create database
engine = create_engine("sqlite:///data/stocks.db")

# load processed dataset
df = pd.read_csv("data/processed/apple_features.csv")

# store in SQL
df.to_sql(
    name="apple_stock_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully stored in SQL database")