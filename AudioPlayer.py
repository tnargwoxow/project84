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
