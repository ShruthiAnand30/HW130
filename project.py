import csv
import pandas as pd
df = pd.read_csv("total_stars.csv")

print(df.columns)
final_data = df.dropna()
final_data.reset_index(drop = True, inplace = True)

final_data.to_csv("final_data.csv")