__author__ = 'Administrator'
print "HI"
import os
import subprocess
import time
import sys
args="ssh ec2-user@54.210.51.206"+ " -tt -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" "+ "sudo python /home/ec2-user/project84/showisk.py"


#ssh ec2-user@54.210.51.206"+ " -i "+ '"C:/Users/Administrator/Documents/UNI/Performing/Felicity Nicols - 1984/Technical/GrantCONNECT.pem"'+" sudo -s"+ " /home/ec2-user/project84/showisk.py"
ssh=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
while ssh.poll() is None:
    line = ssh.stdout.readline()
    if "Playing audio file with channel" in line:
        print "FUCK YEAH! THEYRE HERE!"
    sys.stdout.write(line)




    #    #if result == []:
    #    #    error = ssh.stderr.readlines()
    #    #    print >>sys.stderr, "ERROR: %s" % error
    #    #else:
#    #    print result
