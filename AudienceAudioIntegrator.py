__author__ = 'Administrator'
print "HI"
import subprocess
import sys
import AudioPlayer
import re


import Tkinter as tk
from Tkinter import *
import ttk
import threading
import Queue as queue
import time

#GLOBAL VARIABLE
global startstring

class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.queue = queue.Queue()

        self.status1 = Label(self, width=15, height=2, text="unloaded", bg="red");self.status2 = Label(self, width=15, height=2, text="unloaded", bg="red")
        self.status3 = Label(self, width=15, height=2, text="unloaded", bg="red");self.status4 = Label(self, width=15, height=2, text="unloaded", bg="red")
        self.statuslist = [self.status1,self.status2,self.status3,self.status4]
        self.id1 = Label(self, width=15, height=2, text="id", bg="red");self.id2 = Label(self, width=15, height=2, text="id", bg="red")
        self.id3 = Label(self, width=15, height=2, text="id", bg="red");self.id4 = Label(self, width=15, height=2, text="id", bg="red")
        self.idlist=[self.id1,self.id2,self.id3,self.id4]
        self.mobile1 = Label(self, width=15, height=2, text="mobile", bg="red");self.mobile2 = Label(self, width=15, height=2, text="mobile", bg="red")
        self.mobile3 = Label(self, width=15, height=2, text="mobile", bg="red");self.mobile4 = Label(self, width=15, height=2, text="mobile", bg="red")
        self.mobilelist=[self.mobile1,self.mobile2,self.mobile3,self.mobile4]
        self.currentrecording1 = Label(self, width=15, height=2, text="mobile", bg="red");self.currentrecording2 = Label(self, width=15, height=2, text="mobile", bg="red")
        self.currentrecording3 = Label(self, width=15, height=2, text="mobile", bg="red");self.currentrecording4 = Label(self, width=15, height=2, text="mobile", bg="red")
        self.currentrecordinglist=[self.currentrecording1,self.currentrecording2,self.currentrecording3,self.currentrecording4]
        self.input1 = Entry(self, width=15, text="enter1", bg="white");self.input2 = Entry(self, width=15, text="enter2", bg="white")
        self.input3 = Entry(self, width=15, text="enter3", bg="white");self.input4 = Entry(self, width=15, text="enter4", bg="white")
        self.inputlist=[self.input1,self.input2,self.input3,self.input4]

        self.button = Button(self, text="Start", command=self.spawnthread)

        self.whichrecording=Entry(self, width=15, text="whichrecording", bg="white")
        self.status1.grid(row=0,column=1);self.status2.grid(row=0,column=2)
        self.status3.grid(row=0,column=3);self.status4.grid(row=0,column=4)
        self.id1.grid(row=1,column=1);self.id2.grid(row=1,column=2);self.id3.grid(row=1,column=3);self.id4.grid(row=1,column=4)
        self.mobile1.grid(row=2,column=1);self.mobile2.grid(row=2,column=2);self.mobile3.grid(row=2,column=3);self.mobile4.grid(row=2,column=4)
        self.currentrecording1.grid(row=3,column=1);self.currentrecording2.grid(row=3,column=2);self.currentrecording3.grid(row=3,column=3)
        self.currentrecording4.grid(row=3,column=4)
        self.input1.grid(row=4,column=1);self.input2.grid(row=4,column=2);self.input3.grid(row=4,column=3);self.input4.grid(row=4,column=4)
        self.whichrecording.grid(row=5, column=3)
        self.button.grid(row=5, column=2)

    def spawnthread(self):
        if self.input1.get()=="986":
          prepend=""
        else:
          prepend="didlogic-trunk/"
        self.startstring=prepend+self.input1.get()+" "+"didlogic-trunk/"+self.input2.get()+" "+"didlogic-trunk/"+self.input3.get()+" "+"didlogic-trunk/"+self.input4.get()+" "+self.whichrecording.get()
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue,self.startstring)
        self.thread.start()
        self.periodiccall()

    def periodiccall(self):
        self.checkqueue()
    def checkqueue(self):
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.button.config(state="active")
        while self.queue.qsize():
            try:
                self.actorlist=self.queue.get(0)

            except queue.Empty:
                pass
        try:
          for i in range(len(self.actorlist)):

            try: self.statuslist[i]["text"]=self.actorlist[i].name
            except:pass
            try: self.statuslist[i]["bg"]=self.actorlist[i].call_status
            except:pass
            try: self.idlist[i]["text"]=self.actorlist[i].uniqueID
            except:pass
            try: self.idlist[i]["bg"]="grey"
            except:pass
            try:self.mobilelist[i]["text"]=self.actorlist[i].number
            except:pass
            try:self.mobilelist[i]["bg"]="grey"
            except:pass
            try:self.currentrecordinglist[i]["text"]=self.actorlist[i].section[0]
            except:pass
            try:self.currentrecordinglist[i]["bg"]=self.actorlist[i].section[1]
            except:pass

        except:
          pass


