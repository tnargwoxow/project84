#! /usr/bin/python

import showisk



''' 
Create a show based on the functionality provided in showisk.py.
You can define 
'''

# names of the main characters, to make description of the plan and reporting easier
names = ['burnP1','burnP2','burnP3','burnP4']

'''
The audio plan is structured as follows: It is a list of periods. A period is the sync checkpoint
for all actors. All actors should complete their path of actions before starting the next period.
A period is a list of trees, one for each actor (technically is a dict/map of trees)
A tree is a tree of actions and possible options that an Actor has at a given period. An action
is an audio file to be played. A tree is represented as a dictionary (of possibly nested
dictionaries). Generally in Python, a dictionary, has  multiple entries of the form key:value
separated with commas. In our tree representation, if a key has non-numeric value then it is
interpreted as an audio filename to be played. The value of the key is the next action to take.
'None' means that nothing happens and we are done. The value can also be another tree! If the key
values are numeric, then the program interprets this as a choice that needs to be made by the user
by pressing a number in the phone keypad (DTMF tones). Once the choice is made and is valid, then
the value of the corresponding key is the action. It can be a simple filename (in which case the
corresponding filename is played and we are done) or it can be another tree. This way we can
build arbitrarily complex trees of actions and options. When creating options it is a good idea for
the preceding audio file to explain these options and ask you to take them. For example if we have
this tree {'blah':{1:'hi', 2:'bye'}} it will play the 'blah' and then just wait for a DTMF tone.
So the valid options should be given and explained at the end of audio file 'blah'
If the DTMF tone pressed is not one of the options given, it will 'say please try again'
The program will try to get a correct input for x secs (x=30 by default). Giving an invalid
input will not reset this timer. If no valid option is given, a default option will be taken by
the program. Currenly th default option is 1, but you one can easily change this when calling
the function waitForDTMF
'''

audioPlan = [
    # Hi to humans
    {'burnP1': {'burnishuman':None},
     'burnP2': {'burnishuman':None},
     'burnP3': {'burnishuman':None},
     'burnP4': {'burnishuman':None},
     'Audience': {'burnishuman':None},
    },
    {'burnP1': {'burnP101':None},
     'burnP2': {'burnP201':None},
     'burnP3': {'burnP301':None},
     'burnP4': {'burnP401':None},
     'Audience': {'burnAudience01':None},
    },
    {'burnP1': {'burnP102':None},
     'burnP2': {'burnP202':None},
     'burnP3': {'burnP302':None},
     'burnP4': {'burnP402':None},
     'Audience': {'burnAudience02':None},
    },
    {'burnP1': {'burnP103':None},
     'burnP2': {'burnP203':None},
     'burnP3': {'burnP303':None},
     'burnP4': {'burnP403':None},
     'Audience': {'burnAudience03':None},
    },
    {'burnP1': {'burnP104':None},
     'burnP2': {'burnP204':None},
     'burnP3': {'burnP304':None},
     'burnP4': {'burnP404':None},
     'Audience': {'burnAudience04':None},
    },
    {'burnP1': {'burnP105':None},
     'burnP2': {'burnP205':None},
     'burnP3': {'burnP305':None},
     'burnP4': {'burnP405':None},
     'Audience': {'burnAudience05':None},
    },
    {'burnP1': {'burnP106':None},
     'burnP2': {'burnP206':None},
     'burnP3': {'burnP306':None},
     'burnP4': {'burnP406':None},
     'Audience': {'burnAudience06':None},
    },

    ]


# create a new show
show = showisk.Show(names, audioPlan, audiencePhone='61413817002', username='admin', pswd='Pr0ject84')
#show = showisk.Show(names, audioPlan, audiencePhone='', username='admin', pswd='L1v3pupp3t5')


# set some configuration parameters. For example the audio directory or the full path for commonly
# played sounds like the beep or 'press 1'. No need to set everything, there are default values.
show.audiodir = '/audio/'
show.press1 = '/audio/burnpress1'
show.register ='/audio/Register1'
show.nothuman = '/audio/burnnothuman'
show.register2 = '/audio/Register2'		# asked when calling in
show.triggerPreshow = '/audio/ShowStart1'		# to be played at the trigger phone just before begin()
show.triggerDuringShow = '/audio/ShowStart2' # to be played at the trigger phone during begin()
show.registerconf = '/audio/RegisterConf'
show.tryAgain = '/audio/please-try-again'
show.whenReconnected = '/audio/burnreconnected'
show.thankyou = '/audio/burnthankyou'

# the phones that we can call from to begin the main show. Add as many as you like
triggerPhones = ['']
#show.collectPhones(triggerPhones)
# collect phones, you can also add an optional maximum delay in case no call from a trigger phone is made
# we have collected phones. begin the show#
show.begin(['61431956912','61431736473','61438918180','61438242444'],randomShuffle=False,)
#show.begin()
#show.begin(['61415867748'])