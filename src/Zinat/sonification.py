import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


#import pandas as pd
#
## Load CSV file
#df = pd.read_csv('amplitude.csv')
#
#print("Column name:", df.columns)
#
## Rename first column to sample if needed
#df.rename(columns={'Unnamed: 0': 'sample'}, inplace=True)
#
## plot and sound
#
#if df['amplitude'].dtype == 'object':  # Verify if it is an object
#    df[['amplitude1', 'amplitude2', 'amplitude3']] = df['amplitude'].astype(str).str.split(',', expand=True)
#    df.drop('amplitude', axis=1, inplace=True)
#
#df.to_csv('new_file_project.csv', index=False)
#
#print("CSV File has been processed and saved as new_file.csv.")
#







# Make sine wave signals from arrays of frequencies and amplitudes
filename = 'Beat'
outfile = './'
TargetDuration = 2  # [s] length of signal


# Example input arrays (these should be replaced with our actual data)
fsig_array = np.array([200.9, 210.8, 220.7])  # Example frequencies [Hz]
A_array = np.array([0.5, 0.3, 0.7])  # Example amplitudes [float]

#df = pd.read_csv('amplitude.csv')
#tsig_array = df['time'].values  # Frequency sampling values
#
#
#if np.any(tsig_array == 0):
#    print("Warning: Found zeros in tsig_array, replacing them with a small value.")
#    tsig_array = np.where(tsig_array == 0, 1e-10, tsig_array)  # Replace zeros with a small value
#
#fsig_array = 1 / tsig_array
#



#A_array = df['amplitude'].astype(float).values  # Amplitude values


pi = np.pi

# Sampling frequency must be at least 2x the maximum frequency
fs = 5 * np.max(fsig_array)

# Build time axis for target duration
t = np.arange(0, TargetDuration, 1/fs)

# Initialize an empty array for the combined signal
combined_signal = np.zeros_like(t)

# Generate sine wave signals for each frequency and amplitude
for fsig, A in zip(fsig_array, A_array):
    # Generate the sine wave signal
    x = 2 * pi * fsig * t
    y = A * np.sin(x)

    # Combine the signal with a Hanning window
    window = np.hanning(len(t))  # Use NumPy's Hanning window
    y_windowed = y * window

    # Add the windowed signal to the combined signal
    combined_signal += y_windowed

# Play the audio
sd.play(combined_signal, fs)
sd.wait()  # Wait until the sound has finished playing

# Create a plot for the waveform
plt.figure("Sonification")
plt.title('Combined Sine Waves')
plt.plot(t, combined_signal)  # Use the original time array
plt.title('Combined Sine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