class ThreadedClient(threading.Thread):
    def __init__(self, queue, startstring):
        threading.Thread.__init__(self)
        self.queue = queue
        self.startstring = startstring

    def run(self):
        args="ssh ec2-user@52.64.208.135"+ " -tt -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" "+ "sudo python /home/ec2-user/project84/5318008Show.py "+self.startstring
        print args
        systemwarning=""
        response="" #define the response temporary variable so it can never be undefined

        #Define class Actor()
        class Actor:
          #Actor() variable declarations
          call_status="grey"; name="undefined"; number=""; warning=""
          uniqueID="empty"; channel=""; section=["NotStart","inactive"]
          log=""; originateresponse=""

          def parselog(self,logline):
            #Function that parses the line of the log to generate status
            self.log+=logline
            if "Originating call to" in logline:
              try:
                pattern=re.search("Originating call to "+self.name+" (\d+) Response: (.+)",logline)
                self.call_status="orange"
                self.number=pattern.group(1)
                self.originateresponse=pattern.group(2)
              except:
                self.log+="WARNING - This error occurred (STILL TO ADD)"
                self.warning+="Failed to show status of call origination"
            if "Registering "+self.name+" with channel" in logline:
              try:
                pattern= re.search("Registering "+self.name+" with channel (.+) and call uniqueID (.+)",logline)
                self.channel=pattern.group(1)
                self.uniqueID=pattern.group(2)
              except:
                self.log+="WARNING - This error occurred (STILL TO ADD)"
                self.warning+="Failed to show status of channel registration and uniqueID"
            if "Success establishing call" in logline:
              self.call_status="blue"
            if "***Hangup***  Will try to call back" in logline:
              self.call_status="purple"
            if "WARNING: playback ended for" in logline: #without a thready waiting for it
              self.warning+="No thread waiting after playback ended, possible orphan"
            if "answered a call, which is not originated, or waiting to be answered" in logline:
              self.warning+="Answered a call without that call being made, possible oprhan"
            if "======WARNING! CANCEL SHOW! The Call to" in logline:
              self.status="red"
              self.warning="User did not answer the call, Cancel the show!"
            if "======================WARNING! PERFORMANCE MUST BE RESTARTED, Cancel the show!":
              self.status="red"
              self.warning="User did not press 1 on time, Cancel the show!"
            if "Playing audio file" in logline:

              try:

                #sys.stdout(logline)
                patty=re.search("Playing audio file (.+) to "+self.name,logline)
                #print "compare this "+patty.group(3)
                #testy=str(''.join(patty.group(3)))
                #sys.stdout.write(testy)
                #print testy
                #sys.stdout.write("nahnah here")
                #if str(patty.group(3)) == "Success":
                #  #print "HI THERE" + self.call_status
                #  value="blue"
                #  self.call_status="green"
                #elif patty.group(3) == "Finished":
                #  value="green"
                #else:
                #  value="yellow"
                self.section=patty.group(1)
              except:
                #e=sys.exc_info()[0]
                #sys.stdout(e)
                pass
                self.log+="WARNING - This error occurred (STILL TO ADD)"
                self.warning+="Failed to show status of audio file playing"


        class Audience:
          name="Audience"
          section="NotStart"
          log=""
          warning=""

          def audienceparse(self,logline):
            if "ABLETON" in logline:
              try:
                pattern=re.search("ABLETON Audience(\d+)",logline)
                self.section=pattern.group(1)
              except:
                self.log+="WARNING - This error occurred (STILL TO ADD)"
                self.warning+="Failed to show status of audio file playing"
        #Initiate actor names
        Audience1=Audience()
        Actor1 = Actor();Actor2=Actor();Actor3=Actor();Actor4=Actor();Actor5=Actor();Actor6=Actor()
        actorlist = [Actor1,Actor2,Actor3,Actor4,Actor5,Actor6]
        for member in actorlist:
          member.name="Actor"+str(actorlist.index(member)+1)

        # Display if server is on (what speed it is running at)
        def server_online(host):
          #Call with hostname, returns status (1,0)
          value = (subprocess.Popen("ping -n 1 "+host,stdout=subprocess.PIPE,stderr=subprocess.PIPE))
          for line in value.stdout:
            if "Packets:" in line:
              if "Received = 0" in line:
                return False
              else:
                return True

        status=server_online("localhost")
        if status:
          print "Green light, online"
        else:
          print "Red light, offline"

        #
        ssh=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
        while ssh.poll() is None:
          #thisthing=file.readlines(file("C:\\a.txt"))
            line = ssh.stdout.readline()
            logline=line
            sys.stdout.write(line)
            if "ABLETON" in line:
                stringtocut=line
                if "Audience01" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq01.wav"
                elif "Audience02" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq02.wav"
                elif "Audience03" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq03.wav"
                elif "Audience04" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq04.wav"
                elif "Audience05" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq05.wav"
                elif "Audience06" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq06.wav"
                elif "Audience07" in stringtocut:
                    audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Lucille and Grant\\Call for 5318008\\AutomationScripts\\showAudio\\Split\\Audiencehq07.wav"
                else:
                    audiofile=""
                print "==--==COMPTUER IS PLAYING THIS "+audiofile +"==--=="
                if audiofile!="":
                    AudioPlayer.playInThread(audiofile)
                else:
                    print "==--==NO SUCH AUDIENCE FILE==--=="
            if "Audience" in logline:
              try:
                Audience1.audienceparse(logline)
              except:
                systemwarning+="Couldn't use audience parser, I need to put the error code into here"

            if "Actor" in logline:
              try:
                response=re.search('(Actor[\d])[\s|.]',logline).group(1)
              except:
                pass
                systemwarning+="There was an error getting to the actor field for status viewing, I need to put the error code into here"
              if response:
                try:
                  eval(response).parselog(logline)
                except TypeError as e:
                  print e
                except:
                  print "ERROR - THIS type error occurred"+sys.exc_info()[0]
                  systemwarning+="There was an error getting to the actor field for status viewing, I need to put the error code into here"

            #print Actor1.channel
            #print Actor1.uniqueID
            #print Actor1.section
            #print Actor1.number
            ##print Actor1.log
            #print systemwarning
            #print Audience1.section
            self.queue.put(actorlist)

if __name__ == "__main__":
    app = App()
    app.mainloop()









