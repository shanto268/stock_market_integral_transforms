import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

#import data
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
data = pd.read_csv('data.csv',sep=',', index_col='Date', parse_dates=['Date'], date_parser=dateparse).fillna(0)

#extract information
df_close = data['Close']
prices = df_close.to_numpy()

#Fourier Transform
amplitude = prices
days = np.array([i for i in range(amplitude.size)])

def showPlot()
    plt.figure(figsize=(10,6))
    plt.plot(days, amplitude)
    plt.xlabel('Days since stock IPO\'d')
    plt.ylabel('Close Prices')
    plt.title('Altaba Inc. closing price')
    plt.grid(True)
    plt.show()

samplingFrequency = 100
samplingInterval = 1 / samplingFrequency

fourierTransform = np.fft.fft(amplitude)/len(amplitude)           
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] 
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

plt.plot(frequencies, abs(fourierTransform))
plt.title('Fourier transform depicting the frequency components')
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()
