import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/processed/apple_features.csv")

actual = df['Close'][-200:]

predicted = df['MA_10'][-200:]

plt.figure(figsize=(10,5))

plt.plot(actual.values, label="Actual")
plt.plot(predicted.values, label="Predicted")

plt.legend()

plt.title("Actual vs Predicted Prices")

plt.show()