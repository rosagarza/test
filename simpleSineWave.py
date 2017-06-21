# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:04:16 2017

@author: Rosa
"""
import numpy as np
from numpy import pi
import math,struct
import scipy.io.wavfile
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
import wave
import pyaudio


samplesPerSec = 44100
freq=400
numOfSecs = 1.5
maxInt=32767.0 #Max number of 16 bits

t = np.float32(np.arange(0, numOfSecs*samplesPerSec, dtype=float))/samplesPerSec
      
mySignal=np.sin(2*pi*t*freq)

########## SCALING TO WRITE WAV FILES #######################
# range -32768 to 32767 and cast to 16-bit integers as so:
scaled=np.int16(mySignal*maxInt)

#######################################################
########## WRITING THE WAV FILES ######################
#######################################################

######## Basic sine wave ########
fw=wave.openfp('sampleSin.wav','wb')
fw.setnframes(samplesPerSec)
fw.setsampwidth(2) #amount of bytes, 8bits/byte
fw.setnchannels(1) #mono-1 stereo-2
fw.setframerate(samplesPerSec)
data = scaled
fw.writeframesraw(data)
fw.close()


################################################
############# PLaying Audio in real time #######
################################################
chunk=1024
sin_play=wave.open('sampleSin.wav','rb')
p=pyaudio.PyAudio()

stream=p.open(format=p.get_format_from_width(sin_play.getsampwidth()),channels=sin_play.getnchannels(),rate=sin_play.getframerate(),output=True)
data=sin_play.readframes(chunk)

while data:
    stream.write(data)
    data=sin_play.readframes(chunk)
stream.stop_stream()
stream.close()
