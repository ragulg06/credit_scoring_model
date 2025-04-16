import pandas as pd

# Define the path to your .data file
data_file_path = 'german.data'

# Define the path for the output CSV file
csv_file_path = 'output_file.csv'

# Read the .data file
# Assuming the data is space-separated. Change the delimiter if necessary.
df = pd.read_csv(data_file_path, delimiter=' ', header=None)

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False, header=False)

print(f"Data has been converted and saved to {csv_file_path}")