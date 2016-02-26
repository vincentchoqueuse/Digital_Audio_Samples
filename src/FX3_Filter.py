import os                                           #needed to play wavfile from os command
from scipy import *
from scipy.signal import *
from scipy.io.wavfile import *
from pylab import *

# Filter effect

Q=0.5
fc=1200

# Load sound
[Fe,signal]=read('../sounds/daftpunk.wav')           #read wavfile

# Simple lowpass filter (see http://webaudio.github.io/web-audio-api/)
w0=2*pi*fc/Fe
alphaq=sin(w0)/(2*Q)
coef_a=[1+alphaq,-2*cos(w0),1-alphaq]
coef_b=[(1-cos(w0))/2,1-cos(w0),(1-cos(w0))/2]

#Analyse filter
figure("Transfer Function")
w, h = freqz(coef_b,coef_a)
semilogx(Fe*w/(2*pi), 20 * np.log10(abs(h)), 'b')
ylabel('Amplitude [dB]')
xlabel('Frequency [rad/sample]')
ylim(-40,30)

# Apply Filter
output_signal=lfilter(coef_b,coef_a,signal)

# Save File
write('daftpunk_FX3.wav',Fe,output_signal)          #save wavefile

# Play Reverse sound with default OS player
os.system("open daftpunk_FX3.wav")

# Display Signal
N=len(output_signal)
t=arange(N)/Fe
figure("Filtered output")
plot(t,signal)
xlabel('Time (s)')
ylabel('Amplitude')
show()


