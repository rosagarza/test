# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:10:15 2017

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
myOddSig= np.sin(2*pi*t*freq)+np.sin(2*pi*t*freq*3)/3 + np.sin(2*pi*t*freq*5)/5 + np.sin(2*pi*t*freq*7)/7 + np.sin(2*pi*t*freq*9)/9;

########## SCALING TO WRITE WAV FILES #######################
# range -32768 to 32767 and cast to 16-bit integers as so:
scaledOdd=np.int16(myOddSig*maxInt)

#######################################################
########## WRITING THE WAV FILES ######################
#######################################################

###### Odd (1,3,5,7,9) wave ################
##Be sure to time numOfSecs=10 to hear it
odd=wave.openfp('sampleOdd.wav','wb')
odd.setnframes(samplesPerSec)
odd.setsampwidth(2)
odd.setnchannels(1) #mono
odd.setframerate(samplesPerSec)
dataOdd = scaledOdd
odd.writeframesraw(dataOdd)
odd.close()


################################################
############# PLaying Audio in real time #######
################################################
chunk=1024
odd_play=wave.open('sampleOdd.wav','rb')
p=pyaudio.PyAudio()

stream=p.open(format=p.get_format_from_width(odd_play.getsampwidth()),channels=odd_play.getnchannels(),rate=odd_play.getframerate(),output=True)
data=odd_play.readframes(chunk)

while data:
    stream.write(data)
    data=odd_play.readframes(chunk)
stream.stop_stream()
stream.close()