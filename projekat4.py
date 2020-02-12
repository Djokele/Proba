import IPython
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io

#ucitavanje zvuka
wav_loc = "C:/Users/Djordje/Desktop/download.wav"
rate, data = wavfile.read(wav_loc)
data = data / 32768

IPython.display.Audio(data=data, rate=rate)

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)

#dodavanje suma
noise_len = 2 # sekunde
noise = band_limited_noise(min_freq=2000, max_freq = 12000, samples=len(data), samplerate=rate)*10
noise_clip = noise[:rate*noise_len]
audio_clip_band_limited = data+noise

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(audio_clip_band_limited)


IPython.display.Audio(data=audio_clip_band_limited, rate=rate)

#uklanjanje suma
noise_reduced = nr.reduce_noise(audio_clip=audio_clip_band_limited, noise_clip=noise_clip, prop_decrease=1.0, verbose=True)

#zvuk posle uklonjenog suma
fig, ax = plt.subplots(figsize=(20,3))
ax.plot(noise_reduced)

IPython.display.Audio(data=noise_reduced, rate=rate)

