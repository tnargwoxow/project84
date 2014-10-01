#! /usr/bin/python

import showisk



''' 
Create a show based on the functionality provided in showisk.py.
You can define 
'''

# names of the main characters, to make description of the plan and reporting easier
names = ['Antagonist','Alpha','Intellectual','Cancerfriend','Redhead','Megatroll']

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
    {'Antagonist': {'ishuman':None},
     'Alpha': {'ishuman':None},
     'Intellectual': {'ishuman':None},
     'Cancerfriend': {'ishuman':None},
     'Redhead': {'ishuman':None},
     'Megatroll': {'ishuman':None},
     'Audience': {'':None},
    },
   # Get headphones then start part 1
    {'Antagonist': {'Antagoniststart':None},
     'Alpha': {'Alphastart':None},
     'Intellectual':  {'Intellectualstart':None},
     'Cancerfriend': {'Cancerfriendstart':None},
     'Redhead': {'Redheadstart':None},
     'Megatroll':   {'Megatrollstart':None},
     'Audience': {'Audiencestart':None},
    },
    {'Antagonist': {'Antagonist01':None},
     'Alpha': {'Alpha01':None},
     'Intellectual':  {'Intellectual01':None},
     'Cancerfriend': {'Cancerfriend01':None},
     'Redhead': {'Redhead01':None},
     'Megatroll':   {'Megatroll01':None},
     'Audience': {'Audience01':None},
    },
    {'Antagonist': {'Antagonist02':None},
     'Alpha': {'Alpha02':None},
     'Intellectual':  {'Intellectual02':None},
     'Cancerfriend': {'Cancerfriend02':None},
     'Redhead': {'Redhead02':None},
     'Megatroll':   {'Megatroll02':None},
     'Audience': {'Audience02':None},
    },
    {'Antagonist': {'Antagonist03':None},
     'Alpha': {'Alpha03':None},
     'Intellectual':  {'Intellectual03':None},
     'Cancerfriend': {'Cancerfriend03':None},
     'Redhead': {'Redhead03':None},
     'Megatroll':   {'Megatroll03':None},
     'Audience': {'Audience03':None},
    },
    {'Antagonist': {'Antagonist04':None},
     'Alpha': {'Alpha04':None},
     'Intellectual':  {'Intellectual04':None},
     'Cancerfriend': {'Cancerfriend04':None},
     'Redhead': {'Redhead04':None},
     'Megatroll':   {'Megatroll04':None},
     'Audience': {'Audience04':None},
    },
    {'Antagonist': {'Antagonist05':None},
     'Alpha': {'Alpha05':None},
     'Intellectual':  {'Intellectual05':None},
     'Cancerfriend': {'Cancerfriend05':None},
     'Redhead': {'Redhead05':None},
     'Megatroll':   {'Megatroll05':None},
     'Audience': {'Audience05':None},
    },
    {'Antagonist': {'Antagonist06':None},
     'Alpha': {'Alpha06':None},
     'Intellectual':  {'Intellectual06':None},
     'Cancerfriend': {'Cancerfriend06':None},
     'Redhead': {'Redhead06':None},
     'Megatroll':   {'Megatroll06':None},
     'Audience': {'Audience06':None},
    },
    {'Antagonist': {'Antagonist07':None},
     'Alpha': {'Alpha07':None},
     'Intellectual':  {'Intellectual07':None},
     'Cancerfriend': {'Cancerfriend07':None},
     'Redhead': {'Redhead07':None},
     'Megatroll':   {'Megatroll07':None},
     'Audience': {'Audience07':None},
    },
    {'Antagonist': {'Antagonist08':None},
     'Alpha': {'Alpha08':None},
     'Intellectual':  {'Intellectual08':None},
     'Cancerfriend': {'Cancerfriend08':None},
     'Redhead': {'Redhead08':None},
     'Megatroll':   {'Megatroll08':None},
     'Audience': {'Audience08':None},
    },
    {'Antagonist': {'Antagonist09':None},
     'Alpha': {'Alpha09':None},
     'Intellectual':  {'Intellectual09':None},
     'Cancerfriend': {'Cancerfriend09':None},
     'Redhead': {'Redhead09':None},
     'Megatroll':   {'Megatroll09':None},
     'Audience': {'Audience09':None},
    },
    {'Antagonist': {'Antagonist10':None},
     'Alpha': {'Alpha10':None},
     'Intellectual':  {'Intellectual10':None},
     'Cancerfriend': {'Cancerfriend10':None},
     'Redhead': {'Redhead10':None},
     'Megatroll':   {'Megatroll10':None},
     'Audience': {'Audience10':None},
    },
    {'Antagonist': {'Antagonist11':None},
     'Alpha': {'Alpha11':None},
     'Intellectual':  {'Intellectual11':None},
     'Cancerfriend': {'Cancerfriend11':None},
     'Redhead': {'Redhead11':None},
     'Megatroll':   {'Megatroll11':None},
     'Audience': {'Audience11':None},
    },
    {'Antagonist': {'Antagonist12':None},
     'Alpha': {'Alpha12':None},
     'Intellectual':  {'Intellectual12':None},
     'Cancerfriend': {'Cancerfriend12':None},
     'Redhead': {'Redhead12':None},
     'Megatroll':   {'Megatroll12':None},
     'Audience': {'Audience12':None},
    },
    {'Antagonist': {'Antagonist13':None},
     'Alpha': {'Alpha13':None},
     'Intellectual':  {'Intellectual13':None},
     'Cancerfriend': {'Cancerfriend13':None},
     'Redhead': {'Redhead13':None},
     'Megatroll':   {'Megatroll13':None},
     'Audience': {'Audience13':None},
    },
    {'Antagonist': {'Antagonist14':None},
     'Alpha': {'Alpha14':None},
     'Intellectual':  {'Intellectual14':None},
     'Cancerfriend': {'Cancerfriend14':None},
     'Redhead': {'Redhead14':None},
     'Megatroll':   {'Megatroll14':None},
     'Audience': {'Audience14':None},
    },
    ]


# create a new show
show = showisk.Show(names, audioPlan, audiencePhone=None, username='admin', pswd='Pr0ject84')
#show = showisk.Show(names, audioPlan, audiencePhone='', username='admin', pswd='L1v3pupp3t5')


# set some configuration parameters. For example the audio directory or the full path for commonly
# played sounds like the beep or 'press 1'. No need to set everything, there are default values.
show.audiodir = '/audio/'
show.press1 = '/audio/press-1'
show.register ='/audio/Register1'
show.nothuman = '/audio/nothuman'
show.register2 = '/audio/Register2'		# asked when calling in
show.triggerPreshow = '/audio/ShowStart1'		# to be played at the trigger phone just before begin()
show.triggerDuringShow = '/audio/ShowStart2' # to be played at the trigger phone during begin()
show.registerconf = '/audio/RegisterConf'
show.tryAgain = '/audio/please-try-again'
show.whenReconnected = '/audio/reconnected'
show.thankyou = '/audio/thankyou'

# the phones that we can call from to begin the main show. Add as many as you like
triggerPhones = ['']
#show.collectPhones(triggerPhones)
# collect phones, you can also add an optional maximum delay in case no call from a trigger phone is made
# we have collected phones. begin the show#
show.begin(['61413817002'])
#show.begin(['61413817002'])