import os                                           #needed to play wavfile from os command
from scipy import *
from scipy.io.wavfile import *
from pylab import *

#Reverse sound FX. The effect is obtained by reversing the array containing the audio samples

# Load sound
[Fe,signal]=read('../sounds/daftpunk.wav')          #read wavfile

# Reverse sound
output_signal=flipud(signal)                        #reverse sound

# Save File
write('daftpunk_FX1.wav',Fe,output_signal)           #save wavefile

# Play Reverse sound with default OS player
os.system("open daftpunk_FX1.wav")

# Display Signal
N=len(signal)                                       #length of the signal
t=arange(N)/Fe                                      #create time base
plot(t,output_signal)
xlabel('Time (s)')
ylabel('Amplitude')
show()


