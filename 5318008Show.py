#! /usr/bin/python

import showisk



''' 
Create a show based on the functionality provided in showisk.py.
You can define 
'''

# names of the main characters, to make description of the plan and reporting easier
names = ['P1','P2','P3','P4']

audioPlan = [
    # Hi to humans
    {'P1': {'ishuman':None},
     'P2': {'ishuman':None},
     'P3': {'ishuman':None},
     'P4': {'ishuman':None},
     'Audience': {'ishuman':None},
    },
    {'P1': {'P101':None},
     'P2': {'P201':None},
     'P3': {'P301':None},
     'P4': {'P401':None},
     'Audience': {'Audience01':None},
    },
    {'P1': {'P102':None},
     'P2': {'P202':None},
     'P3': {'P302':None},
     'P4': {'P402':None},
     'Audience': {'Audience02':None},
    },
    {'P1': {'P103':None},
     'P2': {'P203':None},
     'P3': {'P303':None},
     'P4': {'P403':None},
     'Audience': {'Audience03':None},
    },
    {'P1': {'P104':None},
     'P2': {'P204':None},
     'P3': {'P304':None},
     'P4': {'P404':None},
     'Audience': {'Audience04':None},
    },
    {'P1': {'P105':None},
     'P2': {'P205':None},
     'P3': {'P305':None},
     'P4': {'P405':None},
     'Audience': {'Audience05':None},
    },
    {'P1': {'P106':None},
     'P2': {'P206':None},
     'P3': {'P306':None},
     'P4': {'P406':None},
     'Audience': {'Audience06':None},
    },
    {'P1': {'P107':None},
     'P2': {'P207':None},
     'P3': {'P307':None},
     'P4': {'P407':None},
     'Audience': {'Audience07':None},
    },

    ]


# create a new show
show = showisk.Show(names, audioPlan, audiencePhone='986', username='admin', pswd='Pr0ject84')
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
#show.begin(['986','','',''],randomShuffle=False,)
#show.begin()
show.begin(['986'])