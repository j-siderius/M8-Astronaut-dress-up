# import electrocardiogram
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram

# import numpy
import numpy as np

# define electrocardiogram as ecg model
ecg = electrocardiogram()

# frequency is 0
frequency = 360

# calculating time data with ecg size along with frequency
time_data = np.arange(ecg.size) / frequency

# plotting time and ecg model
plt.plot(time_data, ecg)
plt.xlabel("time in seconds")
plt.ylabel("ECG in milli Volts")
plt.xlim(9, 10.2)
plt.ylim(-1, 1.5)

# display
plt.show()
