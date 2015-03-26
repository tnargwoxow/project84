__author__ = 'Administrator'
import time
import pymedia.audio.sound as sound
import pygame
import wave
import os
import pyglet
import sys
import threading
from multiprocessing import Process


def playwav(fname):
    f=wave.open(fname,'rb')
    sampleRate= f.getframerate()
    channels= f.getnchannels()
    format= sound.AFMT_S16_LE
    snd= sound.Output( sampleRate, channels, format )
    s=' '
    time.sleep(0.2)
    while len( s )>0:
       s= f.readframes( 100 ) #TODO: May need to fix this up
       snd.play( s )
    while snd.isPlaying(): time.sleep( 0.05 )
def playInThread(fname):
    thread1=threading.Thread(target=playwav, args=(fname,))
    thread1.daemon = False
    thread1.start()


#-------------------------------------------
#if __name__== '__main__':
    #playInThread("C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience04.wav")
    #print "I PLAYED IT"
    #print "HI"
    #line ="ABLETON /audio/Alpha_01"
    #if "ABLETON" in line:
    #    stringtocut=line
    #    print stringtocut
    #    cutstring=stringtocut[15:]+".wav"
    #    print cutstring
    #    audiofile="C:\\"+cutstring
    #    print audiofile
    #
    #    playInThread(audiofile)
    #    #thread1.start()
    #    time.sleep(3)
    #
    #    playInThread("C:\\Ding.wav")
    #    print "alpha2"
    #    playInThread("C:\\Ding.wav")
    #    print "alpha2"
    #    time.sleep(1)
    #    playInThread("C:\\chimes.wav")
    #    print "alpha2"
    #    time.sleep(1)
    #    playInThread("C:\\chord.wav")
    #    print "alpha2"
    #    time.sleep(1)
    #    playInThread("C:\\Ding.wav")
    #    print "alpha2"
    #    playInThread("C:\\Ding.wav")
    #    print "alpha2"
    #    time.sleep(1)
    #    playInThread("C:\\Ding.wav")
    #    print "alpha2"
    #    playInThread("C:\\Ding.wav")
    #    print "alpha2"
        #TODO: ADD ANOTHER TRACK HERE
#
##  if len( sys.argv )!= 2:
##    print "Usage: play_wav <file>"
##  else:
##    playwav( sys.argv[ 1 ] )
##

##


#TODO: CHECK THIS CODE I DIDN"T WRITE OUT
#I don't suppose it's particularly elegant, but I opened a pipe to a background MPlayer process.
#
#import subprocess
#player = subprocess.Popen(["mplayer", "song.mp3", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#Then, when I wanted to terminate the MPlayer process, I simply wrote "q" for quit to the pipe.
#
#player.stdin.write("q")
#Look at MPlayer documentation for all sorts of commands you can pass in this way to control playback.
#
#Hopefully that's somewhat helpful!