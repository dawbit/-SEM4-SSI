import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

class Dzwiek():
    def __init__(self, filename):
        self.filename = filename

    def amplituda(self):
        # Wersja pierwsza - skaluje dane do przedziału [-1, 1]
        rate, audioData = scipy.io.wavfile.read("cartoon001.wav")
        print("Rate:", rate)
        amount_of_samples = len(audioData)
        print("Liczba próbek:", amount_of_samples)

        time = np.arange(0, float(amount_of_samples), 1) / rate
        scaled_audioData = audioData / (2.**15)
        plt.plot(time, scaled_audioData, linewidth=0.01, alpha=0.7, color='#004bc6')
        plt.xlabel('Czas (s)')
        plt.ylabel('Amplituda')
        plt.show()

plik = Dzwiek('cartoon001.wav')
plik.amplituda()