__author__ = 'Administrator'
print "HI"
import subprocess
import sys
import AudioPlayer
args="ssh ec2-user@54.210.51.206"+ " -tt -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" "+ "sudo python /home/ec2-user/project84/debugger.py"


#ssh ec2-user@54.210.51.206"+ " -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" sudo -s"+ " /home/ec2-user/project84/showisk.py"
ssh=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
while ssh.poll() is None:
    line = ssh.stdout.readline()
    sys.stdout.write(line)
    if "ABLETON" in line:
        stringtocut=line
        print stringtocut + " This is the string to cut"
        if "/audio/" in stringtocut:
            cutstring=stringtocut[15:].rstrip()+".wav"
        else:
            cutstring=stringtocut[8:].rstrip()+".wav"
        print cutstring+"THISISTHEFILE"
        audiofile="C:\\Users\\Administrator\\Documents\\UNI\\Performing\\Felicity Nicols - 1984\\Technical\\AudioFiles\\Split\\"+cutstring
        AudioPlayer.playInThread(audiofile)





    #    #if result == []:
    #    #    error = ssh.stderr.readlines()
    #    #    print >>sys.stderr, "ERROR: %s" % error
    #    #else:
#    #    print result
