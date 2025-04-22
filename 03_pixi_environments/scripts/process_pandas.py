# Requires pandas=1.3.0 (incompatible with numpy 2.0+)
import pandas as pd
import os

os.makedirs('results', exist_ok=True)

df = pd.read_csv('data/raw_data.csv', header=None)

df = df.apply(lambda x: x*100)  # Older apply behavior
df.to_csv('results/processed_pandas.csv', index=False)