import pandas as pd
import ast

# Path of the input CSV file
input_csv_file_path = 'amplitude.csv'  # Change this to the path of your CSV file
# Path of the output CSV file
output_csv_file_path = 'clean_data.csv'  # Change this to the path where you want to save the new CSV file

# Read the CSV file, specify dtype for safety
data = pd.read_csv(input_csv_file_path, header=None, dtype=str)  # Read all data as strings

# Create lists to store the data
sample_numbers = []
timestamps = []
amplitudes = []

# Process each row of the dataframe
for row in data[0]:
    try:
        # Convert the string representation of the array to a list
        array_data = ast.literal_eval(row)

        # Extract elements from the array
        sample_number = array_data[0]
        timestamp = array_data[1]
        amplitude = array_data[2]

        # Add the data to the lists
        sample_numbers.append(sample_number)
        timestamps.append(timestamp)
        amplitudes.append(amplitude)

    except (ValueError, SyntaxError) as e:
        # Ignore rows that are invalid and print the error
        print(f"Ignored row (not valid): {row} | Error: {e}")

# Create a new DataFrame with the processed data
output_data = pd.DataFrame({
    'Sample Number': sample_numbers,
    'Timestamp': timestamps,
    'Amplitude': amplitudes
})

# Save the new DataFrame as a CSV file
output_data.to_csv(output_csv_file_path, index=False)

print(f"Generated CSV file: {output_csv_file_path}")
