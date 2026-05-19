import pandas as pd
import os

def clean_data(file_path):

    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['Date'])

    df = df.sort_values(by='Date')

    df = df.fillna(method='ffill')

    return df


if __name__ == "__main__":

    # create processed folder automatically
    os.makedirs("data/processed", exist_ok=True)

    df = clean_data("data/raw/apple_stock.csv")

    df.to_csv("data/processed/apple_clean.csv", index=False)

    print("Data cleaned successfully")