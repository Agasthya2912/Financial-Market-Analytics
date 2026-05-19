import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(stock_symbol, start_date, end_date):

    stock = yf.download(stock_symbol, start=start_date, end=end_date)
    stock.reset_index(inplace=True)

    return stock


if __name__ == "__main__":

    # create folders automatically
    os.makedirs("data/raw", exist_ok=True)

    data = fetch_stock_data("AAPL", "2015-01-01", "2024-01-01")

    data.to_csv("data/raw/apple_stock.csv", index=False)

    print("Data downloaded successfully")