import os                                           #needed to play wavfile from os command
from scipy import *
from scipy.io.wavfile import *
from pylab import *

# Amplitude Modulation of a wavfile
fmod=12800

# Load sound
[Fe,signal]=read('../sounds/daftpunk.wav')           #read wavfile


# Apply modulation
N=len(signal)                                       #length of the signal
t=arange(N)/Fe                                      #create time base
modulator=sin(2*pi*fmod*t)                          #create modulator
output_signal=modulator*signal                      #reverse sound

# Save File
write('daftpunk_FX2.wav',Fe,output_signal)          #save wavefile

# Play Reverse sound with default OS player
os.system("open daftpunk_FX2.wav")

# Display Signal
plot(t,output_signal)
xlabel('Time (s)')
ylabel('Amplitude')
show()


