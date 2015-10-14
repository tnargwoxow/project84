#! /usr/bin/python

import showisk
from sys import argv


''' 
Create a show based on the functionality provided in showisk.py.
You can define 
'''

# names of the main characters, to make description of the plan and reporting easier
names = ['Actor1','Actor2','Actor3','Actor4']
numbers=[]
for number in argv[1:5]:
  print number
  if number:
    numbers.append(number)
try:
  startat=int(argv[5])
except:
  startat=0
  pass
audioPlan = [
    # Hi to humans
    {'Actor1': {'ishuman':None},
     'Actor2': {'ishuman':None},
     'Actor3': {'ishuman':None},
     'Actor4': {'ishuman':None},
     'Audience': {'ishuman':None},
    },
    {'Actor1': {'P101':None},
     'Actor2': {'P201':None},
     'Actor3': {'P301':None},
     'Actor4': {'P401':None},
     'Audience': {'Audience01':None},
    },
    {'Actor1': {'P102':None},
     'Actor2': {'P202':None},
     'Actor3': {'P302':None},
     'Actor4': {'P402':None},
     'Audience': {'Audience02':None},
    },
    {'Actor1': {'P103':None},
     'Actor2': {'P203':None},
     'Actor3': {'P303':None},
     'Actor4': {'P403':None},
     'Audience': {'Audience03':None},
    },
    {'Actor1': {'P104':None},
     'Actor2': {'P204':None},
     'Actor3': {'P304':None},
     'Actor4': {'P404':None},
     'Audience': {'Audience04':None},
    },
    {'Actor1': {'P105':None},
     'Actor2': {'P205':None},
     'Actor3': {'P305':None},
     'Actor4': {'P405':None},
     'Audience': {'Audience05':None},
    },
    {'Actor1': {'P106':None},
     'Actor2': {'P206':None},
     'Actor3': {'P306':None},
     'Actor4': {'P406':None},
     'Audience': {'Audience06':None},
    },
    {'Actor1': {'P107':None},
     'Actor2': {'P207':None},
     'Actor3': {'P307':None},
     'Actor4': {'P407':None},
     'Audience': {'Audience07':None},
    },

    ]


# create a new show
show = showisk.Show(names, audioPlan[startat:], audiencePhone='didlogic-trunk/61404504804', username='admin', pswd='Pr0ject84')
#show = showisk.Show(names, audioPlan, audiencePhone='', username='admin', pswd='L1v3pupp3t5')


# set some configuration parameters. For example the audio directory or the full path for commonly
# played sounds like the beep or 'press 1'. No need to set everything, there are default values.
show.audiodir = '/audio/5318008/'
show.press1 = '/audio/5318008/press1'
show.register ='/audio/5318008/Register1'
show.nothuman = '/audio/5318008/nothuman'
show.register2 = '/audio/5318008/Register2'		# asked when calling in
show.triggerPreshow = '/audio/5318008/ShowStart1'		# to be played at the trigger phone just before begin()
show.triggerDuringShow = '/audio/5318008/ShowStart2' # to be played at the trigger phone during begin()
show.registerconf = '/audio/5318008/RegisterConf'
show.tryAgain = '/audio/please-try-again'
show.whenReconnected = '/audio/5318008/reconnected'
show.thankyou = '/audio/5318008/thankyou'
show.pathToTrunk = 'SIP/'
# the phones that we can call from to begin the main show. Add as many as you like
triggerPhones = ['6111545453']
#show.collectPhones(triggerPhones)
# collect phones, you can also add an optional maximum delay in case no call from a trigger phone is made
# we have collected phones. begin the show#

show.begin(numbers,randomShuffle=False,)
#show.begin()
#show.begin(['986'])