import dask.dataframe as dd
import os

os.makedirs('results', exist_ok=True)

ddf = dd.read_csv('results/processed_pandas.csv', header=None)

result = ddf.mean().compute() * 2  # Older compute() syntax

# Save report
with open('results/final_analysis.html', 'w') as f:
    f.write("<h1>Analysis Report</h1>")
    f.write(f"<pre>Doubled means:\n{result.to_string()}</pre>")