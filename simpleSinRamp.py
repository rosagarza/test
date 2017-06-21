# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:18:56 2017

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

#for ramp
upAmp=[t/(numOfSecs*samplesPerSec) for t in range(int((numOfSecs*samplesPerSec)))] #getting equal intervals of 1/Hz
myUpSig=upAmp*np.sin(2*pi*freq*t) #for linearity 

########## SCALING TO WRITE WAV FILES #######################
# range -32768 to 32767 and cast to 16-bit integers as so:
scaledUp=np.int16(myUpSig*maxInt)

#######################################################
########## WRITING THE WAV FILES ######################
#######################################################

###### Ramp of sine function (Amp. Increasing.) ##########
fw2=wave.openfp('sampleSinRamp.wav','wb')
fw2.setnframes(samplesPerSec)
fw2.setsampwidth(2)
fw2.setnchannels(1) #mono
fw2.setframerate(samplesPerSec)
data2 =scaledUp
fw2.writeframesraw(data2)
fw2.close()

################################################
############# PLaying Audio in real time #######
################################################
chunk=1024
ramp_play=wave.open('sampleSinRamp.wav','rb')
p=pyaudio.PyAudio()

stream=p.open(format=p.get_format_from_width(ramp_play.getsampwidth()),channels=ramp_play.getnchannels(),rate=ramp_play.getframerate(),output=True)
data=ramp_play.readframes(chunk)

while data:
    stream.write(data)
    data=ramp_play.readframes(chunk)
stream.stop_stream()
stream.close()