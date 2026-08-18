import pandas as pd

file_path = "D:/CodeAlpha/CodeAlpha_DataVisualization/dataset/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("Dataset loaded successfully!")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())