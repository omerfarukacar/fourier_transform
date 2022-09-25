
import numpy as np
import matplotlib.pyplot as plotter 

# Örnekleme Sıklığı
SAMPLE_FREQUENCY  = 200

# Zaman noktaları örneklenmesi
SAMPLE_INTERVAL = 1 / SAMPLE_FREQUENCY 

# Sinyalin başlangıç ve bitiş zamanı
START_TIME   = 0
END_TIME     = 10 
PI = np.pi

# Sinyal frekansları
FREQ_1   = 3
FREQ_2   = 7 

# Zaman noktaları
TIME = np.arange(START_TIME, END_TIME, SAMPLE_INTERVAL) 

# 2 Sinüs dalgası oluşturulur
AMPLITUDE_1 = np.sin(2*PI*FREQ_1*TIME)
AMPLITUDE_2 = np.sin(2*PI*FREQ_2*TIME) 

# Gösterilecek tablolar
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=3) 

# Sinüs 1 dalgası için zaman alanı gösterimi
axis[0].set_xlabel('Zaman')
axis[0].set_ylabel('Genlik') 
axis[0].set_title(f"{FREQ_1} Hz'lik sinyal frekansı")
axis[0].plot(TIME, AMPLITUDE_1)

# Sinüs 2 dalgası için zaman alanı gösterimi
axis[1].set_xlabel('Zaman')
axis[1].set_ylabel('Genlik') 
axis[1].set_title(f"{FREQ_2} Hz'lik sinyal frekansı")
axis[1].plot(TIME, AMPLITUDE_2)

# Sinüs dalgaları toplamı
TOTAL_AMPLITUDE = AMPLITUDE_1 + AMPLITUDE_2 

# Elde edilen sinüs dalgasının zaman alanı gösterimi
axis[2].set_xlabel('Zaman')
axis[2].set_ylabel('Genlik') 
axis[2].set_title('Toplam sinüs dalgası')
axis[2].plot(TIME, TOTAL_AMPLITUDE)

# Frekans alanı gösterimi
FOURIER_TRANSFORM = np.fft.fft(TOTAL_AMPLITUDE)/len(TOTAL_AMPLITUDE)
FOURIER_TRANSFORM = FOURIER_TRANSFORM[range(int(len(TOTAL_AMPLITUDE)/2))]
 

FOURIER_ARRAY      = np.arange(int(len(TOTAL_AMPLITUDE)/2))  # bir aralık içinde eşit aralıklı değerler içeren ndarray nesnesi 
TIME_PERIOD  = len(TOTAL_AMPLITUDE)/SAMPLE_FREQUENCY
FOURIER_FREQUENCY = FOURIER_ARRAY/TIME_PERIOD 

# Frekans alanı gösterimi
axis[3].set_xlabel('Frekans')
axis[3].set_ylabel('Genlik')
axis[3].set_title('Fourier dönüşümü')
axis[3].plot(FOURIER_FREQUENCY, abs(FOURIER_TRANSFORM))

plotter.show()