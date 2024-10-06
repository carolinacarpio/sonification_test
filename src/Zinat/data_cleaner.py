import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import pandas as pd

# Load CSV file
df = pd.read_csv('amplitude.csv')

print("Column name:", df.columns)

# Rename first column to sample if needed
df.rename(columns={'Unnamed: 0': 'sample'}, inplace=True)

# plot and sound

if df['amplitude'].dtype == 'object':  # Verify if it is an object
    df[['amplitude1', 'amplitude2', 'amplitude3']] = df['amplitude'].astype(str).str.split(',', expand=True)
    df.drop('amplitude', axis=1, inplace=True)

df.to_csv('new_file_project.csv', index=False)

print("CSV File has been processed and saved as new_file.csv.")
