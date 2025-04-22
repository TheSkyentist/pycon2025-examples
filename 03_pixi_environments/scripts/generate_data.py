import numpy as np
import os

# Create random numbers
rng = np.random.default_rng(seed=42) 

# Generate random data
data = rng.random((100, 5))  # 100 rows

# Create directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Create array with numpy 1.21.0 specific functionality
np.savetxt('data/raw_data.csv', data, delimiter=',', fmt='%.4f')