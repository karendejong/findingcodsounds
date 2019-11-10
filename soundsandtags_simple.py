import os as os
from pathlib import Path
import math
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy import signal
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import numpy as np



data_folder = Path('/home/a5541/spawnseis_pilot/')

text_file_1 = data_folder/"20180305_180000.csv"


# ## README: This script only works for 1-channel wav.files. (Only use this part for unprepared files).
#
# # filter and downsample
# import parselmouth
# from parselmouth.praat import call
#
# # define band-pass filter lowcut-highcut (for more complex filters)
# def butter_bandpass(lowcut, highcut, fs, order=5):
#     nyq = 0.5 * fs
#     low = lowcut / nyq
#     high = highcut / nyq
#     b, a = butter(order, [low, high], btype='band')
#     return b, a
#
#
# def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
#     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y
#
# # import sound file
# sound_file_original = data_folder/"20180305_180000_ch1.wav"
# sample_rate, samples = scipy.io.wavfile.read(sound_file_original)
# print(sample_rate)
#
# # # Define sample rate and desired cutoff frequencies (in Hz).
# # fs = sample_rate
# # lowcut = 5.0
# # highcut = 600.0
# #
# # # # plot the original signal. to check if it imported properly
# # plt.figure(2)
# # plt.clf()
# # plt.plot(samples, label='Noisy signal')
# #
# # # Filter the signal.
# # y = butter_bandpass_filter(samples, lowcut, highcut, fs, order=3)
#
# # # plot the filtered signal to check if filter works
# # f0 = 1000.0
# # b, a = butter_bandpass(lowcut, highcut, fs, order=3)
# # plt.plot(y, label='Filtered signal (%g Hz)' % f0)
# # plt.xlabel('time (seconds)')
# # plt.hlines([-a, a], 0, T, linestyles='--')
# # plt.grid(True)
# # plt.axis('tight')
# # plt.legend(loc='upper left')
#
# # Filter sound with praat using parselmouth
# sound = parselmouth.Sound('/home/a5541/spawnseis_pilot/20180305_180000_ch1.wav')
# sound_filtered = call(sound, "Filter (pass Hann band)", 0.0, 600.0, 10.0)
# sound_filtered.save('/home/a5541/spawnseis_pilot/20180305_180000_ch1filt.wav', "WAV")
#
# # Down sample filtered sound file with praat via parselmouth
# sound_resampled = call(sound_filtered, "Resample", 1200, 50)
# type(sound_resampled)
# sound_resampled.save("/home/a5541/spawnseis_pilot/20180305_180000_ch1frs.wav", "WAV")


# import sound file
sound_file_1 = data_folder/"20180305_180000_ch1frs.wav"
sample_rate, samples = scipy.io.wavfile.read(sound_file_1)
print(sample_rate)

#Create spectrogram if needed
# freqs, times, spectrogram = signal.spectrogram(samples,
#                                                fs=sample_rate,
#                                                nperseg=100,
#                                                window='hamming',
#                                                noverlap=50,
#                                                detrend=False)

# Import labels from text file
times_sounds = pd.read_csv('/home/a5541/spawnseis_pilot/20180305_180000_gruntint.csv')
times_sounds.drop('text', axis=1, inplace=True)
times_sounds_fs = times_sounds * sample_rate
times_sounds_fsr = times_sounds_fs.applymap(math.ceil)
times_sounds_fsr['length'] = times_sounds_fsr['tmax']-times_sounds_fsr['tmin']
print("min length:",min(times_sounds_fsr['length']),", max length:",max(times_sounds_fsr['length']))
print("max t grunt:",max(times_sounds_fsr['tmax']), ", max t file:",samples.shape)
numbergrunts = times_sounds_fsr.shape[0]

vector_labels = np.zeros(samples.shape)
vector_labels.shape
sum(vector_labels)
for x in range(0,numbergrunts):
    vector_labels[times_sounds_fsr.iat[x,0]:times_sounds_fsr.iat[x,1]] = 1
    print(x)

#Show vector labels (to compare to Praat)
plt.plot(vector_labels)
print("total grunt length:",sum(times_sounds_fsr['length']), ", total number of ones:",sum(vector_labels))