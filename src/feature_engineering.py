import pandas as pd
import os

def create_features(file_path):

    df = pd.read_csv(file_path)

    # convert financial columns to numeric
    numeric_cols = ['Open','High','Low','Close','Volume']

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # moving averages
    df['MA_10'] = df['Close'].rolling(window=10).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()

    # daily return
    df['Daily_Return'] = df['Close'].pct_change()

    # volatility
    df['Volatility'] = df['Daily_Return'].rolling(window=10).std()

    df = df.dropna()

    return df


if __name__ == "__main__":

    os.makedirs("data/processed", exist_ok=True)

    df = create_features("data/processed/apple_clean.csv")

    df.to_csv("data/processed/apple_features.csv", index=False)

    print("Features created successfully")