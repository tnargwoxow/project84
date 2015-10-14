__author__ = 'Administrator'
#from tkinter import *
#from tkinter import ttk

import subprocess
import os
import re
#os.system(r'python "C:\Users\Administrator\Documents\UNI\Performing\Lucille and Grant\LucilleGrantShowScript\AudienceAudioIntegrator.py" 123 321 433 55576')

# Display python processes (and have ability to kill them)
# Show cpu usage
# Display active calls through asterisk
  #asterisk -rx 'Sip show calls'
# Confirm that SIP Audience phone is working
# Start the show
# Show each phone being picked up using status lights (grey = nothing, red = failed, orange = connecting, blue = waiting for pres 1, green = good)



#logline="Registering Actor1 with channel 123572@$UHgdfvsdf34567 and call uniqueID 99asdg999999"
logline="ABLETON Audience02 Playing audio file Press-1 to Actor1. Finished"
#logline="ABLETON Audience123124d3123216 Originating call to Actor1 61413817002 Response: Abcdefg"



# Show log of all errors
# Have instant termination button (ends program, kills all python processes, restart asterisk, dumpts time of event into a log file with all logging of the show)

#
#root=Tk()
#root.title("Title")
#Label(text="hithere").pack()
#mainframe= ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0,sticky=(N, W, E, S))
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0, weight=1)
#for child in mainframe.winfo_children():child.grid_configure(pax=5,pady=5)
#root.mainloop()
#
import Tkinter as tk
from Tkinter import *
import ttk
import threading
import Queue as queue
import time


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.queue = queue.Queue()
        self.listbox = tk.Listbox(self, width=20, height=5)
        self.progressbar = ttk.Progressbar(self, orient='horizontal',
                                           length=300, mode='determinate')
        self.button = tk.Button(self, text="Start", command=self.spawnthread)
        self.listbox.pack(padx=10, pady=10)
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def spawnthread(self):
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue)
        self.thread.start()
        self.periodiccall()

    def periodiccall(self):
        self.checkqueue()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.button.config(state="active")

    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.listbox.insert('end', msg)
                self.button["text"]="NOO"
                self.progressbar.step(25)
            except queue.Empty:
                pass


class ThreadedClient(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(1, 5):
            time.sleep(2)
            msg = "Function %s finished..." % x
            print msg
            self.queue.put(msg)


if __name__ == "__main__":
    app = App()
    app.mainloop()