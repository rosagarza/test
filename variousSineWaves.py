# * Creating audio of sine waves*-
"""
Created on Thu May 25 20:26:43 2017

@author: Rosa Garza
"""
import numpy as np
from numpy import pi
import math,struct
import scipy.io.wavfile
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
import wave

##NOTE: #samples per second are the "dots" in a line
#########frequency is how many periods per sec.

samplesPerSec = 44100
freq=400
numOfSecs = 1.5
maxInt=32767.0 #Max number of 16 bits

t = np.float32(np.arange(0, numOfSecs*samplesPerSec, dtype=float))/samplesPerSec

#printing is only practically useful if numberOfSeconds is very low (e.g. 0.005)
#print(t)

#mySignal = math.sin(2 * pi * t * 440)    ## this is a sine wave at 440Hz
mySignal=np.sin(2*pi*t*freq)
myOddSig= np.sin(2*pi*t*freq)+np.sin(2*pi*t*freq*3)/3 + np.sin(2*pi*t*freq*5)/5 + np.sin(2*pi*t*freq*7)/7 + np.sin(2*pi*t*freq*9)/9;
squareSig=(np.greater(np.sin(2*pi*t*freq),0,))*1
#for ramp
upAmp=[t/(numOfSecs*samplesPerSec) for t in range(int((numOfSecs*samplesPerSec)))] #getting equal intervals of 1/Hz
myUpSig=upAmp*np.sin(2*pi*freq*t) #for linearity 

# Looking at the maximum or minimum value can also help with debugging
#print("Maximum value in signal is " + np.max(mySignal).astype('str'))
#print("Minimum value in signal is " + np.min(mySignal).astype('str'))

########## SCALING TO WRITE WAV FILES #######################
# range -32768 to 32767 and cast to 16-bit integers as so:
scaled=np.int16(mySignal*maxInt)
scaledOdd=np.int16(myOddSig*maxInt)
scaledUp=np.int16(myUpSig*maxInt)
scaledSquare=np.int16(squareSig*maxInt)

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




###### Ramp of sine function (Amp. Increasing.) ##########
fw2=wave.openfp('sampleSinRamp.wav','wb')
fw2.setnframes(samplesPerSec)
fw2.setsampwidth(2)
fw2.setnchannels(1) #mono
fw2.setframerate(samplesPerSec)
data2 =scaledUp
fw2.writeframesraw(data2)
fw2.close()

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


######### PLOTTING ######################
# Plotting is useful unless it is a long sound, then it will take
# too long to display (unless you display only some of the elements ...)
#If a plot shows up solid color, do (t[:100], (variable)[:100]) to see values better
plt.plot(t,mySignal) ##x-axis is t (time), y-axis is mySignal (amps)
plt.plot(t,scaledUp) #ramp
plt.plot(t,myOddSig) #odd
plt.plot(t,squareSig)
plt.show()
