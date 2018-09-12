print("hello python")

import numpy
import scipy
from scipy import signal
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile



# random signal for testing
# numpy.random.seed(0)
#
# time_step = .01
# time_vec = numpy.arange(0, 70, time_step)
#
# # A signal with a small frequency chirp
# sig = numpy.sin(0.5 * numpy.pi * time_vec * (1 + .1 * time_vec))

# various ways of reading real signal from wav file to spectrogram

#simplest way
sample_rate, samples = scipy.io.wavfile.read('sounds_library/cod_grunts/ML_cod1.wav')

# Spectrogram of .wav file
freqs, times, spec_data = signal.spectrogram(samples, sample_rate)
# Note sample_rate and sampling frequency values are same but theoretically they are different measures

# Use matplot library to visualize the spectrogram
plt.pcolormesh(times, freqs, spec_data )
plt.title('simple spectrogram')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#more complicated - smaller frequency band
plt.pcolormesh(times, freqs, spec_data)
plt.imshow(spec_data, aspect='auto', cmap='hot_r', origin='lower')
plt.title('Spectrogram')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.tight_layout()
plt.show()

#log-plot
def log_specgram(samples, sample_rate, window_size = 20,
                 step_size = 10, eps = 1e-10):
    nperseg = int(round(window_size * sample_rate / 1e3))
    noverlap = int(round(step_size * sample_rate / 1e3))
    freqs, times, spec = signal.spectrogram(samples,
                                    fs=sample_rate,
                                    nperseg=nperseg,
                                    window='hamming',
                                    noverlap=noverlap,
                                    detrend=False)
    return freqs, times, numpy.log(spec.T.astype(numpy.float32) + eps)
print(freqs)

freqs, times, spectrogram = log_specgram(samples, sample_rate)

plt.imshow(spectrogram.T, aspect='auto', origin='lower')
plt.axis('off')
plt.title('log_scale')
plt.show()



# plt.figure(figsize=(8, 5))
# plt.plot(time_vec, sig)
# plt.show()
#
# freqs, times, spectrogram = signal.spectrogram(sig)
#
# plt.figure(figsize=(5, 4))
# plt.imshow(spectrogram, aspect='auto', cmap='hot_r', origin='lower')
# plt.title('Spectrogram')
# plt.ylabel('Frequency band')
# plt.xlabel('Time window')
# plt.tight_layout()
# plt.show()
#
# freqs, psd = signal.welch(sig)
#
# plt.figure(figsize=(5, 4))
# plt.semilogx(freqs, psd)
# plt.title('PSD: power spectral density')
# plt.xlabel('Frequency')
# plt.ylabel('Power')
# plt.tight_layout()
# plt.show()
