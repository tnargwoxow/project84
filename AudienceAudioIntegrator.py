__author__ = 'Administrator'
print "HI"
import subprocess
import sys
import AudioPlayer
args="ssh ec2-user@54.210.51.206"+ " -tt -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" "+ "sudo python /home/ec2-user/project84/grantShow.py"


#ssh ec2-user@54.210.51.206"+ " -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" sudo -s"+ " /home/ec2-user/project84/showisk.py"
ssh=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
while ssh.poll() is None:
    line = ssh.stdout.readline()
    sys.stdout.write(line)
    if "ABLETON" in line:
        stringtocut=line
        if "Audience01" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience01.wav"
        elif "Audience02" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience02.wav"
        elif "Audience03" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience03.wav"
        elif "Audience04" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience04.wav"
        elif "Audience05" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience05.wav"
        elif "Audience06" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience06.wav"
        elif "Audience07" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience07.wav"
        elif "Audience08" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience08.wav"
        elif "Audience09" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience09.wav"
        elif "Audience10" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience10.wav"
        elif "Audience11" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience11.wav"
        elif "Audience12" in stringtocut:
            audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\Audience12.wav"
        else:
            audiofile=""

        #print stringtocut + " This is the string to cut"
        #if "/audio/" in stringtocut:
        #    cutstring=stringtocut[15:].rstrip()+".wav"
        #else:
        #    cutstring=stringtocut[8:].rstrip()+".wav"
        print "==--==COMPTUER IS PLAYING THIS "+audiofile +"==--=="
        if audiofile!="":
            AudioPlayer.playInThread(audiofile)
        else:
            print "==--==NO SUCH AUDIENCE FILE==--=="





    #    #if result == []:
    #    #    error = ssh.stderr.readlines()
    #    #    print >>sys.stderr, "ERROR: %s" % error
    #    #else:
#    #    print result
