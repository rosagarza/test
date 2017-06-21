# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:14:12 2017

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
squareSig=(np.greater(np.sin(2*pi*t*freq),0,))*1

########## SCALING TO WRITE WAV FILES #######################
# range -32768 to 32767 and cast to 16-bit integers as so:
scaledSquare=np.int16(squareSig*maxInt)

#######################################################
########## WRITING THE WAV FILES ######################
#######################################################

###### Square wave ################
##Be sure to time numOfSecs=10 to hear it
square=wave.openfp('sampleSquare.wav','wb')
square.setnframes(samplesPerSec)
square.setsampwidth(2)
square.setnchannels(1) #mono
square.setframerate(samplesPerSec)
s = scaledSquare
square.writeframesraw(s)
square.close()

################################################
############# PLaying Audio in real time #######
################################################
chunk=1024
square_play=wave.open('sampleSquare.wav','rb')
p=pyaudio.PyAudio()

stream=p.open(format=p.get_format_from_width(square_play.getsampwidth()),channels=square_play.getnchannels(),rate=square_play.getframerate(),output=True)
data=square_play.readframes(chunk)

while data:
    stream.write(data)
    data=square_play.readframes(chunk)
stream.stop_stream()
stream.close()