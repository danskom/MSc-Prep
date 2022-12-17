import numpy as np
import soundfile as sf

# Load the audio file into a numpy array
data, fs = sf.read('/Users/danielskomorowski/Dropbox/Project Equator/Atlantis/Self Control/Dum Waiter/Bounces/Project Equator - Atlantis (Ambotronic Mix).wav')

# Create a delay line with a delay of 0.5 seconds
delay_samples = int(fs * 0.5)
delay_line = np.zeros(delay_samples)

# Create the output array
output = np.zeros(len(data))

# Set the wet/dry mix
wet_dry_mix = 0.5

# Loop through the input samples and apply the reverb
for n, x in enumerate(data):
    output[n] = wet_dry_mix * x + (1 - wet_dry_mix) * delay_line[0]
    delay_line = np.roll(delay_line, -1)
    delay_line[-1] = x

# Write the output to a file
sf.write('output.wav', output, fs)
